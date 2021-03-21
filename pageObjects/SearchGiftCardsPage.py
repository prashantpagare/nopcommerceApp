import time
from selenium.webdriver.support.ui import Select

class SearchGiftCards:
    txtbox_RecipientName_xpath = "//*[@id='RecipientName']"
    txtbox_CouponCode_xpath= "//*[@id='CouponCode']"
    drp_ActivatedStatus_xpath = "//*[@id='ActivatedId']"
    btn_Search_xpath = "//*[@id='search-giftcards']"
    tblSearchResult_xpath =  "//*[@id='giftcards-grid_wrapper']/div[1]"
    table_xpath = "//table[@id='giftcards-grid']"
    table_Rows_xpath = "//table[@id='giftcards-grid']//tbody/tr"
    table_Columns_xpath = "//table[@id='giftcards-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setRecipientName(self, name):
        self.driver.find_element_by_xpath(self.txtbox_RecipientName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_RecipientName_xpath).send_keys(name)

    def setCouponCode(self, copcode):
        self.driver.find_element_by_xpath(self.txtbox_CouponCode_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_CouponCode_xpath).send_keys(copcode)

    def setIsGiftCardsActivated(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drp_ActivatedStatus_xpath))
        drp.select_by_visible_text(value)

    def clickOnSearch(self):
        self.driver.find_element_by_xpath(self.btn_Search_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.table_Rows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.table_Columns_xpath))

    def searchGiftCardsByCouponCode(self ,CouponCode):
        flag = False
        for row in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            copcode = table.find_element_by_xpath("//table[@id='giftcards-grid']//tbody/tr["+str(row)+"]/td[3]").text
            if CouponCode == copcode:
                flag = True
                break
        return flag

    def searchGiftCardsByRecipientName(self ,Rname):
        flag = False
        for row in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='giftcards-grid']//tbody/tr["+str(row)+"]/td[4]").text
            if Rname == name:
                flag = True
                break
        return flag