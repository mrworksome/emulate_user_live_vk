import os
import random
import sys
from time import strftime, sleep

import schedule

from emulate_user_live.desktop_pages.autofilling_account import AutoFillAccount
from emulate_user_live.mobile_pages.all_user_action import UserCases


class EmulateUserLive(AutoFillAccount, UserCases):
    def start(self):
        if self.conn.hget(self.login, "session"):
            self.schedule_account_actions_day()
        else:
            self.filling_user_data()
            self.light_session()
            self.schedule_account_actions_day()

    def schedule_account_actions_day(self):

        time_morning_session = strftime(
            f"0{random.randint(6, 9)}:{random.randint(10, 59)}:{random.randint(10, 59)}"
        )
        time_day_session = strftime(
            f"{random.randint(10, 16)}:{random.randint(10, 59)}:{random.randint(10, 59)}"
        )
        time_night_session = strftime(
            f"{random.randint(17, 20)}:{random.randint(10, 59)}:{random.randint(10, 59)}"
        )
        time_light_session = strftime(
            f"{random.randint(21, 23)}:{random.randint(10, 59)}:{random.randint(10, 59)}"
        )

        schedule.every().day.at(time_morning_session).do(self.morning_session).tag(
            "morning_session"
        )

        schedule.every().day.at(time_day_session).do(self.day_session).tag(
            "day_session"
        )

        schedule.every().day.at(time_night_session).do(self.night_session).tag(
            "night_session"
        )

        schedule.every().day.at(time_light_session).do(self.light_session).tag(
            "light_session"
        )

        # todo: rework after join in grpc
        while True:
            schedule.run_pending()
            sys.stdout.flush()
            sleep(60)

    # def create_scheduler(self, action: function, hours: int=Tuple[Number, Number]):
    #     time = strftime(f"{hours}:{random.randint(10, 59)}:{random.randint(10, 59)}")
    #     if datetime.datetime.now().time() == datetime.time(hours, random.randint(10, 59), random.randint(10, 59)):
    #         # time_schedule = strftime(f'{hours}:{minutes}')
    #         schedule.every().day.at(time).do(action)
    #         while True:
    #             schedule.run_pending()
    #             sys.stdout.flush()
    #     else:
    #         pass


if __name__ == "__main__":
    vk_login_1 = os.environ.get("LOGIN")
    vk_password_1 = os.environ.get("PASS")
    a = EmulateUserLive(vk_login_1, vk_password_1)
    a.start()
