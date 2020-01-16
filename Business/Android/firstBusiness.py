from Handle.Android.firstHandle import FirstHandle
from Page.Android.firstPage import FirstPage

from Handle.Android.listHandle import ListHandle

from Business.Android.loginBusiness import LoginBusiness
from Base import utils
from time import sleep
from run import PATH


class FirstBusiness:
    def __init__(self, driver):
        self.first_handle = FirstHandle(driver)
        self.list_handle = ListHandle(driver)
        self.first_page = FirstPage(driver)
        self.driver = driver

    def close_mask(self):
        self.first_handle.close_mask()
        return self

    def check_online_topbanner(self):
        return self.first_handle.check_top_ad_displayed()

    def check_online_listbanner(self):
        self.first_handle.click_audi_topdealer() \
            .click_select_topdealer()
        return self.list_handle.check_ad_displayed()

    def check_online_midbanner(self):
        self.first_handle.click_buttom_firstPage()
        utils.new_swipe_up(self.driver, y_pecent=0.6)
        return self.first_handle.check_mid_displayed()

    def check_topbanner(self):
        elementPath = "com.addcn.car8891:id/ad_default_view"
        result = []
        templateimage = utils.newGetExpUsedCarTopBanner()
        list_temp = utils.newGetUsedCarTopBanner()

        for i in list_temp:
            utils.get_screenshot_picture(self.driver, i, elementPath)
            result.append(utils.match(i, templateimage))
            sleep(7)
        return result

    def check_listbanner(self):
        self.first_handle.click_audi_topdealer() \
            .click_select_topdealer()

        TEMP_FILE = utils.getBanner('listBanner')
        elementPath = "com.addcn.car8891:id/image_ad"
        utils.getElementImgHashById(self.driver, TEMP_FILE, elementPath)

        img = utils.getExpBanner("listBanner")
        result = utils.match(TEMP_FILE, img)

        return [result]

    def check_midbanner(self):
        self.first_handle.click_buttom_firstPage()
        result = []
        templateimage = utils.newgetusedCarMidBanner()
        utils.swipe_up(self.driver, x_pecent=0.5)
        sleep(1)
        utils.swipe_up(self.driver, x_pecent=0.5)
        sleep(1)
        # todo swipe不穩定,需要優化為Scroll to

        mid_banner = PATH("./tmp/usedCar_screenshot/mid_banner1.png")
        elementPath = "com.addcn.car8891:id/ad_default_view"
        utils.get_screenshot_picture(self.driver, mid_banner, elementPath)
        result.append(utils.match(mid_banner, templateimage))
        return result

    def serch_keyword(self, keywords):
        self.first_handle.click_first_search() \
            .send_search_keywords(keywords) \
            .click_searchbtn()
        return self.list_handle.get_condition_text()

    def check_four_nav(self):
        self.first_handle.click_buttom_firstPage().click_top_buycar()
        self.first_handle.click_buttom_firstPage().click_top_sellcar()
        self.first_handle.click_buttom_firstPage().click_top_8891dealer()
        self.first_handle.click_buttom_firstPage().click_top_specialServer()
        result = self.first_handle.get_specialServer_title_text()
        self.first_handle.click_specialServer_back()
        return result

    def check_8891news(self):
        self.first_handle.click_8891news().click_news_back()
        return FirstPage(self.driver).get_8891news_tag_element()
