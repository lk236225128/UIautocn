import allure
from run import PATH
from PageObject.Web.HomePage.BasePage import BasePage


@allure.feature('车商业务')
class TestSeller(object):
    # @allure.story('访问百度首页234')
    # def test_one(self, getDriver):
    #     app = {"driver": getDriver,
    #            "path": PATH("./Yamls/Web//baidu.yaml")}
    #     page = BasePage(app)
    #     page.operate()

    # @allure.story('判断是否有234')
    # def test_two(self, getDriver):
    #     input_box = getDriver.find_element_by_id("kw")
    #     input_box.clear()
    #     input_box.send_keys("bcd")
    #     submit = getDriver.find_element_by_id("su")
    #     submit.click()
    #     title = getDriver.title
    #     assert '百度一下' in title

    @allure.story('登录8891')
    def test_login(self, getDriver):
        app = {"driver": getDriver,
               "path": PATH("./Yamls/Web/Seller/Login.yaml")}
        page = BasePage(app)
        page.operate()
        print("test_login run")

    # @allure.story('刊登汽车')
    # def test_publish(self, getDriver):
    #     app = {"driver": getDriver,
    #            "path": PATH("./Yamls/Web/Seller/Publish.yaml")}
    #     page = BasePage(app)
    #     page.operate()
    #
    # @allure.story('订单支付')
    # def test_pay(self, getDriver):
    #     app = {"driver": getDriver,
    #            "path": PATH("./Yamls/Web/Seller/SellerPay.yaml")}
    #     page = BasePage(app)
    #     page.operate()

    # @allure.story('刊登机车')
    # def test_publishmotor(self, getDriver):
    #     app = {"driver": getDriver,
    #            "path": PATH("./Yamls/Web/Seller/PublishMotor.yaml")}
    #     page = BasePage(app)
    #     page.operate()

    # @allure.story('特色说明')
    # def test_description(self, getDriver):
    #     app = {"driver": getDriver,
    #            "path": PATH("./Yamls/Web/Seller/Description.yaml")}
    #     page = BasePage(app)
    #     page.operate()

    # @allure.story('广告管理')
    # def test_description(self, getDriver):
    #     #Todo
    #     pass

    # @allure.story('网路店铺管理')
    # def test_shopmanage(self, getDriver):
    #     app = {"driver": getDriver,
    #            "path": PATH("./Yamls/Web/Seller/ShopManage.yaml")}
    #     page = BasePage(app)
    #     page.operate()

    # @allure.story('会员功能')
    # def test_membership(self, getDriver):
    #     app = {"driver": getDriver,
    #            "path": PATH("./Yamls/Web/Seller/Membership.yaml")}
    #     page = BasePage(app)
    #     page.operate()

    @allure.story('储值发票')
    def test_storedandinvoice(self, getDriver):
        app = {"driver": getDriver,
               "path": PATH("./Yamls/Web/Seller/StoredAndInvoice.yaml")}
        page = BasePage(app)
        page.operate()