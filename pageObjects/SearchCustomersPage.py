import time
from selenium.webdriver.support.ui import Select

class SearchCustomers:
    # Add page objects
    txtEmail_xpath = "//*[@id='SearchEmail']"
    txtFirstname_xpath = "//*[@id='SearchFirstName']"
    txtLastname_xpath = "//*[@id='SearchLastName']"
    # drpdobmonth_xpath = "//*[@id='SearchMonthOfBirth']"
    # drpdobday_xpath = "//*[@id='SearchDayOfBirth']"
    # txtCompanyname_xpath = "//*[@id='SearchCompany']"
    # txtipaddress_xpath = "//*[@id='SearchIpAddress']"
    # txtCustomerRoles_xpath = "/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div"
    # listbox_Registered_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[1]"
    # listbox_Administrators_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[1]"
    # listbox_Guests_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[1]"
    # listbox_Vendors_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[1]"
    btnSearch_xpath = "//*[@id='search-customers']"
    tblSearchResult_xpath = "//*[@id='customers-grid_wrapper']/div[1]/div/div"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"


    # Action Events

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).clear()
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setFirstname(self,firstname):
        self.driver.find_element_by_xpath(self.txtFirstname_xpath).clear()
        self.driver.find_element_by_xpath(self.txtFirstname_xpath).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element_by_xpath(self.txtLastname_xpath).clear()
        self.driver.find_element_by_xpath(self.txtLastname_xpath).send_keys(lastname)

    # def setMonth(self ,value):
    #     drp = Select(self.driver.find_element_by_xpath(self.drpdobmonth_xpath).click())
    #     drp.select_by_visible_text(value)
    #
    # def setDay(self ,value):
    #     drp = Select(self.driver.find_element_by_xpath(self.drpdobday_xpath).click())
    #     drp.select_by_visible_text(value)
    #
    # def setComanyname(self, conname):
    #     self.driver.find_element_by_xpath(self.txtCompanyname_xpath).send_keys(conname)
    #
    # def setIPAddress(self , value):
    #     self.driver.find_element_by_xpath(self.txtipaddress_xpath).send_keys(value)
    #
    # def setCustomerRoles(self, role):
    #     self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
    #     time.sleep(3)
    #     if role == 'Registered':
    #         self.itemlist = self.driver.find_element_by_xpath(self.listbox_Registered_xpath)
    #     elif  role == 'Administrator':
    #         self.itemlist = self.driver.find_element_by_xpath(self.listbox_Administrators_xpath)
    #     elif role == 'Guests':
    #         time.sleep(3)
    #         self.driver.find_element_by_xpath(self.listbox_Registered_xpath).click()
    #         self.itemlist = self.driver.find_element_by_xpath(self.listbox_Guests_xpath)
    #     elif role == 'Registered':
    #         self.itemlist = self.driver.find_element_by_xpath(self.listbox_Registered_xpath)
    #     elif  role == 'Administrator':
    #         self.itemlist = self.driver.find_element_by_xpath(self.listbox_Administrators_xpath)
    #     else:
    #         self.itemlist = self.driver.find_element_by_xpath(self.listbox_Guests_xpath)
    #         time.sleep(2)
    #         self.driver.excute_script("arguments[0].click():", self.itemlist)

    def clickonSearch(self):
        self.driver.find_element_by_xpath(self.btnSearch_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchCustomersByEmail(self, email):
        flag = False
        for row in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(row)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomersByName(self, Name):
        flag = False
        for row in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr [" + str(row) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag





