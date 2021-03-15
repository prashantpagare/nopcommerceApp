import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_Login_DDT(self,setup):
        self.logger.info("**********test_Login_DDT test ***********")
        self.logger.info("********** Verifying Login test **********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in Excel" , self.rows)

        lst_status = []


        for rowz in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',rowz,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', rowz, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', rowz, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("Test is Passed")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("Test Failed")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("Test Failed")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("Test is Passed")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Test is Passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Test  Failed")
            self.driver.close()
            assert False

        self.logger.info("End of DDT Login Test")
        self.logger.info("**********test_Login_DDT Completed***")




