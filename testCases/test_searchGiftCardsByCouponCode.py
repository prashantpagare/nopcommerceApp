import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddGiftCardsPage import AddGiftCards
from pageObjects.SearchGiftCardsPage import SearchGiftCards
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_007_searchGiftCardsByCouponCode:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchGiftCardsByCouponCode(self, setup):
        self.logger.info("************ SearchCustomerByEmail_004 *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successfull *********")
        self.logger.info("******** Starting searchGiftCardsByCouponCode Test*********")

        self.driver.implicitly_wait(20)
        self.addgift = AddGiftCards(self.driver)
        self.addgift.clickOnSalesMenu()
        self.addgift.clickOnSalesGiftCards()

        self.searchgf = SearchGiftCards(self.driver)
        self.searchgf.setCouponCode("bd5795c9-15ee")
        # self.searchgf.setIsGiftCardsActivated("Activated")
        self.searchgf.clickOnSearch()

        time.sleep(5)
        self.driver.close()
