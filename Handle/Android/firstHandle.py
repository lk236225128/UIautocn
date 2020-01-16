from Page.Android.firstPage import FirstPage
from Business.Android.listBusiness import ListBusiness

from Page.Android.loginPage import LoginPage
from Business.Android.loginBusiness import LoginBusiness
from Base import utils
from time import sleep
from run import PATH


class FirstHandle:
    def __init__(self, driver):
        self.driver = driver
        self.first_page = FirstPage(driver)

    def check_top_ad_displayed(self):
        return self.first_page.get_top_ad_element().is_displayed()

    def check_mid_displayed(self):
        return self.first_page.get_mid_ad_element().is_displayed()

    def close_mask(self):
        self.first_page.get_close_mask_element().click()

    def click_first_search(self):
        self.first_page.get_top_serach_element().click()
        return self

    def send_search_keywords(self, keywords):
        self.first_page.get_top_edit_search_element().send_keys(keywords)
        return self

    def click_searchbtn(self):
        self.first_page.get_searchbtn_element().click()
        return self

    def check_listbanner(self):
        utils.check_listbanner(self.driver)

    def check_midbanner(self):
        utils.check_midbanner(self.driver)

    def screenshot_picture(self):
        pass

    def click_audi_topdealer(self):
        self.first_page.get_audi_topdealer_element().click()
        return ListBusiness(self.driver)

    def click_refresh(self):
        if self.first_page.get_refresh_element():
            self.first_page.get_refresh_element().click()
        else:
            print("no refresh btn")

    def click_buttom_homePage(self):
        self.first_page.get_buttom_homePage_element().click()
        return self

    def click_buttom_firstPage(self):
        self.first_page.get_buttom_firstPage_element().click()
        return self

    def click_buttom_buycar(self):
        self.first_page.get_buttom_buycar_element().click()
        return self

    def click_buttom_sellcar(self):
        self.first_page.get_buttom_sellcar_element().click()
        return self

    def click_top_buycar(self):
        self.first_page.get_top_buycar_element().click()
        return self

    def click_top_sellcar(self):
        self.first_page.get_top_sellcar_element().click()
        return self

    def click_top_8891dealer(self):
        self.first_page.get_top_8891dealer_element().click()
        return self

    def click_top_specialServer(self):
        self.first_page.get_top_specialServer_element().click()
        return self

    def get_specialServer_title_text(self):
        return self.first_page.get_specialServer_title_element().text

    def click_specialServer_back(self):
        self.first_page.get_specialServer_back_element().click()
        return self

    def click_8891news(self):
        self.first_page.get_8891news_element().click()
        return self

    def click_news_back(self):
        self.first_page.get_news_back_element().click()
        return self