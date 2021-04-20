import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
import traceback
import sys


class Bot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome('../chrome/chromedriver')


    def login(self):
            browser = self.browser
            browser.get('https://www.instagram.com/')
            time.sleep(5)

            try:
                username_input = browser.find_element_by_name('username')
                username_input.clear()
                username_input.send_keys(username)

                time.sleep(3)

                password_input = browser.find_element_by_name('password')
                password_input.clear()
                password_input.send_keys(password)
                password_input.send_keys(Keys.ENTER)

                time.sleep(5)

                button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
                time.sleep(3)
                button.send_keys(Keys.ENTER)  # Save the login and password
                button2 = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
                time.sleep(5)
                button2.send_keys(Keys.ENTER)  # Notifications
                time.sleep(5)
            except Exception as err:
                print(err)


    def close_browser(self):
        self.browser.close()
        self.browser.quit()


    def like_by_hashtag(self, hashtag):
        self.hashtag = hashtag
        browser = self.browser
        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(3)

            for i in range(3):
                browser.execute_script('window.scroll(0, document.body.scrollHeight);')
                time.sleep(4)

            items = browser.find_elements_by_tag_name('a')
            posts_links = [item.get_attribute('href') for item in items if '/p/' in item.get_attribute('href')]
            time.sleep(5)


            for post in posts_links[2:4]:
                browser.get(post)
                like_button = browser.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
                time.sleep(3)
                if like_button:
                    # print('Это вывелось?')
                    if browser.find_element_by_class_name(
                        '_8-yf5 '
                        ).get_attribute('aria-label') == 'Нравится':
                        like_button.click()
                        print('Должно было нажаться')
                time.sleep(3)

                # time.sleep(3)
                # print("I've put a like on this:", post)
                # print(posts_links[:5])
        except Exception as err:
            print(err)
            Type, Value, Trace = sys.exc_info()
            # traceback.print_exception(Type, Value, Trace)  # Have some questions
            print(Type)
            print(Value)



a = Bot(username, password)
a.login()
a.like_by_hashtag('tesla')
a.close_browser()

