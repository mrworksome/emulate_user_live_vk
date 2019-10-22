from emulate_user_live.desktop_pages import selector_desktop_pages as sl

# MAIN PAGE FIELD
main_first_name = {
    "element_selector": sl.MAIN_FIRST_NAME,
    "data_element": "main_first_name",
}
main_last_name = {
    "element_selector": sl.MAIN_LAST_NAME,
    "data_element": "main_last_name",
}

main_gender = {
    "element_selector": sl.MAIN_GENDER,
    "data_element": "main_gender",
    "action": "click",
    "container_selector_element": True,
    "num_container": 0,
}

main_family_status = {
    "element_selector": sl.MAIN_FAMILY_STATUS,
    "data_element": "main_family_status",
    "action": "click",
    "container_selector_element": True,
    "num_container": 1,
}

main_day_of_bday = {
    "element_selector": sl.MAIN_DAY_BDAY,
    "data_element": "main_day_of_bday",
    "action": "click",
    "container_selector_element": True,
    "num_container": 3,
}

main_month_of_bday = {
    "element_selector": sl.MAIN_MONTH_BDAY,
    "data_element": "main_month_of_bday",
    "action": "click",
    "container_selector_element": True,
    "num_container": 4,
}
main_year_of_bday = {
    "element_selector": sl.MAIN_YEAR_BDAY,
    "data_element": "main_year_of_bday",
    "action": "click",
    "container_selector_element": True,
    "num_container": 5,
}

main_visible_bday = {
    "element_selector": sl.MAIN_VISIBLE_BDAY,
    "data_element": "main_visible_bday",
    "action": "click",
    "container_selector_element": True,
    "num_container": 6,
}
main_home_town = {
    "element_selector": sl.MAIN_HOMETOWN,
    "data_element": "main_home_town",
}

# dont no how do this
main_language = {
    "element_selector": sl.SELECTOR_INPUT,
    "data_element": "main_language",
    "action": "send_keys",
    "container_selector_element": True,
    "num_container": 7,
}

main_fields = [
    main_first_name,
    main_last_name,
    main_gender,
    main_family_status,
    main_day_of_bday,
    main_month_of_bday,
    main_year_of_bday,
    main_visible_bday,
    main_home_town,
    # main_language
]

# CONTACT PAGE FIELDS
contact_country = {
    "element_selector": sl.CONTACT_COUNTRY,
    "data_element": "contact_country",
    "action": "click",
    "container_selector_element": True,
    "num_container": 0,
}
contact_town = {
    "element_selector": sl.CONTACT_TOWN,
    "data_element": "contact_town",
    "action": "click",
    "container_selector_element": True,
    "num_container": 1,
}
contact_skype = {"element_selector": sl.CONTACT_SKYPE, "data_element": "contact_skype"}
contact_website = {
    "element_selector": sl.CONTACT_WEBSITE,
    "data_element": "contact_website",
}
# add element for nex activation or registration element
contact_instagram = {
    "element_selector": sl.CONTACT_EXPORT_INSTA,
    "data_element": "contact_instagram",
}
# add element for nex activation or registration element
contact_twitter = {
    "element_selector": sl.CONTACT_EXPORT_TWITTER,
    "data_element": "contact_twitter",
}

contact_fields = [contact_country, contact_town]

# INTERESTS PAGE FIELDS
interests_activities = {
    "element_selector": sl.INTERESTS_ACTIVITIES,
    "data_element": "interests_activities",
}
interests_interests = {
    "element_selector": sl.INTERESTS_INTERESTS,
    "data_element": "interests_interests",
}
interests_music = {
    "element_selector": sl.INTERESTS_MUSIC,
    "data_element": "interests_music",
}
interests_movies = {
    "element_selector": sl.INTERESTS_MOVIES,
    "data_element": "interests_movies",
}
interests_tv_show = {
    "element_selector": sl.INTERESTS_SHOW,
    "data_element": "interests_tv_show",
}
interests_books = {
    "element_selector": sl.INTERESTS_BOOKS,
    "data_element": "interests_books",
}
interests_games = {
    "element_selector": sl.INTERESTS_GAMES,
    "data_element": "interests_games",
}
interests_quotes = {
    "element_selector": sl.INTERESTS_QUOTES,
    "data_element": "interests_quotes",
}
interests_about_user = {
    "element_selector": sl.INTERESTS_ABOUT_USER,
    "data_element": "interests_about_user",
}

