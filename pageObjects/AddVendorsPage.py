import time
from selenium.webdriver.support.ui import Select

class AddVendors:
    link_customersMenu_xpath =  "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/i"
    link_customerVendor_xpath = "//p[contains(text(),'Vendors')]"
    btn_Addnew_xpath = "/html/body/div[3]/div[1]/div/div/a"
    txtbox_Name_xpath = "//*[@id='Name']"
    # txtbox_Decription_xpath = "//*[@id="tinymce"]/p"
    txtbox_Email_xpath = "//*[@id='Email']"
    btn_Upload_xpath = "//*[@id='picture2016559138']/div/div/div[2]"
    txtbox_AdminComent_xpath = "//*[@id='AdminComment']"
    btn_Save_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.link_customersMenu_xpath).click()

    def clickOnCustomerVendor(self):
        self.driver.find_element_by_xpath(self.link_customerVendor_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btn_Addnew_xpath).click()

    def setName(self, name):
        self.driver.find_element_by_xpath(self.link_customersMenu_xpath).send_keys(name)

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.link_customersMenu_xpath).send_keys(email)

    def clickOnUpload(self):
        self.driver.find_element_by_xpath(self.btn_Upload_xpath).click()

    def setAdminComment(self, comment):
        self.driver.find_element_by_xpath(self.txtbox_AdminComent_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btn_Save_xpath).click()