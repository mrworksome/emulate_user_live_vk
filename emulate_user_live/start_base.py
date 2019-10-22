import json
import random
from time import sleep

import redis
from loguru import logger
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    ElementNotInteractableException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from config import HOST, PORT, DB
from emulate_user_live.desktop_pages import selector_desktop_pages as sl
from emulate_user_live.generate_user_data import GenerateUser


class BaseLoginPage(object):
    """ all property in all pages who need auto-fill user content """

    def __init__(self, vk_login: str, vk_password: str):
        self.login = vk_login
        self.password = vk_password
        self.user_data = GenerateUser().create_data()
        self.user_data_group = GenerateUser().create_group()

        # Redis session
        pool = redis.ConnectionPool(host=HOST, port=PORT, db=DB, decode_responses=True)
        self.conn = redis.Redis(
            connection_pool=pool, decode_responses=True, charset="utf-8"
        )

        # start driver
        self.driver = None
        self._start_driver()
        self._vk_auth()

    def _start_driver(self):
        options = Options()
        proxy = ""
        # if proxy:
        #     options.add_argument("--proxy-server=%s" % proxy)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        # todo: replace user agent for generate user data
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36"
        )

        self.driver = webdriver.Chrome(options=options)

    def save_session(self):
        # cookie_path = os.path.join(os.path.dirname(__file__), f'cookie/{self.login}.pkl')
        #
        # with open(cookie_path, 'wb') as cookie_file:
        #     pickle.dump(self.driver.get_cookies(), cookie_file)

        self.conn.hset(self.login, "session", json.dumps(self.driver.get_cookies()))

    def _vk_auth(self):
        """ Authenticate in m.VK.com """
        # mobile version url
        mobile_url = "https://m.vk.com/"

        # cookie_path = os.path.join(os.path.dirname(__file__), f'cookie/{self.login}.pkl')
        self.driver.get(mobile_url)
        self.driver.implicitly_wait(2.5)

        # # upload session
        # if os.path.exists(cookie_path):
        #     with open(cookie_path, 'rb') as cookies_file:
        #         cookies = pickle.load(cookies_file)
        #         for cookie in cookies:
        #             if 'expiry' in cookie:
        #                 del cookie['expiry']
        #             self.driver.add_cookie(cookie)
        #
        #         self.driver.get(mobile_url)

        session = self.conn.hget(self.login, "session")
        if session:
            self.conn.hget(self.login, "session")
            session = json.loads(session)
            for cookie in session:
                if "expiry" in cookie:
                    del cookie["expiry"]
                self.driver.add_cookie(cookie)
            self.driver.get(mobile_url)
        else:
            pass

        # check logged
        if self.check_element_on_page(sl.EMAIL):
            try:
                username = self.driver.find_element(By.XPATH, sl.EMAIL)
                password = self.driver.find_element(By.XPATH, sl.PASSWORD)
                username.clear()
                password.clear()
                self.send_keys_human_like(username, self.login)
                self.send_keys_human_like(password, self.password)

                login = self.driver.find_element_by_xpath('//input[@type="submit"]')
                login.send_keys(Keys.ENTER)

                logger.info(f"Entering credentials for {self.login}")
            except TimeoutException:
                logger.info(f"No entering credentials for {self.login}")
                self.driver.quit()
            except NoSuchElementException:
                logger.info(f"No entering because Element selector changed")
                self.driver.quit()

    @staticmethod
    def send_keys_human_like(element: WebElement, value: str):
        """ Typing value with human like """
        # todo: get value is list and string
        for character in value:
            element.send_keys(character, Keys.ARROW_DOWN)
            sleep(random.uniform(0.2, 0.4))
        sleep(random.uniform(0.5, 1.1))

    @staticmethod
    def click_human_like(element: WebElement):
        """ Click on button human like """
        element.click()
        sleep(random.uniform(0.4, 0.9))

    def check_element_on_page(self, selector):
        """ Find selector on page """
        try:
            self.driver.find_element(By.XPATH, selector)
        except NoSuchElementException:
            return False
        return True

    def upload_identity_user(
        self,
        element_selector: str,
        data_element: str,
        action: str = None,
        container_selector_element: bool = False,
        num_container: int = None,
    ):
        """
        Change or replace element in page on current data

        if we have direct selector value who we change
        else update user_data selector value

        :param element_selector: selector for element
        :param data_element: element in data which we are changing
        :param action: type of change element
        :param container_selector_element: if element in container, need selector container
        :param num_container: number container where located element
        """
        if not container_selector_element:
            if self.check_element_on_page(element_selector):
                element = self.driver.find_element(By.XPATH, element_selector)
                value_element = element.get_attribute("value")
                if value_element:
                    # Update data element
                    self.user_data.update({data_element: value_element})
                    logger.info(
                        f"User data {data_element} update value on {value_element}"
                    )
                else:
                    if self.user_data.get(data_element):
                        # Update parameter on page
                        self.click_human_like(element)
                        self.send_keys_human_like(
                            element, self.user_data.get(data_element)
                        )
                        logger.info(
                            f"User page element {data_element} updated on {self.user_data.get(data_element)}"
                        )
                sleep(random.uniform(1.5, 4.3))
            else:
                logger.info("No Such Element Selector")
                self.driver.quit()

        else:
            # Find element in containers or inputs on page
            container = self.driver.find_elements(By.XPATH, sl.CONTAINERS)[
                num_container
            ]
            # sleep(2)
            # container.click()
            # sleep(3)

            # get attribute value element in container
            container_element = container.find_element(By.XPATH, element_selector)
            value_container = container_element.get_attribute("value")

            # check value element on page by type:
            if value_container.isdigit():
                # Update user data with CUSTOM VALUE
                if action == "click":
                    self.click_human_like(container)
                    if int(value_container) != 0:
                        if self.check_element_on_page(sl.ACTIVE):
                            # if value have selector active
                            element = self.driver.find_element_by_class_name("active")
                        else:
                            # search Value in dropdown list by <li>
                            element = container.find_element_by_class_name(
                                "result_list"
                            ).find_elements_by_tag_name("li")[int(value_container) - 1]
                        value_element = element.get_attribute("title")
                        self.click_human_like(element)
                        if self.user_data.get(data_element):
                            self.user_data.update({data_element: value_element})
                            sleep(random.randint(1, 2))
                            logger.info(
                                f"User data {data_element} change value on "
                                f"{value_element}"
                            )
                        if data_element == "main_gender":
                            self.user_data = GenerateUser().create_interests(
                                self.user_data, value_element
                            )

                    elif int(value_container) == 0:
                        # Change DEFAULT VALUE
                        try:
                            select_value = self.driver.find_element(
                                By.XPATH,
                                f'//li[@title="{self.user_data.get(data_element)}"]',
                            )
                            self.driver.execute_script(
                                "arguments[0].click();", select_value
                            )
                        except ElementNotInteractableException as e:
                            container.click()
                            pass
                        sleep(random.uniform(2.1, 3.2))
                        logger.info(
                            f"DEFAULT value {data_element} change on {self.user_data.get(data_element)}"
                        )

                    elif int(value_container) == -1:
                        # CUSTOM input is full go to second 'hidden' input on value
                        element = self.driver.find_element(By.XPATH, sl.HIDDEN_INPUT)
                        # id group work
                        value_element_custom = element.get_attribute("value")
                        logger.info(
                            f"value {data_element} is custom {value_element_custom}"
                        )

                    # todo: some think about custom value on fields by group id working or subscribe
                    sleep(random.uniform(2.1, 3.2))

                elif action == "send_keys":
                    self.send_keys_human_like(
                        container_element, self.user_data.get(data_element)
                    )
                    element = self.driver.find_element(
                        By.XPATH, f'//li[@title="{self.user_data.get(data_element)}"]'
                    )
                    self.driver.execute_script("arguments[0].click();", element)
                    # self.click_human_like(element)
                    logger.info(
                        f"User data {data_element} input {self.user_data.get(data_element)}"
                    )

                    sleep(random.uniform(2.4, 3.7))

            elif not value_container:
                # if element not attribute  value
                container.click()
                sleep(random.uniform(2.2, 3.8))
                if action == "send_keys":
                    # typing human like
                    element_input = container.find_elements(
                        By.XPATH, sl.SELECTOR_INPUT
                    )[num_container + 1]
                    self.send_keys_human_like(
                        element_input, self.user_data.get(data_element)
                    )
                    self.driver.execute_script("arguments[0].click;")
                    # self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    # todo: waiting by human

                elif action == "click":
                    # select element in drop down list
                    # todo: may be some scrolling for element and click him by visible
                    select_value = container.find_element(
                        By.XPATH, f'//li[@title="{self.user_data.get(data_element)}"]'
                    )
                    self.click_human_like(select_value)
                    logger.info(
                        f"DEFAULT value {data_element} change on "
                        f"{self.user_data.get(data_element)}"
                    )
                sleep(random.uniform(1.7, 2.9))
