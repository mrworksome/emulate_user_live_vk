import datetime
import os
import random
from typing import Dict

import yaml
from faker import Faker
from loguru import logger


class GenerateUser(object):
    """ Create Identity User by yaml file"""

    def __init__(self):
        file_path = os.path.join(
            os.path.dirname(__file__), "desktop_pages/user_data_identity.yaml"
        )

        with open(file_path, "r") as f:
            try:
                self.data = yaml.safe_load(f)
            except yaml.YAMLError as exc:
                logger.info(exc)

    def create_data(self) -> Dict:
        fake = Faker("ru_RU")
        now = datetime.datetime.now()

        # user agent
        user_agent = random.choice(self.data.get("user_agent"))

        # main page
        visible_bday = random.choice(self.data.get("main").get("visible_birthday"))
        year_of_bday = random.randrange(1983, 2005)
        family_status = random.choice(self.data.get("main").get("family_status"))
        home_town = random.choice(self.data.get("main").get("hometown"))

        # contact page
        country = self.data.get("contact").get("country")
        town = random.choice(self.data.get("contact").get("town"))

        # career
        start_working = int(now.year) - 1

        # middle school education
        # school_name = random.choice(
        # data.get("education").get("school_name"))

        # high university education
        form_education = random.choice(
            self.data.get("education").get("university").get("form_education")
        )
        university_status = random.choice(
            self.data.get("education").get("university").get("status")
        )
        if town == "Москва":
            university = random.choice(
                self.data.get("education").get("university").get("moscow")
            )
        else:
            university = random.choice(
                self.data.get("education").get("university").get("spb")
            )

        quotes = random.sample(
            list(self.data.get("interests").get("quotes")), random.randint(1, 2)
        )
        about_user = random.choice(self.data.get("interests").get("about_user"))
        interests = random.choice(self.data.get("interests").get("interests"))

        # Life position
        politics = random.choice(self.data.get("life_position").get("politics"))
        worldview = random.choice(self.data.get("life_position").get("worldview"))
        thing_life = random.choice(self.data.get("life_position").get("thing_life"))
        thing_people = random.choice(self.data.get("life_position").get("thing_people"))

        inspire = random.choice(self.data.get("life_position").get("inspire"))

        user_fake_data = {
            # credential
            "--user-agent": user_agent,
            "proxy": "",
            "login": "",
            "password": "",
            # main page
            "main_first_name": "",
            "main_last_name": "",
            "main_gender": "",
            "main_family_status": family_status,
            "main_day_of_bday": random.randint(1, 28),
            "main_month_of_bday": random.choice(
                self.data.get("main").get("month_of_bday")
            ),
            "main_year_of_bday": year_of_bday,
            "main_visible_bday": visible_bday,
            "main_home_town": home_town,
            # contact
            "contact_country": country,
            "contact_town": town,
            # 'contact_skype': '',
            # 'contact_website': '',
            # 'contact_instagram': '',
            # 'contact_twitter': '',
            # middle school
            # 'education_country': f'{country}',
            # 'education_town': f'{town}',
            # 'education_school_name': f'{school_name}',
            # 'education_school_date_start': '',
            # 'education_school_date_end': '',
            # 'education_school_end': '',
            # 'education_school_class': '',
            # 'education_school_specialization': '',
            # interests
            # 'interests_activities': '',
            "interests_interests": interests,
            # 'interests_music': '',
            # 'interests_movies': '',
            # 'interests_tv_show': '',
            # 'interests_books': '',
            # 'interests_games': '',
            "interests_quotes": ", ".join(quotes),
            "interests_about_user": about_user,
            # high university
            "university_country": country,
            "university_town": town,
            "university_name": university,
            # 'university_faculty': '',
            # 'university_direction': '',
            "university_form_study": form_education,
            "university_status": university_status,
            # 'university_date_end': '',
            # Career
            "career_company_name": fake.company(),
            "career_company_country": country,
            "career_company_town": town,
            "career_start_working": start_working,
            # 'career_graduation': '',
            "career_position": fake.job(),
            # Life position
            "position_politics": politics,
            "position_worldview": worldview,
            "position_thing_life": thing_life,
            "position_thing_people": thing_people,
            "position_smoking": random.choice(
                self.data.get("life_position").get("smoking_and_alcohol")
            ),
            "position_alcohol": random.choice(
                self.data.get("life_position").get("smoking_and_alcohol")
            ),
            "position_inspire": inspire,
        }

        return user_fake_data

    def create_group(self) -> str:
        top_groups = self.data.get("top_group_vk").get("group_name")

        return random.choice(top_groups)

    def create_interests(self, data: Dict, gender: str):
        """ Update elements in user data """
        # interests page
        if gender == "мужской":
            # first_name = fake.first_name_male()
            # last_name = fake.last_name_male()
            activities = random.choice(
                self.data.get("interests").get("male").get("activities")
            )
            movies = random.sample(
                list(self.data.get("interests").get("male").get("films")),
                random.randint(4, 5),
            )
            tv_show = random.sample(
                list(self.data.get("interests").get("male").get("tv_show")),
                random.randint(2, 3),
            )
            music = random.sample(
                list(self.data.get("interests").get("male").get("music")),
                random.randint(4, 6),
            )
            books = random.sample(
                list(self.data.get("interests").get("male").get("books")),
                random.randint(2, 3),
            )
            games = random.sample(
                list(self.data.get("interests").get("male").get("games")),
                random.randint(2, 7),
            )
        else:
            # first_name = fake.first_name_female()
            # last_name = fake.last_name_female()
            activities = random.choice(
                self.data.get("interests").get("female").get("activities")
            )
            movies = random.sample(
                list(self.data.get("interests").get("female").get("films")),
                random.randint(3, 5),
            )
            tv_show = random.sample(
                list(self.data.get("interests").get("female").get("tv_show")),
                random.randint(5, 7),
            )
            music = random.sample(
                list(self.data.get("interests").get("female").get("music")),
                random.randint(3, 5),
            )
            books = random.sample(
                list(self.data.get("interests").get("female").get("books")),
                random.randint(4, 5),
            )
            games = random.sample(
                list(self.data.get("interests").get("female").get("games")),
                random.randint(3, 5),
            )

        new_value = {
            # interests
            "interests_activities": activities,
            "interests_music": ", ".join(music),
            "interests_movies": ", ".join(movies),
            "interests_tv_show": ", ".join(tv_show),
            "interests_books": ", ".join(books),
            "interests_games": ", ".join(games),
        }

        data.update(new_value)
        return data
