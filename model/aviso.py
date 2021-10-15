from seleniumwire.webdriver import ChromeOptions, Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from properties import QUERY_SELECT_NETHERLANDS, QUERY_SELECT_SINGAPORE, QUERY_SELECT_UK, QUERY_SELECT_US
from properties import DRIVER_PATH, URL, URL_CHROME_EXTENSION, LIST_RANDOM_URL, QUERY_CLICK_ON_OFF
from properties import QUERY_STATUS, QUERY_CHANGE_LOCATE, QUERY_CHANGE_LOCATE
# from add_cookies import add_cookie
import time
import json
import random
import properties
import requests
import html
from bs4 import BeautifulSoup


class Aviso:

    def __init__(self, account, position=(10, 10), size=properties.SIZE_WIN, batch=properties.BATCH):
        self.account = account
        self.batch = batch
        self.pre_twiron = None
        self.home_youtube_tab = None
        self.list_query_select_locate = [QUERY_SELECT_NETHERLANDS, QUERY_SELECT_SINGAPORE,
                                         QUERY_SELECT_UK, QUERY_SELECT_US]
        self.now = time.strftime("%H:%M-%d/%m")
        if self.account.get_start_time() is None or self.account.get_start_time().split("-")[1] !=\
                self.now.split("-")[1]:
            self.account.set_start_time(self.now)

        # add option to driver
        options = ChromeOptions()
        options.add_argument('--disable-infobars')
        options.add_argument("--log-level=3")
        options.add_extension("browsec_vpn.crx")
        options.add_argument("--user-agent=%s" % self.account.get_agent())

        self.driver = Chrome(executable_path=DRIVER_PATH, chrome_options=options)
        self.driver.implicitly_wait(20)
        self.driver.minimize_window()
        #             set position
        self.driver.set_window_size(size[0], size[1])
        self.driver.set_window_position(position[0], position[1])
        # Go vpn
        self.driver.get(URL_CHROME_EXTENSION)
        self.tab_vpn = self.driver.current_window_handle
        # get url for driver
        self.driver.execute_script('''window.open("%s","_blank");''' % URL)
        self.driver.implicitly_wait(20)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        try:
            self.load_cookie()
            self.go_to_youtube()
        except:
            raise ValueError("Login and initialize failed!")

    def load_cookie(self):
        if self.account.get_cookies() is not None:
            cookies = json.loads(self.account.get_cookies())
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            time.sleep(random.randint(1, 3))
            self.driver.get(URL)
            time.sleep(random.randint(1, 3))

            try:
                money = self.driver.find_element_by_id("new-money-ballans").text
                if self.account.get_start_coins() is None or self.account.get_start_time().split("-")[1] !=\
                        self.now.split("-")[1]:
                    self.account.set_start_coins(float(money.split(" ")[0]))
            #         handle with start date
            except:
                self.login()
        else:
            self.login()

    def login(self):
        #         write info about account
        random_url = LIST_RANDOM_URL[random.randint(0, 3)]
        self.driver.get(random_url)
        time.sleep(random.randint(5, 10))
        self.driver.get(URL)
        time.sleep(random.randint(5, 10))

        try:
            span_ref = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/login')]"))
            )
            span_ref.click()

            # type user, password
            time.sleep(random.randint(5, 10))
            user_input = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            user_input.send_keys(self.account.get_user())
            time.sleep(random.randint(5, 10))

            pwd_input = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            pwd_input.send_keys(self.account.get_password())
            time.sleep(random.randint(5, 10))

            # login
            btn_login = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//button[@id='button-login']/span"))
            )
            btn_login.click()

            time.sleep(random.randint(1, 5))
            money = self.driver.find_element_by_id("new-money-ballans").text
            print("Success")

        except:
            print("No login, get cookies failed")
            self.driver.quit()
            raise ValueError("Login failed")

    def go_to_youtube(self):
        self.home_youtube_tab = self.driver.current_window_handle

        try:
            btn_youtube = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "YouTube"))
            )
            btn_youtube.click()

        except:
            pull_down = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "mnu_title1"))
            )
            pull_down.click()
            btn_youtube = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "YouTube"))
            )
            btn_youtube.click()
        time.sleep(random.randint(1, 3))
        btn_price = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Дорогие"))
        )
        btn_price.click()
        self.account.set_cookies(self.driver.get_cookies())
        time.sleep(random.randint(2, 5))

    def find_class_view(self, class_view):
        try:
            self.driver.switch_to.window(self.home_youtube_tab)
            span_ref = WebDriverWait(class_view, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "span"))
            )
            span_ref.click()

            btn_youtube = WebDriverWait(class_view, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "youtube-button"))
            )
            source = btn_youtube.get_attribute("data-source-traffic")
            id = btn_youtube.get_attribute("id").split("-")[-1]

            status_ref = WebDriverWait(class_view, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "status-link-youtube"))
            )
            onclick = status_ref.get_attribute("onclick")
            list_info = onclick.split("(")[1].split(")")[0]
            list_info = list_info.split(', ')
            report_id = "'" + list_info[0] + "'"
            hash_id = list_info[1]

            timer_show = WebDriverWait(class_view, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "yt-task-timer-show"))
            )
            data_timer = int(timer_show.get_attribute("data-timer"))

            if source == "aviso":
                self.driver.execute_script("""
                    $.ajax({
                        url: '/ajax/earnings/ajax-youtube.php',
                        type: 'POST',
                        data: {
                            'hash': %s,
                            'id': %s,
                            'func': 'ads-status',
                            'time': %s,
                            'player_time': %s + 3
                        },
                        dataType: 'json',
                        error: function(infa) {
                            video_serf = 0;
                        },
                        success: function(infa) {
                            video_serf = 0;
                        }
                    });
                """ % (hash_id, report_id, data_timer, data_timer))
            else:
                if self.pre_twiron is None:
                    try:
                        view_selector = WebDriverWait(class_view, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "span.go-link-youtube"))
                        )

                        count_tab = len(self.driver.window_handles)
                        view_selector.click()
                        while True:
                            if len(self.driver.window_handles) == count_tab + 1:
                                break
                            count_tab = len(self.driver.window_handles)
                            view_selector.click()
                        self.pre_twiron = self.driver.window_handles[-1]
                    except:
                        self.pre_twiron = None

                if self.pre_twiron is not None:
                    sid = self.driver.execute_script("return document.getElementById('sid').value")
                    url_redirect = "https://twiron.com/view-video?sid=" + sid + "&id=" + id
                    try:
                        r = requests.get(url_redirect, timeout=10)
                        soup = BeautifulSoup(html.unescape(r.text))
                        hash_id = "'" + soup.find('input', {'id': "hash"}).attrs['value'] + "'"
                        sid = "'" + sid.replace("252", "2") + "'"
                        self.driver.switch_to.window(self.pre_twiron)
                        self.driver.execute_script("""
                            $.ajax({
                                url: 'https://aviso.bz/ajax/earnings/ajax-youtube-domain.php',
                                type: 'POST',
                                data: {
                                    'hash': %s,
                                    'sid': %s,
                                    'func': 'ads-check',
                                    'time': %s,
                                    'player_time': %s + 3
                                },
                                dataType: 'json',
                                error: function(infa) {
                                    video_serf = 0;
                                },
                                success: function(infa) {
                                    video_serf = 0;
                                    $('#succes-error').html(infa.html);
                                }
                            });
                        """ % (hash_id, sid, data_timer, data_timer))
                    except:
                        pass
        except:
            pass

    def find_class_like(self, class_like):
        self.driver.switch_to.window(self.home_youtube_tab)
        try:
            span_ref = WebDriverWait(class_like, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "span"))
            )
            span_ref.click()
            status_ref = WebDriverWait(class_like, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "status-link-youtube"))
            )
            onclick = status_ref.get_attribute("onclick")
            self.driver.execute_script(onclick)
            time.sleep(1.5)
        except:
            pass

    def play(self):
        list_views = []
        list_likes = []
        for class_view in self.driver.find_elements_by_class_name("work-serf"):
            try:
                if class_view.text != "" and class_view.get_attribute('id').split("-")[0] == "ads":
                    list_views.append(class_view)
            except:
                continue

            try:
                if class_view.text != "" and class_view.get_attribute('id').split("-")[0] == "likes":
                    list_likes.append(class_view)
            except:
                continue

        if len(list_views) >= 3:
            count = 0
            for class_view in list_views:
                self.driver.switch_to.window(self.home_youtube_tab)
                try:
                    self.find_class_view(class_view)
                except:
                    continue

                count += 1
                if count == self.batch:
                    break

            for class_like in list_likes:
                self.driver.switch_to.window(self.home_youtube_tab)
                try:
                    self.find_class_like(class_like)
                except:
                    continue

        else:
            # Change VPN connectionsSSSS
            if len(self.list_query_select_locate) != 0:
                self.driver.switch_to.window(self.tab_vpn)
                status = self.driver.execute_script(QUERY_STATUS)
                if status == "":
                    self.driver.execute_script(QUERY_CLICK_ON_OFF)
                    self.driver.execute_script(QUERY_CHANGE_LOCATE)
                    query_select_locate = self.list_query_select_locate.pop(0)
                    self.driver.execute_script(query_select_locate)

                else:
                    try:
                        self.driver.execute_script(QUERY_CHANGE_LOCATE)
                        query_select_locate = self.list_query_select_locate.pop(0)
                        self.driver.execute_script(query_select_locate)
                    except:
                        query_select_locate = self.list_query_select_locate.pop(0)
                        self.driver.execute_script(query_select_locate)
            else:
                raise ValueError("List View Empty")

        self.driver.switch_to.window(self.home_youtube_tab)
        self.driver.refresh()
        self.driver.implicitly_wait(5)
        self.play()

    def run_to_end(self):
        try:
            self.play()
        except:
            #             update count_login
            money = self.driver.find_element_by_id("new-money-ballans").text
            self.account.set_end_coins(float(money.split(" ")[0]))
            self.account.set_end_time(time.strftime("%H:%M-%d/%m"))
            self.account.set_total_coins_per_day(self.account.get_end_coins() - self.account.get_start_coins())
            self.account.set_cookies(self.driver.get_cookies())
            self.driver.quit()

        return self.account



