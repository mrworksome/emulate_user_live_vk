# user profile
USER_PROFILE = '//div[@class="ip_user_link"]'

# news
NEWS_PAGE = '//a[@data-header="Новости"]'

# Liked
LIKED_POST = '//a[@data-header="Понравилось"]'

# recommendations
RECOMMENDATIONS_PAGE = '//a[@href="/feed?section=recommended"]'

# notifications
NOTIFICATIONS_PAGE = '//a[@href="/feed?section=notifications"]'

# messages
MESSAGES_PAGE = '//a[@href="/mail"]'

# friends
FRIENDS_PAGE = '//a[@href="/friends"]'
FRIENDS_LIST = '//div[@class="Friends__item Friends__item_request"]'
ADD_FRIEND = '//div[text()="Добавить"]//parent::a[@role="button"]'
SEND_COMMENT = '//textarea[@id="reply_field_text"]'

# send text in wall group
NEW_POST_IN_GROUP = '//a[@class="new_post_link" and @role="button"]'
SEND_CALL_TO_ACTION = '//textarea[@name="message"]'
PUBLISH = '//button[@type="submit"]'


# groups
GROUPS_PAGE = '//a[@href="/groups"]'
USER_GROUP_EMPTY = '//div[text()="Вы пока не состоите ни в одном сообществе."]'
USER_GROUP_COUNT = '//a[@class="Groups__item simple_fit_item"]'
GROUP_VERIFIED = '//b[@class="verified"]'
GROUP_LIST = '//a[contains(@class,"Groups__item")]'

# after comment scroll select user go to user profile ACTION DRIVER BACK
CLOSED_USER_PROFILE = '//div[@class="ClosedProfileWall__title"]'

# all selector tlo join group, page and community
GR_COMMUNITY_JOIN = (
    '//div[contains(@class, "Icon_community_join")]//parent::a[@role="button"]'
)
JOIN_GROUP = '//div[text()="Вступить в группу"]//parent::a[@role="button"]'
FOLLOWS_BUTTON = '//div[text()="Подписаться"]//parent::a[@role="button"]'


BACK_ON_PAGE = '//a[@title="Назад"]'

# selector for articles
GROUP_ARTICLES = '//a[text()="Статьи " and @class="pm_item"]'  # click
ARTICLES_LIST = '//div[contains(@class, "author-page-article")]'  # select by [number]
ARTICLES_CLOSE = (
    '//a[@class="articleView__close al_back_history al_force_back"]'
)  # scroll pages
ARTICLES_FOOTER_SHARE = '//div[@class="articleView__footer"]//div[@class="articleView__footer_btn_icon"]//parent::a[contains(@class, "articleView__footer_btn_share")]'  # todo: click -> next action
ARTICLE_BOOKMARK = '//div[contains(@class, "ActionsPanel-button--bookmark")]'  # click
ARTICLE_SHARE = (
    '//div[contains(@class, "ActionsPanel-button--own")]'
)  # click -> next action
ARTICLE_PUBLISH_ON_WALL = '//button[@type="submit"]'  # if send return to main page


MORE_ABOUT_GROUP = '//a[text()="Ещё..." and @class="pm_item"]'  # click -> next action
GROUP_AUDIO = '//a[text()="Аудиозаписи " and @class="pm_item"]'  # click
AUDIO_PLAYLIST = '//div[text()="Плейлисты"]'  # if we have else -> next action
PLAYLIST_ALL = (
    '//div[@class="audioPlaylists__header"]//a[text()="Показать все"]'
)  # click -> next action (scroll and select)
PLAYLIST_SELECT = (
    '//a[contains(@class, "audioPlaylistsPage__itemLink")]'
)  #  select by [number] action click
LISTENING_PLAYLIST = '//a[text()="Слушать"]'  # action click
ADD_FOR_USER = '//a[text()="Добавить"]'  # action click
ELSE_ADDED = '//a[text()="Добавлен"]'  # conditions for playlist

AUDIO_PREFERENCES = '//div[@class="ai_dur"]'  # click on duration have title "-6:56"
AUDIO_LIST = (
    '//div[contains(@class," ai_has_btn audio_item")]'
)  # action (scroll and click) to play
#  by (ai_current- is played) start timer music played

AUDIO_MENU = '//div[@class=" ai_has_btn audio_item"]//a[contains(@class, "ai_menu_toggle_button")]'  # action click -> next action
AUDIO_ADD = (
    '//div[@class="ai_menu wi_actions"]//div[@class="ai_add wia_item"]'
)  # try to select element is visible
AUDIO_DEL = (
    '//div[@class="ai_add wia_item" and text()="Удалить аудиозапись"]'
)  # conditions for music

GROUP_VIDEO = '//a[text()="Видео " and @class="pm_item"]'  # action (click) to play by
VIDEO_LIST = (
    '//div[contains(@class,"video_item")]'
)  # search by elements select by [number] click -> next action
VIDEO_PLAY = '//video[@class="vv_inline_video"]'


SEARCH_GROUP = '//input[@id="gr_search_field"]'  # send_keys for search group field
TYPING_MSG_ON_WALL = '//span[text()="Написать сообщение"]'  # todo: send_keys and click
CLICK_TO_SEND_MSG = ""

# post dynamic selectors
VIEW_POST = (
    '//div[contains(@class, "wall_item")//a[@class="pi_text_more"]'
)  # click to read more in post text
GROUP_POST_LIST = '//div[contains(@class, "wall_item")]'  # all post on page
CAPITALIZE_POST = '//a[text()="Рекламная запись"]'  # in wall recommendation
MARK_ADS = (
    '//div[contains(@class, "pi_signed ads_mark")]'
)  # advertise mark post condition
POST_MORE_TEXT = '//a[contains[text(), "Показать полностью…")]'


# post static selector
POST_LIKE = (
    '//a[contains(@class, "item_like")]'
)  # get_attribute('aria-label') count like
POST_COMMENT = (
    '//a[contains(@class, "item_replies")]'
)  # get_attribute('aria-label') count comment
POST_SHARE = (
    '//a[contains(@class, "item_share _i")]'
)  # get_attribute('aria-label') count share
COMMENT_POST = (
    '//textarea[@id="reply_field_text"]'
)  # action send_keys in comment as text
WATCH_COMMENT = (
    '//div[contains(@class, "ReplyItem Post__rowPadding")]'
)  # for scroll comment
STICKER = '//input[@name="add_sticker"]'  # select sticker in user comment
EMOJI = '//a[contains(@class, "sp_tab")]'  # for selected sticker pack
SELECT_EMOJI = (
    '//div[contains(@class, "sticker_item")]'
)  # find_elements with random by num #
SHARE_POST_ON_USER_PAGE = '//div[text()="На своей странице"]'
PUBLISH_SHARE = '//button[@type="submit"]'


COMMENT_COUNT = '//b[@class="v_replies"]'  # get title and int

# photo
PHOTO_PAGE = '//a[@href="/feed?section=photos"]'

# upload photo
UPLOAD_PHOTO = '//a[@class="pm_item profile_photo_upload_wrap"]'

# videos
VIDEOS_PAGE = '//a[@href="/video"]'

# audio
AUDIO_PAGE = '//a[@href="/audio"]'
