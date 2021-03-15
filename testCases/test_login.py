import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_HomePageTitle(self,setup):
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying Home Page Title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** HomePage Title Test is Passed **********")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_HomePageTitle.png")
            self.driver.close()
            self.logger.error("********** HomePage Title Test is Failed **********")
            assert False


    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info("********** Verifying Login test **********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        self.lp.clickLogout()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("********** Login Test is Passed **********")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_Login.png")
            self.driver.close()
            self.logger.error("********** Login Test is Failed **********")
            assert False
