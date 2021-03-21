import time
from selenium.webdriver.support.ui import Select

class AddGiftCards:
    link_SalesMenu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/a/p"
    link_SalesGiftCards_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/ul/li[5]/a/p"
    btn_Addnew_xpath = "/html/body/div[3]/div[1]/div/div/a"
    drpdown_GiftCardtype_xpath = "//*[@id='GiftCardTypeId']"
    # txtbox_InitialValue_xpath = "//*[@id='Amount']"
    # btn_upkeyInitialValue_xpath = "//*[@id='gift-card-info']/div[2]/div[2]/div[2]/span[1]/span/span[2]/span[1]/span"
    # btn_downkeyInitialValue_xpath = "//*[@id='gift-card-info']/div[2]/div[2]/div[2]/span[1]/span/span[2]/span[2]/span"
    chkbox_GiftCardActivated_xpath = "//*[@id='IsGiftCardActivated']"
    # txtbox_CouponCode_xpath = "//*[@id='GiftCardCouponCode']"
    btn_GenerateCouponCode_xpath = "//*[@id='generateCouponCode']"
    txtbox_RecipientName_xpath = "//*[@id='RecipientName']"
    txtbox_RecipientEmail_xpath  = "//*[@id='RecipientEmail']"
    txtbox_SendersName_xpath = "//*[@id='SenderName']"
    txtbox_SendersEmail_xpath = "//*[@id='SenderEmail']"
    txtbox_Message_xpath = "//*[@id='Message']"
    btn_Save_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnSalesMenu(self):
        self.driver.find_element_by_xpath(self.link_SalesMenu_xpath).click()

    def clickOnSalesGiftCards(self):
        self.driver.find_element_by_xpath(self.link_SalesGiftCards_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btn_Addnew_xpath).click()

    def setGiftCardType(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpdown_GiftCardtype_xpath))
        drp.select_by_visible_text(value)

    # def setInitialValue(self, money):
    #     self.driver.find_element_by_xpath(self.txtbox_InitialValue_xpath).clear()
    #     self.driver.find_element_by_xpath(self.txtbox_InitialValue_xpath).click()
    #     self.driver.find_element_by_xpath(self.txtbox_InitialValue_xpath).send_keys(money)

        # self.driver.find_element_by_xpath(self.btn_upkeyInitialValue_xpath).click()
        # self.driver.find_element_by_xpath(self.btn_downkeyInitialValue_xpath)


    def setGiftCardActivated(self):
        checkbox = self.driver.find_element_by_xpath(self.chkbox_GiftCardActivated_xpath)
        self.driver.execute_script("arguments[0].click();", checkbox)

    def clickOnGenerateCode(self):
        self.driver.find_element_by_xpath(self.btn_GenerateCouponCode_xpath).click()

    def setRecipientName(self, Rname):
        self.driver.find_element_by_xpath(self.txtbox_RecipientName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_RecipientName_xpath).send_keys(Rname)

    def setRecipientEmail(self, Remail):
        self.driver.find_element_by_xpath(self.txtbox_RecipientEmail_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_RecipientEmail_xpath).send_keys(Remail)

    def setSendersName(self, Sname):
        self.driver.find_element_by_xpath(self.txtbox_SendersName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_SendersName_xpath).send_keys(Sname)

    def setSendersEmail(self, Semail):
        self.driver.find_element_by_xpath(self.txtbox_SendersEmail_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_SendersEmail_xpath).send_keys(Semail)

    def setMessage(self, message):
        self.driver.find_element_by_xpath(self.txtbox_Message_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_Message_xpath).send_keys(message)

    def clickonSave(self):
        self.driver.find_element_by_xpath(self.btn_Save_xpath).click()