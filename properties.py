POSITIONS = {
    "0": (10, 10), "1": (250, 10), "2": (500, 10), "3": (750, 10), "4": (1000, 10),
    "5": (10, 350), "6": (250, 350), "7": (500, 350), "8": (750, 350), "9": (1000, 350)

}
POSITIONS_WIN = {
    "0": (10, 10), "1": (400, 10), "2": (800, 10),
    "3": (10, 350), "4": (400, 350), "5": (800, 350)
}
DRIVER_PATH = "chromedriver.exe"
SIZE = (400, 800)
SIZE_WIN = (500, 700)
BATCH = 5
THREADS = 1
URL = "https://aviso.bz"
URL_CHROME_EXTENSION = "chrome-extension://omghfjlpggmjjaagoclmmobgdodcjboh/popup/popup.html"
ACCOUNTS_FILE_PATH = "accounts_info.xlsx"
LIST_RANDOM_URL = ["https://www.google.com/", "https://bing.com", "https://github.com/", "https://www.youtube.com/"]

# config mapping fields
ID_NO = 0
IP_MACHINE = 1
MACHINE_ID = 2
USER_AVISO = 3
PASSWORD_AVISO = 4
USER_MAIL = 5
PASSWORD_MAIL = 6
RECOVER_MAIL = 7
NUMBER_PHONE = 8
ID_PAYEER = 9
PASSWORD_PAYEER = 10
YOUTUBE = 11
USER_AGENT = 12
COOKIES = 13
UPDATE_COOKIES = 14
START_COIN = 15
END_COIN = 16
TOTAL_COIN_PER_DAY = 17
START_TIME = 18
END_TIME = 19
COUNT_LOGIN = 20

# Query tab_vpn
QUERY_CLICK_ON_OFF = "document.querySelector('page-switch').shadowRoot.querySelector('main-index').\
    shadowRoot.querySelector('c-switch').shadowRoot.querySelector('.Circle').click()"
QUERY_STATUS = "return document.querySelector('page-switch').shadowRoot.querySelector('main-index').shadowRoot.\
    querySelector('c-switch').className"
QUERY_CHANGE_LOCATE = "document.querySelector('page-switch').shadowRoot.querySelector('main-index').\
    shadowRoot.querySelector('index-home').shadowRoot.querySelector('.Active').\
        querySelector('.ChangeButton').click()"
QUERY_SELECT_NETHERLANDS = "document.querySelector('page-switch').shadowRoot.querySelector('main-index').\
    shadowRoot.querySelector('index-locations').shadowRoot.querySelectorAll('index-locations-element')[0].\
        shadowRoot.querySelector('.Country').click()"
QUERY_SELECT_SINGAPORE = "document.querySelector('page-switch').shadowRoot.querySelector('main-index').\
    shadowRoot.querySelector('index-locations').shadowRoot.querySelectorAll('index-locations-element')[1].\
        shadowRoot.querySelector('.Country').click()"
QUERY_SELECT_US = "document.querySelector('page-switch').shadowRoot.querySelector('main-index').\
    shadowRoot.querySelector('index-locations').shadowRoot.querySelectorAll('index-locations-element')[2].\
        shadowRoot.querySelector('.Country').click()"
QUERY_SELECT_UK = "document.querySelector('page-switch').shadowRoot.querySelector('main-index').\
    shadowRoot.querySelector('index-locations').shadowRoot.querySelectorAll('index-locations-element')[3].\
        shadowRoot.querySelector('.Country').click()"
LIST_QUERY_SELECT_LOCATE = [QUERY_SELECT_NETHERLANDS, QUERY_SELECT_SINGAPORE,
                            QUERY_SELECT_US, QUERY_SELECT_UK]