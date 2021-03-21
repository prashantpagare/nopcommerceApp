import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.AddPromotionAffiliatePage import AddPromotionAffiliate
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import string
import random

class Test_008_AddPromotionAffiliate:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addPromotionAffiliate(self,setup):
        self.logger.info("******** Test_008_AddPromotionAffiliate *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successfull *********")

        self.logger.info("******** Starting ADD-PromotionAffiliate Test*********")

        self.driver.implicitly_wait(20)
        self.promo = AddPromotionAffiliate(self.driver)
        self.promo.clickOnPromotionMenu()
        self.promo.clickOnAffiliates()
        self.promo.clickOnAddNew()

        self.logger.info("********Providing PromotionAffiliate info *********")

        self.promo.clickOnActive()
        self.promo.setFirstname("Prashant")
        self.promo.setLastname("Yoyo")

        self.email = random_emailGen() + "@gmail.com"
        self.promo.setEmail(self.email)
        self.promo.setCompany("Apple")
        self.promo.selectCountry("India")
        self.promo.selectState("Other")

        self.promo.setRegion("India")
        self.promo.setCity("Panvel")

        self.promo.setAddress1("anfoamfa , AIaf ")
        self.promo.setAddress2("apafa , afonafo")

        self.promo.setPostalCode("102365")
        self.promo.setPhoneNumber("")
        self.promo.setFaxNumber("456398")

        self.promo.setAdminComment("Testing")
        self.promo.setFriendlyURL("www.frndly.com")
        self.promo.clickOnSave()

        self.logger.info("************* Saving PromotionAffiliate info **********")

        self.logger.info("********* Add PromotionAffiliate validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if "The new affiliate has been added successfully." in self.msg:
            assert True == True
            self.logger.info("************* Add PromotionAffiliate test passed **********")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_addPromotionAffiliates_scr.png")
            assert False == False
            self.logger.info("************* Add PromotionAffiliate test Failed **********")

        time.sleep(3)
        self.driver.close()
        self.logger.info("************* Ending PromotionAffiliate test **********")

def random_emailGen(size=8,char=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for x in range(size))