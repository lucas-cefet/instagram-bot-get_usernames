from selenium import webdriver
# you need to creat a information.py file with variables username and password
from information import username, password
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


usernamesList = []
usernamesWithAtSign = []


class InstagramBot():
    def __init__(self):
        self.driver = webdriver.Chrome()  # starts a new GoogleChrome browser

    def login(self):
        self.driver.get('http://www.instagram.com')  # go to Instagram homepage
        sleep(2)
        yourUsername = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')  # find where to put username information
        yourUsername.send_keys(username)  # send username information
        yourPassword = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')  # find where to put password information
        yourPassword.send_keys(password)  # send password information
        self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button/div').click()  # click on ENTER
        sleep(3)  # wait for the first popup (maybe not that long)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button').click()  # click on NO (makes no diference YES or NO)
        sleep(2)  # wait for the second popup (maybe not that long)
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]').click()  # click on NO (makes no diference YES or NO)

    def roll_down_direct(self):
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()  # click on direct buttom
        sleep(1)

        for i in range(5):  # Here we probable have some problem. In my case (about 70 direct message), 5 loops go to the end of it. But if you have more or few msg in yours, you maybe need more or few loops. I wander if there is a way to the script knows when to stop rolling down by itself
            page = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div')
            page.click()  # click on direct msgs area
            # try to roll down (we need to get to the last message stored on your direct)
            self.driver.find_element_by_tag_name('body').send_keys(Keys.END)

            sleep(1)
            page = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div')
            # click on direct msgs area again. We need to double click on the direct area. Otherwise the Keys.END doesn't work. Believe me
            page.click()
            sleep(1)
            # try to roll down (we need to get to the last message stored on your direct)
            self.driver.find_element_by_tag_name('body').send_keys(Keys.END)
            # always good waiting a second for overcome some internet laziness
            sleep(1)

            # at the end of the for loop above you should be at the last message in your direct. If you are not, increase de range(5). 5 works for +- 70 messages stored

    def get_usernames(self):
        self.driver.find_element_by_xpath(
            '//*[@id = "react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()  # clik on NEW MESSAGE buttom

        sleep(2)

        # here we get all information about the class uL8Hv. Notice the find_elements and no find_element!
        username = self.driver.find_elements_by_class_name('uL8Hv')

        # create a list with the text of all information we recive from uL8Hv class: we have ourselfs our username list!
        for name in username:
            usernamesList.append(name.text)

        # this delete some preview three texts like "your messages", and so one. Try yourself with and without this to see if you get the same as I do
        del(usernamesList[0])
        del(usernamesList[0])
        del(usernamesList[0])

        # this just creat a new list with a at sign (@) in front all usernames
        for name in usernamesList:
            atSignName = "@"+name
            usernamesWithAtSign.append(atSignName)

    def export_as_txt(self):
        # here you have to change the path where you want the txt.file to be created
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
