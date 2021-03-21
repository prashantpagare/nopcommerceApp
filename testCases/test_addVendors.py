import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddVendorsPage import AddVendors
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_005_AddVendors:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addVendors(self, setup):
        self.logger.info("******** Test_005_AddVendors *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successfull *********")

        self.logger.info("******** Starting AddVendors Test*********")

        self.addVen = AddVendors(self.driver)

        self.addVen.clickOnCustomersMenu()
        self.addVen.clickOnCustomerVendor()
        self.addVen.clickOnAddnew()
        self.addVen.setName("Prashant")
        self.email = random_generator() + "@gmail.com"
        self.addVen.setEmail(self.email)
        self.addVen.clickOnUpload()
        self.addVen.setAdminComment("Comment 1")
        self.addVen.clickOnSave()

        self.logger.info("************* Saving Vendors info **********")

        self.logger.info("********* Add Vendors validation started *****************")



def random_generator(size=8, chars=string.ascii_lowercase + string.digits ):
    return ''.join(random.choice(chars) for x in range(size))