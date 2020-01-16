from Page.Android.basePage import BasePage


class FirstPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def get_close_mask_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/close")

    def get_top_serach_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/text_search")

    def get_top_edit_search_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/edit_search")

    def get_searchbtn_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/text_search")

    def get_top_ad_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/ad_default_view")

    def get_mid_ad_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/ad_default_view")

    def get_top_tenenter_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/ten")

    def get_top_buycar_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/action0")

    def get_top_sellcar_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/action1")

    def get_top_8891dealer_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/gif")

    def get_top_specialServer_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/action3")

    def get_below25_element(self):
        return self.driver.find_element_by_xpath('//*[@text="25萬以下"]')

    def get_buttom_homePage_element(self):
        return self.driver.find_element_by_xpath('//*[@text="會員中心"]')

    def get_buttom_firstPage_element(self):
        return self.driver.find_element_by_xpath('//*[@text="首頁"]')

    def get_buttom_buycar_element(self):
        return self.driver.find_element_by_xpath('//*[@text="買車"]')

    def get_buttom_sellcar_element(self):
        return self.driver.find_element_by_xpath('//*[@text="賣車"]')

    def get_audi_topdealer_element(self):
        return self.driver.find_element_by_xpath('//*[@text="Audi嚴選"]')

    # 實價、實車、實況、不實賠付！>>
    def get_goto_topdealer_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/text_more")

    def get_topdealer_product_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/tag_tv")

    # 更多嚴選車輛>
    def get_goto_more_topdealer_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/more_tv")

    # 110項性能檢測，安心首選>>
    def get_goto_more_audidealer_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/text_more")

    # 更多奧迪嚴選車輛>
    def get_auditopdealer_product_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/tag_tv")

    # 更多奧迪嚴選車輛>
    def get_goto_more_audi_topdealer_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/more_tv")

    # 進入專館> 公會
    def get_goto_guild_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/text_more")

    # 進入公會物件詳情
    def get_goto_guild_product_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/tag")

    # 更多公會專館
    def get_goto_more_guild_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/more_tv")

    # 進入專館> 聯盟
    def get_goto_alliance_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/text_more")

    # 進入聯盟物件詳情
    def get_goto_alliance_product_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/tag")

    # 更多SAVE認證金選車輛>
    def get_goto_more_alliance_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/more_tv")

    # 最新出售控件
    def get_latest_sale_element(self):
        return self.driver.find_element_by_xpath('//*[@text="最新出售"]')

    # 更多中古車>
    def get_goto_more_usedproduct_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/more")

    # 台北市
    def get_goto_nearby_map_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/text_nearby_map")

    # 古馳上
    def get_goto_usedshop_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/text_shop")

    # 更多中古車行>
    def get_goto_more_usedshop_element(self):
        return self.driver.find_element_by_xpath('//*[@text="更多中古車行>"]')

    def get_refresh_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/refresh")

    def get_specialServer_title_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/membercentre_goodstop_title")

    def get_specialServer_back_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/membercentre_goodstop_brack")

    def get_8891news_element(self):
        return self.driver.find_element_by_xpath(
            '//*[@resource-id="com.addcn.car8891:id/flipper"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]')

    def get_news_back_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/back")

    def get_8891news_tag_element(self):
        return self.driver.find_element_by_id("com.addcn.car8891:id/image_news")

