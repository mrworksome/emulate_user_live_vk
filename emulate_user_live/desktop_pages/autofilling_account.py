from time import sleep
from typing import Dict

from loguru import logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from emulate_user_live.desktop_pages import selector_desktop_pages as sl
from emulate_user_live.desktop_pages.desktop_navigation import DesktopMethod
from emulate_user_live.desktop_pages.field_page import (
    main_fields,
    contact_fields,
    interests_fields,
    university_fields,
    career_fields,
    life_position_fields,
)


class AutoFillAccount(DesktopMethod):
    """ Inheritance DesktopMethod for use element """

    def _fill_page(
        self, selector_page: str, page_fields: Dict, second_selector_on_page: str = None
    ):
        """ filling account information on page """

        page = self.driver.find_element(By.XPATH, selector_page)
        self.click_human_like(page)

        if self.check_element_on_page('//div[@id="box_layer"]'):
            element = self.driver.find_element(By.ID, "box_layer")
            self.driver.execute_script("arguments[0].click();", element)

        # else in page have more 1
        if second_selector_on_page:
            next_page = self.driver.find_element(By.XPATH, second_selector_on_page)
            self.click_human_like(next_page)

        for i in range(len(page_fields)):
            self.upload_identity_user(**page_fields[i])

        self.save_changes()

        try:
            element = WebDriverWait(self.driver, 4).until(EC.alert_is_present())
            element.send_keys(Keys.ENTER)
            logger.info("Close popup")
        except TimeoutException:
            pass

    def filling_user_data(self):
        sleep(2)
        self.to_desktop_version()
        sleep(2)
        self.main_page_desktop()
        sleep(2)

        self._fill_page(sl.EDIT_PROFILE_PAGE, main_fields)
        self._fill_page(sl.CONTACT_PAGE, contact_fields)
        self._fill_page(sl.INTERESTS_PAGE, interests_fields)
        self._fill_page(sl.EDUCATION_PAGE, university_fields, sl.HIGH_EDUCATION)
        self._fill_page(sl.CAREER_PAGE, career_fields)
        self._fill_page(sl.LIFE_POSITION_PAGE, life_position_fields)
        sleep(2)

        # todo: save user_data in Redis
        # todo: add method for upload photo and albums
        # todo: may be a status in main page

        self.conn.hmset(self.login, self.user_data)

        self.return_to_mobile_version()
        sleep(2)

        self.save_session()
        logger.info(f"Account {self.login} is completed!")
