from selenium import webdriver
from information import username, password
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


usernamesList = []
usernamesWithAtSign = []


class InstagramBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('http://www.instagram.com')
        sleep(2)
        yourUsername = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')
        yourUsername.send_keys(username)
        yourPassword = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')
        yourPassword.send_keys(password)
        self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button/div').click()
        sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]').click()

    def roll_down_direct(self):
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        sleep(1)

        for i in range(5):
            page = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div')
            page.click()
            self.driver.find_element_by_tag_name('body').send_keys(Keys.END)
            sleep(1)
            page = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div')
            page.click()
            sleep(1)
            self.driver.find_element_by_tag_name('body').send_keys(Keys.END)
            sleep(1)

    def get_usernames(self):
        self.driver.find_element_by_xpath(
            '//*[@id = "react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
        sleep(2)
        username = self.driver.find_elements_by_class_name('uL8Hv')

        for name in username:
            usernamesList.append(name.text)

        del(usernamesList[0])
        del(usernamesList[0])
        del(usernamesList[0])

        for name in usernamesList:
            atSignName = "@"+name
            usernamesWithAtSign.append(atSignName)

    def export_as_txt(self):
        f = open("C:\\Users\\lucas\\Downloads\\usernames.txt", "w+")
        for item in usernamesWithAtSign:
            f.write("%s\n" % item)
        f.close()

    def play(self):
        self.login()
        self.roll_down_direct()
        self.get_usernames()
        self.export_as_txt()


bot = InstagramBot()
bot.play()
