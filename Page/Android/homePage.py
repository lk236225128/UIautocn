from Page.Android.basePage import BasePage
from Page.Android.listPage import ListPage
from Base import utils
from run import PATH
from time import sleep


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def get_login_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/info")

    def get_setting_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/setting")

    def get_logout_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/out")

    def get_favourite_element(self):
        return self.driver.find_element_by_xpath('//*[@text="我的收藏"]')

    def get_history_element(self):
        return self.driver.find_element_by_xpath('//*[@text="瀏覽歷史"]')

    def get_bookseecar_element(self):
        return self.driver.find_element_by_xpath('//*[@text="預約看車"]')

    def get_onlineconnect_element(self):
        return self.driver.find_element_by_xpath('//*[@text="在線聯絡"]')

    def get_pushMsg_element(self):
        return self.driver.find_element_by_xpath('//*[@text="推播消息"]')

    def get_mySubscribe_element(self):
        return self.driver.find_element_by_xpath('//*[@text="我的訂閱"]')

    def get_publishcar_element(self):
        return self.driver.find_element_by_xpath('//*[@text="刊登廣告"]')

    def get_adtop_element(self):
        return self.driver.find_element_by_xpath('//*[@text="廣告置頂"]')

    def get_selling_element(self):
        return self.driver.find_element_by_xpath('//*[@text="出售中"]')

    def get_wait_to_sell_element(self):
        return self.driver.find_element_by_xpath('//*[@text="待出售"]')

    def get_deal_element(self):
        return self.driver.find_element_by_xpath('//*[@text="已成交"]')

    def get_unAudit_element(self):
        return self.driver.find_element_by_xpath('//*[@text="未通過審核"]')

    def get_auth_element(self):
        return self.driver.find_element_by_xpath('//*[@text="身份認證"]')

    def get_impeach_element(self):
        return self.driver.find_element_by_xpath('//*[@text="我的檢舉"]')

    def get_appeal_element(self):
        return self.driver.find_element_by_xpath('//*[@text="線上申訴"]')

    def get_buttom_homePage_element(self):
        return self.driver.find_element_by_xpath('//*[@text="會員中心"]')

    def get_buttom_firstPage_element(self):
        return self.driver.find_element_by_xpath('//*[@text="首頁"]')

    def get_buttom_buycar_element(self):
        return self.driver.find_element_by_xpath('//*[@text="買車"]')

    def get_buttom_sellcar_element(self):
        return self.driver.find_element_by_xpath('//*[@text="賣車"]')

    #TODO 補充當前頁所有有功能的控件
    #
    # def goto_debug(self):
    #     self.driver.find_element_by_id("com.addcn.car8891:id/close").click()
    #     self.driver.find_element_by_id("com.addcn.car8891:id/text_search").click()
    #     self.driver.find_element_by_id("com.addcn.car8891:id/edit_search").send_keys("%%%opendebug%%%")
    #     self.driver.find_element_by_id("com.addcn.car8891:id/text_search").click()
    #     self.driver.find_element_by_id("com.addcn.car8891:id/edit_host").send_keys("www.8891.com.tw")
    #     self.driver.find_element_by_id("com.addcn.car8891:id/editText2").send_keys("0")
    #     self.driver.find_element_by_id("com.addcn.car8891:id/confirm").click()
    #     self.driver.find_element_by_id("com.addcn.car8891:id/button_back").click()
    #     return self
    #
    # def check_topbanner(self):
    #     result = []
    #     templateimage = utils.newgetusedCarTopBanner()
    #
    #     TEMP_FILE1 = PATH("./tmp/usedCar_screenshot/top_banner1.png")
    #     TEMP_FILE2 = PATH("./tmp/usedCar_screenshot/top_banner2.png")
    #     TEMP_FILE3 = PATH("./tmp/usedCar_screenshot/top_banner3.png")
    #     elementPath = "com.addcn.car8891:id/ad_default_view"
    #
    #     utils.get_creenshot_picture(self.driver, TEMP_FILE1, elementPath)
    #     result.append(utils.match(TEMP_FILE1, templateimage))
    #     sleep(7)
    #     utils.get_creenshot_picture(self.driver, TEMP_FILE2, elementPath)
    #     result.append(utils.match(TEMP_FILE2, templateimage))
    #     sleep(6)
    #     utils.get_creenshot_picture(self.driver, TEMP_FILE3, elementPath)
    #     result.append(utils.match(TEMP_FILE3, templateimage))
    #
    #     return result
    #
    # def check_listbanner(self):
    #
    #
    #     if self.driver.find_element_by_xpath("//android.widget.TextView[@text='Audi嚴選']"):
    #         self.driver.find_element_by_xpath("//android.widget.TextView[@text='Audi嚴選']").click()
    #     elif self.driver.find_element_by_id("com.addcn.car8891:id/refresh"):
    #         self.driver.find_element_by_id("com.addcn.car8891:id/refresh").click()
    #
    #     self.driver.find_element_by_id("com.addcn.car8891:id/topdealer").click()
    #
    #     TEMP_FILE1 = PATH("./tmp/usedCar_screenshot/list_banner1.png")
    #     elementPath = "com.addcn.car8891:id/image_ad"
    #     utils.getElementImgHashById(self.driver, TEMP_FILE1, elementPath)
    #
    #     img = PATH("./tmp/usedCar_screenshot/expBanner/exp_list_banner_1.png")
    #     result = utils.match(TEMP_FILE1, img)
    #
    #     return result
    #
    # def check_midbanner(self):
    #     self.driver.find_element_by_xpath('//*[@text="首頁"]').click()
    #     result = []
    #     templateimage = utils.newgetusedCarMidBanner()
    #
    #     sleep(3)
    #     utils.swipe_up(self.driver, x_pecent=0.5)
    #     sleep(3)
    #     utils.swipe_up(self.driver, x_pecent=0.5)
    #     sleep(3)
    #
    #     TEMP_FILE1 = PATH("./tmp/usedCar_screenshot/mid_banner1.png")
    #     elementPath = "com.addcn.car8891:id/ad_default_view"
    #     utils.get_creenshot_picture(self.driver, TEMP_FILE1, elementPath)
    #     result.append(utils.match(TEMP_FILE1, templateimage))
    #     sleep(7)
    #     return result
    #
    # def goto_listpage(self):
    #     pass
    #
    # def goto_login(self):
    #     self.driver.find_element_by_xpath('//*[@text="會員中心"]').click()
    #     self.driver.find_element_by_id("com.addcn.car8891:id/info").click()
    #
    #     return self
