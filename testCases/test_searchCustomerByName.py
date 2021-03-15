import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomersPage import SearchCustomers
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_004_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("************ SearchCustomerByName_004 *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************ Login Successful *********** ")

        self.logger.info("************Starting SearchCustomerByEmail*********** ")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCutomerMenu()
        self.addcust.clickOnCutomerMenuItem()

        self.logger.info("************Searching CustomerByName*********** ")
        searchcust = SearchCustomers(self.driver)
        searchcust.setFirstname("Brenda")
        searchcust.setLastname("Lindgren")
        time.sleep(2)
        searchcust.clickonSearch()
        self.driver.save_screenshot(".\\ScreenShots\\" + "test_searchCustomerbyName_scr.png")


        status = searchcust.searchCustomersByName("Brenda Lindgren")
        self.driver.close()
        assert True==status

        self.logger.info("************ SearchCustomerByEmail Ended *********** ")









