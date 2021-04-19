import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password


def login(username, password):
    browser = webdriver.Chrome('../chrome/chromedriver')
    browser.get('https://www.instagram.com/')
    time.sleep(5)

    try:
        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        button.send_keys(Keys.ENTER)  # Save the login and password
        button2 = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        time.sleep(5)
        button2.send_keys(Keys.ENTER)  # Notifications
        time.sleep(5)
        # button3 = browser.find_element_by_xpath(
        #     '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')  # Img of acc
        # button3.click()
        # time.sleep(7)
        # button4 = browser.find_element_by_xpath(
        #     '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div')  # Profile
        # button4.click()
        # time.sleep(5)

    except Exception as err:
        print(err)
    finally:
        browser.close()
        browser.quit()


def go_to_profile(username, password):
    login(username, password)
    browser = webdriver.Chrome('../chrome/chromedriver')
    try:

        button3 = browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')  # Img of acc
        button3.click()
        time.sleep(15)
        button4 = browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div')  # Profile
        button4.click()
        time.sleep(5)

    except Exception as err:
        print(err)
    finally:
        browser.close()
        browser.quit()


def like(hashtag, username, password):
    '''This function is gonna search for a specified hashtag and put likes on some posts'''
    # login(username, password)
    browser = webdriver.Chrome('../chrome/chromedriver')
    browser.get('https://www.instagram.com/')
    time.sleep(5)
    try:
        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        button.send_keys(Keys.ENTER)  # Save the login and password
        button2 = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        time.sleep(5)
        button2.send_keys(Keys.ENTER)  # Notifications
        time.sleep(5)

        browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(5)
        for i in range(3):
            browser.execute_script('window.scroll(0, document.body.scrollHeight);')
            time.sleep(7)

        links = browser.find_elements_by_tag_name('a')
        posts_urls = [item.get_attribute('href') for item in links if '/p/' in item.get_attribute('href')]

        for post in posts_urls[0:2]:
            browser.get(post)
            time.sleep(3)
            like_button = browser.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
            # like_button = browser.
            like_button.click()
            time.sleep(10)
        # for link in posts_urls:
        #     print(link)
        print(len(posts_urls))
        print(posts_urls[0:2])
        time.sleep(10)
    except Exception as err:
        print(err)
    finally:
        browser.close()
        browser.quit()
        # print(len(posts_urls))


# go_to_profile(username, password)
like('tesla', username, password)