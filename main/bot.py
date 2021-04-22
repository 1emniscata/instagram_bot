import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from main.auth_data import username, password


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
        button3 = browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')  # Img of acc
        button3.click()
        time.sleep(15)
        button4 = browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div')  #Profile
        button4.click()
        time.sleep(5)
    except Exception as err:
        print(err)
    finally:
        browser.close()
        browser.quit()


login(username, password)