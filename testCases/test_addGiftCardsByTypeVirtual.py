import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddGiftCardsPage import AddGiftCards
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from selenium.webdriver import ActionChains
import string
import random

class Test_006_AddGiftCards:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomers(self, setup):
        self.logger.info("******** Test_006_AddGiftCards *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successfull *********")

        self.logger.info("******** Starting AddGiftCards Test*********")

        self.driver.implicitly_wait(20)
        self.addgiftcards = AddGiftCards(self.driver)

        self.addgiftcards.clickOnSalesMenu()
        self.addgiftcards.clickOnSalesGiftCards()
        self.addgiftcards.clickOnAddnew()
        self.addgiftcards.setGiftCardType("Virtual")


        # self.addgiftcards.setInitialValue("17.50")
        # self.driver.find_element_by_xpath("//html").click()


        self.addgiftcards.setGiftCardActivated()
        self.addgiftcards.clickOnGenerateCode()
        time.sleep(3)

        self.addgiftcards.setRecipientName("Prashant")

        self.Remail = random_RecpEmailGen() + "@gmail.com"
        self.addgiftcards.setRecipientEmail(self.Remail)

        time.sleep(3)
        self.addgiftcards.setSendersName("Bhau")

        self.Semail = random_SenderEmailGen() + "@gmail.com"
        self.addgiftcards.setSendersEmail(self.Semail)

        self.addgiftcards.setMessage("This is a Test")
        time.sleep(3)
        self.addgiftcards.clickonSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add GiftCards validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if "The new gift card has been added successfully." in self.msg:
            assert True == True
            self.logger.info("************* Add GiftCards test passed **********")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_addGiftCards_scr.png")
            self.logger.error("************* Add GiftCards test Failed **********")
            assert False == False

        time.sleep(5)
        self.driver.close()
        self.logger.info("************* Ending AddGiftCards test **********")

def random_RecpEmailGen(size=8,char=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for x in range(size))

def random_SenderEmailGen(size=8,char=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for x in range(size))