interests_fields = [
    interests_activities,
    interests_interests,
    interests_music,
    interests_movies,
    interests_tv_show,
    interests_books,
    interests_games,
    interests_quotes,
    interests_about_user,
]

# High education page fields
university_country = {
    "element_selector": sl.UNIVERSITY_COUNTRY,
    "data_element": "university_country",
    "action": "click",
    "container_selector_element": True,
    "num_container": 0,
}
university_town = {
    "element_selector": sl.UNIVERSITY_TOWN,
    "data_element": "university_town",
    "action": "click",
    "container_selector_element": True,
    "num_container": 1,
}
university_name = {
    "element_selector": sl.UNIVERSITY_NAME,
    "data_element": "university_name",
    "action": "click",
    "container_selector_element": True,
    "num_container": 2,
}
university_form_study = {
    "element_selector": sl.UNIVERSITY_FORM,
    "data_element": "university_form_study",
    "action": "click",
    "container_selector_element": True,
    "num_container": 5,
}
university_status = {
    "element_selector": sl.UNIVERSITY_STATUS,
    "data_element": "university_status",
    "action": "click",
    "container_selector_element": True,
    "num_container": 6,
}

university_fields = [
    university_country,
    university_town,
    university_name,
    university_form_study,
    university_status,
]

# career page fields
career_company_name = {
    "element_selector": sl.CAREER_COMPANY_NAME,
    "data_element": "career_company_name",
    "action": "send_keys",
    "container_selector_element": True,
    "num_container": 0,
}
career_company_country = {
    "element_selector": sl.CAREER_COUNTRY,
    "data_element": "career_company_country",
    "action": "click",
    "container_selector_element": True,
    "num_container": 1,
}
career_company_town = {
    "element_selector": sl.CAREER_CITY,
    "data_element": "career_company_town",
    "action": "click",
    "container_selector_element": True,
    "num_container": 2,
}
career_start_working = {
    "element_selector": sl.CAREER_START,
    "data_element": "career_start_working",
    "action": "click",
    "container_selector_element": True,
    "num_container": 3,
}
# career_graduation = {
#     'element_selector': sl.CAREER_GRADUATE,
#     'data_element': 'career_graduation',
#     'action': 'click',
#     'container_selector_element': sl.CONTAINERS,
#     'num_container': 4
# }
career_position = {
    "element_selector": sl.CAREER_POSITION,
    "data_element": "career_position",
    "action": "send_keys",
    "container_selector_element": True,
    "num_container": 5,
}

career_fields = [
    career_company_name,
    career_company_country,
    career_company_town,
    career_start_working,
    career_position,
]

# life position page fields

position_politics = {
    "element_selector": sl.POLITIC,
    "data_element": "position_politics",
    "action": "click",
    "container_selector_element": True,
    "num_container": 0,
}
position_worldview = {
    "element_selector": sl.RELIGION,
    "data_element": "position_worldview",
    "action": "click",
    "container_selector_element": True,
    "num_container": 1,
}
position_thing_life = {
    "element_selector": sl.THING_LIFE,
    "data_element": "position_thing_life",
    "action": "click",
    "container_selector_element": True,
    "num_container": 2,
}
position_thing_people = {
    "element_selector": sl.THING_PEOPLE,
    "data_element": "position_thing_people",
    "action": "click",
    "container_selector_element": True,
    "num_container": 3,
}
position_smoking = {
    "element_selector": sl.SMOKING,
    "data_element": "position_smoking",
    "action": "click",
    "container_selector_element": True,
    "num_container": 4,
}
position_alcohol = {
    "element_selector": sl.ALCOHOL,
    "data_element": "position_alcohol",
    "action": "click",
    "container_selector_element": True,
    "num_container": 5,
}
position_inspire = {"element_selector": sl.INSPIRE, "data_element": "position_inspire"}

life_position_fields = [
    position_politics,
    position_worldview,
    position_thing_life,
    position_thing_people,
    position_alcohol,
    position_smoking,
    position_inspire,
]
