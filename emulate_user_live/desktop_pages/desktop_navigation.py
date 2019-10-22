from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from emulate_user_live.desktop_pages import selector_desktop_pages
from emulate_user_live.start_base import BaseLoginPage


class DesktopMethod(BaseLoginPage):
    """ Inheritance of Base Login class who init driver """

    def to_desktop_version(self):
        """ Go to desktop version in m.vk.com and edit profile"""
        full_version = self.driver.find_element(
            By.XPATH, selector_desktop_pages.DESKTOP_VERSION
        )
        self.click_human_like(full_version)
        logger.info("Go to desktop version app")

    def return_to_mobile_version(self):
        """ Go to mobile version from under the desktop vk.com """
        mobile_version = self.driver.find_element(
            By.XPATH, selector_desktop_pages.MOBILE_VERSION
        )
        self.click_human_like(mobile_version)
        logger.info("Return to mobile version")

    def main_page_desktop(self):
        """ Go to start page user account """
        if self.check_element_on_page('//div[@id="box_layer"]'):
            element = self.driver.find_element(By.ID, "box_layer")
            self.driver.execute_script("arguments[0].click();", element)

        my_page = self.driver.find_element(By.XPATH, selector_desktop_pages.MY_PAGE)
        self.click_human_like(my_page)

    def save_changes(self):
        """ Save changes on page """
        # big blue button
        save = self.driver.find_element(By.XPATH, selector_desktop_pages.SAVE)
        save.send_keys(Keys.ENTER)
        logger.info("Save inform on page")
