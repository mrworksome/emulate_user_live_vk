# registration
EMAIL = '//input[@type="email"]'
PASSWORD = '//input[@type="password"]'

# desktop or mobile version
DESKTOP_VERSION = '//a[starts-with(@href, "/fv?to=")]'
MOBILE_VERSION = '//a[@href="http://m.vk.com/"]'

# DESKTOP
MY_PAGE = '//span[text()="Моя страница"]'

# containers
CONTAINERS = '//div[starts-with(@id, "container")]'
LIST_VALUE = '//div[@class="result_list"]//li'
ACTIVE = '//li[@class="active"]'
SELECTOR_INPUT = '//input[@type="text"]'
HIDDEN_INPUT = '//input[@class="customField"]'
SAVE = '//button[text()="Сохранить"]'

# go to edit main page
EDIT_PROFILE_PAGE = '//a[@id="profile_edit_act"]'
# main page
MAIN_FIRST_NAME = '//input[@id="pedit_first_name"]'
MAIN_LAST_NAME = '//input[@id="pedit_last_name"]'
MAIN_GENDER = '//input[@id="pedit_sex"]'
MAIN_FAMILY_STATUS = '//input[@id="pedit_status"]'
MAIN_DAY_BDAY = '//input[@id="pedit_bday"]'
MAIN_MONTH_BDAY = '//input[@id="pedit_bmonth"]'
MAIN_YEAR_BDAY = '//input[@id="pedit_byear"]'
MAIN_VISIBLE_BDAY = '//input[@id="pedit_bday_visibility"]'
MAIN_HOMETOWN = '//input[@id="pedit_home_town"]'
CHOICE = '//li[@onmousedown="Select.itemMouseDown(14, 0, this)"]'


# contact page
CONTACT_PAGE = '//a[@id="ui_rmenu_contacts"]'
# contact page fields
CONTACT_COUNTRY = '//input[@id="pedit_country"]'
CONTACT_TOWN = '//input[@id="pedit_city"]'
CONTACT_SKYPE = '//input[@id="pedit_skype"]'
CONTACT_WEBSITE = '//input[@id="pedit_website"]'
CONTACT_EXPORT_INSTA = '//div[@id="export_service_4"]'
CONTACT_EXPORT_TWITTER = '//div[@id="export_service_1"]'

# interests page
INTERESTS_PAGE = '//a[@href="/edit?act=interests"]'
# interests fields
INTERESTS_ACTIVITIES = '//textarea[@id="pedit_interests_activities"]'
INTERESTS_INTERESTS = '//textarea[@id="pedit_interests_interests"]'
INTERESTS_MUSIC = '//textarea[@id="pedit_interests_music"]'
INTERESTS_MOVIES = '//textarea[@id="pedit_interests_movies"]'
INTERESTS_SHOW = '//textarea[@id="pedit_interests_tv"]'
INTERESTS_BOOKS = '//textarea[@id="pedit_interests_books"]'
INTERESTS_GAMES = '//textarea[@id="pedit_interests_games"]'
INTERESTS_QUOTES = '//textarea[@id="pedit_interests_quotes"]'
INTERESTS_ABOUT_USER = '//textarea[@id="pedit_interests_about"]'

# education page
EDUCATION_PAGE = '//a[@id="ui_rmenu_education"]'
# education School fields
SCHOOL_COUNTRY = '//input[@id="s_country-1"]'
SCHOOL_TOWN = '//input[@id="s_city-1"]'
SPECIALIZATION = '//input[@id="s_spec-1_custom"]'

# high education page
HIGH_EDUCATION = '//a[@href="/edit?act=higher_education"]'
# high education fields
UNIVERSITY_COUNTRY = "//input[starts-with(@id, u_country)]"
UNIVERSITY_TOWN = '//input[starts-with(@id, "u_city")]'
UNIVERSITY_NAME = '//input[starts-with(@id, "u_university")]'
UNIVERSITY_FORM = '//input[starts-with(@id, "u_edu_form")]'
UNIVERSITY_STATUS = '//input[starts-with(@id, "u_edu_status")]'
UNIVERSITY_GRADUATION = '//input[starts-with(@id, "u_graduation")]'

# career page
CAREER_PAGE = '//a[@href="/edit?act=career"]'
# career fields
CAREER_COMPANY_NAME = '//input[@id="group1"]'
CAREER_COUNTRY = '//input[@id="country1"]'
CAREER_CITY = '//input[@id="city1"]'
CAREER_START = '//input[@id="start1"]'
CAREER_GRADUATE = '//input[@id="finish1_custom"]'
CAREER_POSITION = '//input[@id="position1"]'

# life position page
LIFE_POSITION_PAGE = '//a[@href="/edit?act=personal"]'
# live position fields
POLITIC = '//input[@id="pedit_political"]'
RELIGION = '//input[@id="pedit_religion"]'
THING_LIFE = '//input[@id="pedit_life"]'
THING_PEOPLE = '//input[@id="pedit_people"]'
SMOKING = '//input[@id="pedit_smoking"]'
ALCOHOL = '//input[@id="pedit_alcohol"]'
INSPIRE = '//input[@id="pedit_inspired_by"]'
