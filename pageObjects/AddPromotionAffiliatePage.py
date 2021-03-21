import time
from selenium.webdriver.support.ui import Select

class AddPromotionAffiliate:
    link_PromotionMenu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[5]/a/p"
    link_Affiliates_xpath = "//p[contains(text(),'Affiliates')]"
    btn_AddNew_xpath = "//body/div[3]/div[1]/div[1]/div[1]/a[1]"
    chkbox_Active_xpath = "//*[@id='Active']"
    txtbox_Firstname_xpath = "//*[@id='Address_FirstName']"
    txtbox_Lastname_xpath = "//*[@id='Address_LastName']"
    txtbox_Email_xpath = "//*[@id='Address_Email']"
    txtbox_Company_xpath = "//*[@id='Address_Company']"
    drpdown_Country_xpath = "//*[@id='Address_CountryId']"
    drpdown_StateProvince_xpath= "//*[@id='Address_StateProvinceId']"
    txtbox_Region_xpath = "//*[@id='Address_County']"
    txtbox_City_xpath = "//*[@id='Address_City']"
    txtbox_Address1_xpath = "//*[@id='Address_Address1']"
    txtbox_Address2_xpath = "//*[@id='Address_Address2']"
    txtbox_ZipPostalCode_xpath = "//*[@id='Address_ZipPostalCode']"
    txtbox_PhoneNumber_xpath = "//*[@id='Address_PhoneNumber']"
    txtbox_FaxNumber_xpath = "//*[@id='Address_FaxNumber']"
    txtbox_AdminComment_xpath = "//*[@id='AdminComment']"
    txtbox_FriendlyURLName_xpath = "//*[@id='FriendlyUrlName']"
    btn_Save_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnPromotionMenu(self):
        self.driver.find_element_by_xpath(self.link_PromotionMenu_xpath).click()

    def clickOnAffiliates(self):
        self.driver.find_element_by_xpath(self.link_Affiliates_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btn_AddNew_xpath).click()

    def clickOnActive(self):
        Active_Chkbox = self.driver.find_element_by_xpath(self.chkbox_Active_xpath)
        self.driver.execute_script("arguments[0].click();", Active_Chkbox)

    def setFirstname(self, Fname):
        self.driver.find_element_by_xpath(self.txtbox_Firstname_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_Firstname_xpath).send_keys(Fname)

    def setLastname(self, Lname):
        self.driver.find_element_by_xpath(self.txtbox_Lastname_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_Lastname_xpath).send_keys(Lname)

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtbox_Email_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_Email_xpath).send_keys(email)

    def setCompany(self, comp):
        self.driver.find_element_by_xpath(self.txtbox_Company_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_Company_xpath).send_keys(comp)

    def selectCountry(self, value):
        country = Select(self.driver.find_element_by_xpath(self.drpdown_Country_xpath))
        country.select_by_visible_text(value)

    def selectState(self, value):
        state = Select(self.driver.find_element_by_xpath(self.drpdown_StateProvince_xpath))
        state.select_by_visible_text(value)

    def setRegion(self, country):
        self.driver.find_element_by_xpath(self.txtbox_Region_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_Region_xpath).send_keys(country)

    def setCity(self, city):
        self.driver.find_element_by_xpath(self.txtbox_City_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_City_xpath).send_keys(city)

    def setAddress1(self, add1):
        self.driver.find_element_by_xpath(self.txtbox_Address1_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_Address1_xpath).send_keys(add1)

    def setAddress2(self, add2):
        self.driver.find_element_by_xpath(self.txtbox_Address2_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_Address2_xpath).send_keys(add2)

    def setPostalCode(self, zip):
        self.driver.find_element_by_xpath(self.txtbox_ZipPostalCode_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_ZipPostalCode_xpath).send_keys(zip)

    def setPhoneNumber(self, phone):
        self.driver.find_element_by_xpath(self.txtbox_PhoneNumber_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_PhoneNumber_xpath).send_keys(phone)

    def setFaxNumber(self, fax):
        self.driver.find_element_by_xpath(self.txtbox_FaxNumber_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_FaxNumber_xpath).send_keys(fax)

    def setAdminComment(self, comment):
        self.driver.find_element_by_xpath(self.txtbox_AdminComment_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_AdminComment_xpath).send_keys(comment)

    def setFriendlyURL(self, url):
        self.driver.find_element_by_xpath(self.txtbox_FriendlyURLName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_FriendlyURLName_xpath).send_keys(url)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btn_Save_xpath).click()