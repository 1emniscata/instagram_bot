import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
import sys
import requests
import datetime


class Bot:

    start_time = datetime.datetime.now()

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome('../chrome/chromedriver')

    def login(self):
        browser = self.browser
        browser.get('https://www.instagram.com/')
        # time.sleep(5)
        browser.implicitly_wait(5)

        try:
            if self.xpath_exists('/html/body/div[2]/div/div/button[1]'):
                button = browser.find_element_by_xpath('/html/body/div[2]/div/div/button[1]').click()

            username_input = browser.find_element_by_name('username')
            username_input.clear()
            username_input.send_keys(username)

            # time.sleep(3)
            browser.implicitly_wait(5)

            password_input = browser.find_element_by_name('password')
            password_input.clear()
            password_input.send_keys(password)
            password_input.send_keys(Keys.ENTER)

            # time.sleep(5)
            browser.implicitly_wait(5)

            button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
            # time.sleep(3)
            browser.implicitly_wait(3)
            button.send_keys(Keys.ENTER)  # Save the login and password
            button2 = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
            # time.sleep(5)
            browser.implicitly_wait(5)
            button2.send_keys(Keys.ENTER)  # Notifications
            # time.sleep(5)
            browser.implicitly_wait(5)
        except Exception as err:
            print(err)

    def close_browser(self):
        self.browser.close()
        self.browser.quit()
        # print("Bot did it's job successfully!")

    def xpath_exists(self, xpath):

        browser = self.browser
        try:
            browser.find_element_by_xpath(xpath)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    def like_by_hashtag(self, hashtag):

        self.hashtag = hashtag
        browser = self.browser
        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            # time.sleep(3)
            browser.implicitly_wait(3)

            for i in range(3):
                browser.execute_script('window.scroll(0, document.body.scrollHeight);')
                # time.sleep(4)
                browser.implicitly_wait(3)

            items = browser.find_elements_by_tag_name('a')
            posts_links = [item.get_attribute('href') for item in items if '/p/' in item.get_attribute('href')]
            # time.sleep(5)
            browser.implicitly_wait(5)

            for post in posts_links[2:4]:
                browser.get(post)
                like_button = browser.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
                time.sleep(3)
                if like_button:
                    # print('Это вывелось?')
                    # if browser.find_element_by_class_name(
                    #     '_8-yf5 '
                    #     ).get_attribute('aria-label') == 'Нравится':

                    # Think about it
                    if browser.find_element_by_class_name('_8-yf5 '):
                        like_button.click()
                        print('Должно было нажаться')
                # time.sleep(3)
                browser.implicitly_wait(3)
                # print(browser.find_element_by_class_name('_8-yf5 ').get_attribute('aria-label').value)

                # time.sleep(3)
                # print("I've put a like on this:", post)
                # print(posts_links[:5])
        except Exception as err:
            print(err)
            Type, Value, Trace = sys.exc_info()
            # traceback.print_exception(Type, Value, Trace)  # Have some questions
            print(Type)
            print(Value)
            print(Trace)

    def like_by_profile(self, profile):
        browser = self.browser
        try:
            browser.get(profile)
            # time.sleep(3)
            browser.implicitly_wait(3)

            for i in range(2):
                browser.execute_script('window.scroll(0, document.body.scrollHeight);')
                # time.sleep(3)
                browser.implicitly_wait(3)

            items = browser.find_elements_by_tag_name('a')
            posts_links = [item.get_attribute('href') for item in items if '/p/' in item.get_attribute('href')]
            # time.sleep(5)
            browser.implicitly_wait(5)

            for post in posts_links[0:3]:
                browser.get(post)
                # time.sleep(3)
                browser.implicitly_wait(3)
                like_button = browser.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
                # time.sleep(3)
                browser.implicitly_wait(3)
                like_button.click()
                print(f"I've put a like to: {post}")
                # time.sleep(3)
                browser.implicitly_wait(3)

            finish_time = datetime.datetime.now()
            print(finish_time - self.start_time)
        except Exception as err:
            print(err)
            Type, Value, Trace = sys.exc_info()
            # traceback.print_exception(Type, Value, Trace)  # Have some questions
            print(Type)
            print(Value)
            print(Trace)

    def get_all_posts_urls(self, profile):  # Unfinished
        browser = self.browser
        profile_id = profile.split('/')[-2]
        browser.get(profile)
        # if self.xpath_exists('')  Add XPATH
        time.sleep(3)

        for i in range(2):
            browser.execute_script('window.scroll(0, document.body.scrollHeight);')
            time.sleep(3)

        items = browser.find_elements_by_tag_name('a')
        posts_links = list(set([item.get_attribute('href') for item in items if '/p/' in item.get_attribute('href')]))
        # print('Is it true:', len(posts_links) == len(set(posts_links)))
        # print(len(set(posts_links)))
        time.sleep(5)

        with open(f'{profile_id}_set.txt', 'w') as file:
            for post in posts_links:
                file.write(post + '\n')

        # print(posts_links[0].split('/'))
        # except Exception as err:
        #     print(err)
        #     Type, Value, Trace = sys.exc_info()
        #     # traceback.print_exception(Type, Value, Trace)  # Have some questions
        #     print(Type)
        #     print(Value)
        #     print(Trace)

    def download_content(self, profile):
        browser = self.browser
        self.get_all_posts_urls(profile)
        profile_name = profile.split('/')[-2]

        if os.path.exists(f'{profile_name}'):
            print('Such directory is already exists')
        else:
            os.mkdir(profile_name)

        with open(f'{profile_name}_set.txt') as file:
            posts_links = file.readlines()
            time.sleep(5)
            # img_src = '/html/body/div[1]/section/main/div/div[1]/article/div[2]/div/div/div[1]/img'
            # img_src = '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/div/div/div[1]/img'
            img_src = "/html/body/div[1]/section/main/div/div[1]/article/div[2]/div/div/div[1]/img"
            # '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[1]/img'
            # '/html/body/div[1]/section/main/div/div[1]/article/div[2]/div/div/div[1]/img'
            # video_src = '/html/body/div[1]/section/main/div/div[1]/article/div[2]/div/div/div[1]/div/div/video'
            # video_src = '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/div/div/div[1]/div/div/video'
            video_src = '/html/body/div[6]/div[2]/div/article/div[2]/div/div/div[1]/div/div/video'  # There is a problem
            img_and_video_list = []
            time.sleep(5)

            for post in posts_links[:10]:
                try:
                    browser.get(post)
                    post_id = post.split('/')[-2]
                    time.sleep(5)
                    # print('Xpath exists:', self.xpath_exists(img_src))
                    print('Xpath of video exists:', self.xpath_exists(video_src))

                    time.sleep(5)
                    # print(browser.find_element_by_xpath(img_src))
                    #     img_src_url = browser.find_element_by_xpath(img_src).get_attribute("src")
                    if self.xpath_exists(img_src):
                        img = browser.find_element_by_xpath(img_src).get_attribute('src')
                        img_and_video_list.append(img)
                        get_img = requests.get(img)

                        if os.path.exists(f'{profile_name}/imgs'):
                            print('This directory already exists')
                        else:
                            os.mkdir(f'{profile_name}/imgs')
                        print(f'The img from {post_id} downloaded')

                        with open(f'{profile_name}/imgs/{post_id}_img.jpg', 'wb') as img_file:
                            img_file.write(get_img.content)
                            print('All ok')

                    elif self.xpath_exists(video_src):
                        video = browser.find_element_by_xpath(video_src).get_attribute('src')
                        img_and_video_list.append(video)
                        get_video = requests.get(video_src)

                        if os.path.exists(f'{profile_name}/videos'):
                            print('This directory already exists')
                        else:
                            os.mkdir(f'{profile_name}/videos')

                        with open(f'{profile_name}/videos/{post_id}_video.mp4', 'wb') as video_file:
                            for chunk in get_video.iter_content(chunk_size=1024 * 1024):  # THINK ABOUT IT
                                if chunk:
                                    video_file.write(chunk)
                                    print(f'The video from {post_id} downloaded')
                    else:
                        print("I don't know what happened")
                except Exception as err:
                    print(err)
                    Type, Value, Trace = sys.exc_info()
                    # traceback.print_exception(Type, Value, Trace)  # Have some questions
                    print(Type)
                    print(Value)
                    print(Trace)

    def get_all_following_urls(self, profile):
        browser = self.browser
        try:
            browser.get(profile)

            following_button = browser.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
            following_button.click()
            following_count = int(following_button.text.split(' ')[0])
            # print(following_count)
            time.sleep(5)

            # following_ul = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
            following_ul = browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/ul')
            following_urls = []

            for i in range(following_count+1):
                browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", following_ul)
                time.sleep(3)

            all_following_uls = following_ul.find_elements_by_tag_name('li')

            for ul in all_following_uls:
                following_urls.append(ul.find_element_by_tag_name('a').get_attribute('href'))

            for url in following_urls[:2]:
                browser.get(url)
                print("I'm on that post:", url)
        except Exception as err:
            print(err)



a = Bot(username, password)
a.login()
# a.like_by_hashtag('tesla')
a.like_by_profile('https://www.instagram.com/tesla_official/')
# a.get_all_posts_urls('https://www.instagram.com/tesla_official/')
# a.download_content('https://www.instagram.com/tesla_official/')
# a.get_all_following_urls('https://www.instagram.com/tesla_official/')
a.close_browser()
