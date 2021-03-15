import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add Cutomer page
    lnkCustomer_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p/i"
    lnkCustomer_menuuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddnew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtboxEmail_xpath = "//*[@id='Email']"
    txtPassword_xpath = "//*[@id='Password']"
    txtFirstname = "//*[@id='FirstName']"
    txtLastname = "//*[@id='LastName']"
    rdMaleGender_xpath = "//*[@id='Gender_Male']"
    rdFemaleGender_xpath = "//*[@id='Gender_Female']"
    txtdob_xpath = "//*[@id='DateOfBirth']"
    txtCompanyname_xpath = "//*[@id='Company']"
    # chkbox_taxextempt_xpath = "//*[@id='IsTaxExempt']"
    # txtNewsletter = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div/input"
    txt_CutomerRoles_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div/input"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    # lstitemForunModerators_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li[3]/span[1]"
    lstitemGuest_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendor_xpath = "//li[contains(text(),'Vendors')]"
    drpmgmrVendor_xpath = "//*[@id='VendorId']"
    # chkbox_Active_id = "Active"
    txtboxAdminComment_xpath = "//*[@id='AdminComment']"
    btnSave_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCutomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menu_xpath).click()

    def clickOnCutomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menuuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtboxEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstname(self, firstname):
        self.driver.find_element_by_xpath(self.txtFirstname).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element_by_xpath(self.txtLastname).send_keys(lastname)

    def setCompanyName(self, comname):
        self.driver.find_element_by_xpath(self.txtCompanyname_xpath).send_keys(comname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()
        elif gender == 'Female':
            self.driver.find_element_by_xpath(self.rdFemaleGender_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtdob_xpath).send_keys(dob)

    def setCustomerRole(self, role):
        self.driver.find_element_by_xpath(self.txt_CutomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # ( Here user can be Registered or Guests) only one role
            time.sleep(3)
            self.driver.find_element_by_xpath(self.lstitemRegistered_xpath).click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuest_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendor_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuest_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)


    def setManagerofVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgmrVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtboxAdminComment_xpath).send_keys(content)

    def clickonSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()




