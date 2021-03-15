import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomers:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomers(self,setup):
        self.logger.info("******** Test_003_AddCustomers *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successfull *********")

        self.logger.info("******** Starting AddCustomers Test*********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCutomerMenu()
        self.addcust.clickOnCutomerMenuItem()
        self.addcust.clickOnAddNew()

        self.logger.info("********Providing Customer info *********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstname("Prashant")
        self.addcust.setLastname("Pagare")
        self.addcust.setCompanyName("Invisible")
        self.addcust.setGender("Male")
        self.addcust.setDob("05/05/1990")
        self.addcust.setCustomerRole("Guests")
        self.addcust.setManagerofVendor("Vendor 2")
        self.addcust.setAdminContent("This is for testing......")
        self.addcust.clickonSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("************* Add customer test passed **********")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_addCustomer_scr.png")
            self.logger.error("************* Add customer test Failed **********")
            assert False == False

            self.driver.close()
            self.logger.info("************* Ending AddCustomers test **********")






def random_generator(size=8, chars=string.ascii_lowercase + string.digits ):
    return ''.join(random.choice(chars) for x in range(size))