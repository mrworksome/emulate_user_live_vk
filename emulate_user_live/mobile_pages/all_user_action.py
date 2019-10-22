import random
import time
from numbers import Number
from time import sleep
from typing import Tuple

from loguru import logger
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from emulate_user_live.generate_user_data import GenerateUser
from emulate_user_live.mobile_pages import selector_mobile_page as mob_sl
from emulate_user_live.start_base import BaseLoginPage


class UserCases(BaseLoginPage):
    """ User Action Cases """

    def scroll_to_element_page(self, element: WebElement):
        """ Action to move element """
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    @staticmethod
    def get_post_params(element):
        """ Get count (like, comment, share )"""
        count_params = element.get_attribute("aria-label")
        return int(count_params.split()[0])

    def _scroll(
        self,
        len_posts: int,
        after_scroll_sleep: Tuple[Number, Number],
        page_length: Tuple[Number, Number],
        second_sleep: Tuple[Number, Number],
        condition_action=None,
        selector_page=None,
    ):
        """ Scroll for all pages """
        sleep(1)

        if selector_page:
            groups_page = self.driver.find_element(By.XPATH, selector_page)
            self.click_human_like(groups_page)

        posts = self.driver.find_elements(By.XPATH, mob_sl.GROUP_POST_LIST)
        count_post_on_page = len(posts)
        sleep(random.uniform(*after_scroll_sleep))

        post = None
        for i in range(len_posts):
            if i == count_post_on_page:
                # self.driver.refresh()
                try:
                    element_present = EC.presence_of_element_located(
                        (By.ID, "show_more_loading")
                    )
                    WebDriverWait(self.driver, 3).until(element_present)
                except TimeoutException:
                    pass
                sleep(random.uniform(*after_scroll_sleep))
                sleep(10)

            if i >= count_post_on_page:
                try:
                    post = self.driver.find_elements(By.XPATH, mob_sl.GROUP_POST_LIST)[
                        i - 1
                    ]
                    self.scroll_to_element_page(post)
                    # time to watch posts
                    sleep(random.uniform(0.4, 1.1))
                except IndexError:
                    location_last_post = post.location["y"]
                    for j in range(location_last_post, 0, -random.randint(420, 1050)):
                        self.driver.execute_script(f"window.scrollTo(0, {j});")
                        sleep(random.uniform(0.5, 1.7))
                    self.driver.execute_script(f"window.scrollTo(0, 0);")
                    self.driver.execute_script("window.history.go(-1)")
                    self.driver.refresh()

            post = self.driver.find_elements(By.XPATH, mob_sl.GROUP_POST_LIST)[i]
            self.scroll_to_element_page(post)
            sleep(random.uniform(*after_scroll_sleep))

            if condition_action:
                getattr(self, condition_action)(post)

        location_last_post = post.location["y"]
        for j in range(location_last_post, 0, -random.randint(*page_length)):
            self.driver.execute_script(f"window.scrollTo(0, {j});")
            sleep(random.uniform(*second_sleep))

        self.driver.execute_script(f"window.scrollTo(0, 0);")

    def _scroll_for_groups(
        self,
        len_posts: int,
        after_scroll_sleep: Tuple[Number, Number],
        page_length: Tuple[Number, Number],
        second_sleep: Tuple[Number, Number],
        condition_action=None,
    ):
        """ Scroll in group with conditions views """
        sleep(1)

        if self.check_element_on_page(mob_sl.GROUP_POST_LIST):
            posts = self.driver.find_elements(By.XPATH, mob_sl.GROUP_POST_LIST)
            count_post_on_page = len(posts)
            condition_to_join_group = random.randint(1000000, 1500000)

            views = 0
            post = None
            for i in range(len_posts):
                if i == count_post_on_page:
                    # self.driver.refresh()
                    try:
                        element_present = EC.presence_of_element_located(
                            (By.ID, "show_more_loading")
                        )
                        WebDriverWait(self.driver, 3).until(element_present)
                    except TimeoutException:
                        pass

                if i >= count_post_on_page:
                    try:
                        post = self.driver.find_elements(
                            By.XPATH, mob_sl.GROUP_POST_LIST
                        )[i - 1]
                        self.scroll_to_element_page(post)
                        # time to watch posts
                        sleep(random.uniform(*after_scroll_sleep))
                    except IndexError:
                        location_last_post = post.location["y"]
                        for j in range(
                            location_last_post, 0, -random.randint(*page_length)
                        ):
                            self.driver.execute_script(f"window.scrollTo(0, {j});")
                            sleep(random.uniform(*after_scroll_sleep))
                        self.driver.execute_script(f"window.scrollTo(0, 0);")
                        self.driver.execute_script("window.history.go(-1)")
                        self.driver.refresh()

                # condition for views to join group
                try:
                    views_on_post = post.find_element_by_class_name("item_views ")
                    views += self.get_post_params(views_on_post)
                except AttributeError:
                    views += 0

                post = self.driver.find_elements(By.XPATH, mob_sl.GROUP_POST_LIST)[i]
                self.scroll_to_element_page(post)
                sleep(random.uniform(*after_scroll_sleep))

                if condition_action:
                    getattr(self, condition_action)(post)

            location_last_post = post.location["y"]
            for j in range(location_last_post, 0, -random.randint(*page_length)):
                self.driver.execute_script(f"window.scrollTo(0, {j});")
                sleep(random.uniform(*second_sleep))

            self.driver.execute_script(f"window.scrollTo(0, 0);")

            if views > condition_to_join_group:
                if self.check_element_on_page(mob_sl.JOIN_GROUP):
                    self.join_group(mob_sl.JOIN_GROUP)

                if self.check_element_on_page(mob_sl.GR_COMMUNITY_JOIN):
                    self.join_group(mob_sl.GR_COMMUNITY_JOIN)

                if self.check_element_on_page(mob_sl.FOLLOWS_BUTTON):
                    self.join_group(mob_sl.FOLLOWS_BUTTON)
        else:
            # return to group list or some page(start page)
            self.driver.execute_script("window.history.go(-1)")

    def scroll_group_with_condition(self, len_posts: int = random.randint(35, 50)):
        logger.info("start scroll_group_with_condition")
        condition_list = [
            "_like_condition",
            "_more_text_condition",
            "_comment_condition",
            "_like_share_condition",
        ]
        params = {
            "len_posts": len_posts,
            "after_scroll_sleep": (0.5, 0.9),
            "page_length": (750, 950),
            "second_sleep": (0.5, 2.7),
            "condition_action": f"{random.choice(condition_list)}",
        }
        self._scroll_for_groups(**params)
        logger.info("end scroll_group_with_condition")

    def scroll_wall_back(
        self, selector_page=None, len_posts: int = random.randint(25, 35)
    ):
        """
        For day session scroll random post without condition
        if page have a list post
        :param len_posts: count scroll posts
        :param selector_page: XPATH selector of page
        """
        logger.info("start scroll_wall_back")
        params = {
            "len_posts": len_posts,
            "after_scroll_sleep": (0.5, 0.9),
            "page_length": (300, 650),
            "second_sleep": (0.5, 2.5),
            "selector_page": selector_page,
        }
        self._scroll(**params)
        logger.info("end scroll_wall_back")

    def scroll_like_back(
        self, selector_page=None, len_posts: int = random.randint(35, 45)
    ):
        """ Scroll like post and back to page """
        logger.info("start scroll_like_back")

        params = {
            "len_posts": len_posts,
            "after_scroll_sleep": (0.9, 1.7),
            "page_length": (750, 2000),
            "second_sleep": (0.5, 1.3),
            "selector_page": selector_page,
            "condition_action": "_like_condition",
        }
        self._scroll(**params)
        logger.info("end scroll_like_back")

    def _like_condition(self, post: WebElement):
        try:
            like_on_post = post.find_element_by_class_name("item_like")
            liked = "item_sel" in like_on_post.get_attribute("class")
            if liked:
                self.scroll_to_element_page(post)
            else:
                like_count = self.get_post_params(like_on_post)
                if like_count > random.randint(4500, 10000):
                    # scroll to like on post
                    self.scroll_to_element_page(like_on_post)
                    like_on_post.click()
                    sleep(random.uniform(0.5, 1.5))
        except NoSuchElementException:
            pass

    def scroll_read_more_text_back(
        self, selector_page=None, len_posts: int = random.randint(20, 30)
    ):
        logger.info("start scroll_read_more_text_back")

        params = {
            "len_posts": len_posts,
            "after_scroll_sleep": (0.4, 1.1),
            "page_length": (400, 2500),
            "second_sleep": (0.5, 2.7),
            "selector_page": selector_page,
            "condition_action": "_more_text_condition",
        }
        self._scroll(**params)
        logger.info("end scroll_read_more_text_back")

    def _more_text_condition(self, post: WebElement):
        try:
            big_post = post.find_element_by_class_name("pi_text_more")
            big_post_mark = "pi_text_more" in big_post.get_attribute("class")
            if big_post_mark:
                big_post.click()
                sleep(random.uniform(3.2, 6.6))
        except NoSuchElementException:
            pass

    def scroll_comment_back(
        self, selector_page=None, len_posts: int = random.randint(15, 30)
    ):
        logger.info("start scroll_comment_back")
        params = {
            "len_posts": len_posts,
            "after_scroll_sleep": (0.7, 3.1),
            "page_length": (600, 1500),
            "second_sleep": (0.5, 2.3),
            "selector_page": selector_page,
            "condition_action": "_comment_condition",
        }
        self._scroll(**params)
        logger.info("end scroll_comment_back")

    def _comment_condition(self, post: WebElement):
        try:
            condition_to_comment = random.randint(290, 350)
            comments_on_post = post.find_element(By.CLASS_NAME, "item_replies")
            comments_count = self.get_post_params(comments_on_post)
            if comments_count > condition_to_comment:
                # scroll to comments on post
                comments_on_post.click()
                sleep(4)
                comments_users = self.driver.find_elements(
                    By.XPATH, mob_sl.WATCH_COMMENT
                )
                view_some_comments = int(len(comments_users) / 4)
                for j in range(view_some_comments):
                    scroll_comments = comments_users[j]
                    self.scroll_to_element_page(scroll_comments)
                    sleep(random.uniform(0.4, 2.3))

                # send sticker in comments
                send_sticker = self.driver.find_element(By.XPATH, mob_sl.STICKER)
                self.click_human_like(send_sticker)

                selected_random_sticker = self.driver.find_elements(
                    By.XPATH, mob_sl.SELECT_EMOJI
                )[random.randint(0, 25)]
                self.scroll_to_element_page(selected_random_sticker)
                self.click_human_like(selected_random_sticker)
                sleep(random.uniform(1.5, 2.2))

                self.driver.execute_script(f"window.scrollTo(0, 0);")
                ActionChains(self.driver).double_click(
                    self.driver.find_element_by_xpath(mob_sl.BACK_ON_PAGE)
                ).perform()

        except NoSuchElementException:
            pass

    def scroll_like_share_back(
        self, selector_page=None, len_posts: int = random.randint(15, 30)
    ):
        logger.info("start scroll_like_share_back")

        params = {
            "len_posts": len_posts,
            "after_scroll_sleep": (0.4, 1.1),
            "page_length": (400, 950),
            "second_sleep": (0.5, 1.7),
            "selector_page": selector_page,
            "condition_action": "_like_share_condition",
        }
        self._scroll(**params)
        logger.info("end scroll_like_share_back")

    def _like_share_condition(self, post: WebElement):
        try:
            condition_to_like = random.randint(4500, 15000)
            condition_to_share = random.randint(290, 450)

            like_on_post = post.find_element(By.CLASS_NAME, "item_like")
            share_on_post = post.find_element(By.CLASS_NAME, "item_share")
            liked = "item_sel" in like_on_post.get_attribute("class")
            shared = "item_sel" in share_on_post.get_attribute("class")
            if not liked:
                like_count = self.get_post_params(like_on_post)
                share_count = self.get_post_params(share_on_post)
                # condition_to_share = random.randint(250, 300)
                if like_count > condition_to_like:
                    # scroll to like on post
                    self.scroll_to_element_page(like_on_post)
                    like_on_post.click()
                    sleep(random.uniform(0.4, 3.1))
                    logger.info("like this post")

                if share_count > condition_to_share:
                    if not shared:
                        self.click_human_like(share_on_post)
                        share_on_page = self.driver.find_element(
                            By.XPATH, mob_sl.SHARE_POST_ON_USER_PAGE
                        )
                        self.click_human_like(share_on_page)
                        publish_share = self.driver.find_element(
                            By.XPATH, mob_sl.PUBLISH_SHARE
                        )
                        self.scroll_to_element_page(publish_share)
                        self.click_human_like(publish_share)
                        sleep(4)
                        self.driver.refresh()
            else:
                logger.info("post liked")
                self.scroll_to_element_page(post)
        except NoSuchElementException:
            pass

    def random_action(self, selector_page: str = None):
        self.driver.refresh()
        action_list = [
            "scroll_like_share_back",
            "scroll_comment_back",
            "scroll_read_more_text_back",
            "scroll_like_back",
            "scroll_wall_back",
        ]
        rand_attr = random.choice(action_list)
        return getattr(self, rand_attr)(selector_page)

    def search_group_in_group_list(
        self, group_name: str, default_group: int = random.randint(0, 3)
    ) -> WebElement:
        """
        search field the group check on group elements on page
        and select random group with recursion
        :return group
        """
        field_find_group = self.driver.find_element(By.XPATH, mob_sl.SEARCH_GROUP)
        self.send_keys_human_like(field_find_group, group_name)
        sleep(4)
        group_list = self.driver.find_elements(By.XPATH, mob_sl.GROUP_LIST)

        if len(group_list) > 5:
            group = self.driver.find_elements(By.XPATH, mob_sl.GROUP_LIST)[
                default_group
            ]
            self.scroll_to_element_page(group)
            return group
        else:
            self.send_keys_human_like(field_find_group, " ")
            group_list = self.driver.find_elements(By.XPATH, mob_sl.GROUP_LIST)
            if len(group_list) > 5:
                group = self.driver.find_elements(By.XPATH, mob_sl.GROUP_LIST)[
                    default_group
                ]
                self.scroll_to_element_page(group)
                return group
            else:
                field_find_group.clear()
                return self.search_group_in_group_list(group_name)

    def get_list_group(self, search_group: str = GenerateUser().create_group()):
        """ Condition for user groups """
        sleep(2)
        len_search_group = len(search_group.split(" "))

        if len_search_group > 3:
            typing_group = str(
                search_group.split(" ")[0] + " " + search_group.split(" ")[1]
            )
        elif len_search_group == 2:
            typing_group = str(search_group.split(" ")[0])
        elif len_search_group == 1:
            typing_group = search_group
        else:
            typing_group = search_group[0]

        logger.info("search group start")
        groups_page = self.driver.find_element(By.XPATH, mob_sl.GROUPS_PAGE)
        self.click_human_like(groups_page)

        if self.check_element_on_page(mob_sl.USER_GROUP_EMPTY):
            group = self.search_group_in_group_list(typing_group)
            self.click_human_like(group)
            self.scroll_group_with_condition()
        else:
            # count group to join
            group = self.search_group_in_group_list(typing_group)
            self.click_human_like(group)
            self.scroll_group_with_condition()

    def join_group(self, selector):
        """ JOIN group, community, follows page and return to main page """
        sleep(random.randint(1, 3))
        join = self.driver.find_element(By.XPATH, selector)
        self.scroll_to_element_page(join)
        join.click()
        sleep(random.randint(1, 5))

    def morning_session(self):
        deadline = time.monotonic() + random.randint(150, 250)
        while time.monotonic() < deadline:
            self.random_action()
            time.sleep(random.randint(3, 10))
            self.random_action(mob_sl.RECOMMENDATIONS_PAGE)
            time.sleep(random.randint(7, 13))

        self.save_session()
        self.driver.close()

    def day_session(self):
        deadline = time.monotonic() + random.randint(500, 600)
        while time.monotonic() < deadline:
            time.sleep(random.randint(1, 2))
            self.get_list_group()
            time.sleep(random.randint(4, 5))
            self.random_action(mob_sl.NEWS_PAGE)
            time.sleep(random.randint(1, 2))
            self.get_list_group()
            time.sleep(random.randint(3, 7))
            self.random_action(mob_sl.NEWS_PAGE)

        self.save_session()
        self.driver.close()

    def night_session(self):
        deadline = time.monotonic() + random.randint(500, 600)
        while time.monotonic() < deadline:
            time.sleep(random.randint(2, 4))
            self.get_list_group()
            time.sleep(random.randint(4, 8))
            self.random_action(mob_sl.RECOMMENDATIONS_PAGE)
            time.sleep(random.randint(5, 10))
            self.random_action()
            time.sleep(random.randint(10, 12))
            self.random_action(mob_sl.NEWS_PAGE)

        self.save_session()
        self.driver.close()

    def light_session(self):
        # todo: not scroll page up for this session create this scroll
        # scroll news page with condition
        self.random_action()

        self.save_session()
        self.driver.close()

    def random_session(self):
        session_list = [
            "morning_session",
            "day_session",
            "night_session",
            "light_session",
        ]
        rand_attr = random.choice(session_list)
        return getattr(self, rand_attr)(session_list)
