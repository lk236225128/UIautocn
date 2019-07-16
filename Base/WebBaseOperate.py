import re
import selenium.common.exceptions
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.support.ui import WebDriverWait, Select

from Base.WebBaseElementEnmu import Element as be
import allure

class OperateElement:
    def __init__(self, driver=""):
        self.driver = driver

    def findElement(self, operate):
        '''
        查找元素.operate,dict|list
        operate_type：对应的操作
        element_info：元素详情
        find_type: find类型
        '''
        try:
            t = operate["check_time"] if operate.get("check_time",
                                                     "0") != "0" else be.WAIT_TIME  # 如果自定义检测时间为空，就用默认的检测等待时间
            if operate.get("element_info", "0") == "0":  # 如果没有页面元素，就不检测是页面元素，可能是滑动等操作
                return {"result": True}
            WebDriverWait(self.driver, t).until(lambda x: self.elements_by(operate))  # 操作元素是否存在
            return {"result": True}

        except selenium.common.exceptions.TimeoutException:
            # print("==查找元素超时==")
            return {"result": False, "type": be.TIME_OUT}
        except selenium.common.exceptions.NoSuchElementException:
            # print("==查找元素不存在==")
            return {"result": False, "type": be.NO_SUCH}
        except selenium.common.exceptions.WebDriverException:
            # print("WebDriver出现问题了")
            return {"result": False, "type": be.WEB_DROVER_EXCEPTION}

    def operate(self, operate, testInfo):
        res = self.findElement(operate)
        if res["result"]:
            return self.operate_by(operate, testInfo)
        else:
            return res

    def operate_by(self, operate, testInfo):
        try:
            if operate.get("operate_type", "0") == "0":  # 如果没有此字段，说明没有相应操作，一般是检查点，直接判定为成功
                return {"result": True}

            elements = {
                be.CLICK: lambda: self.click(operate),
                be.GET_VALUE: lambda: self.get_value(operate),
                be.GET_TEXT: lambda: self.get_text(operate),
                be.SEND_KEYS: lambda: self.send_keys(operate),
                be.MOVE_TO_ELEMENT: lambda: self.move_to_element(operate),
                be.SELECT_BY_INDEX: lambda: self.select_by_index(operate),
                be.JS_EXCUTE: lambda: self.js_excute(operate),
                be.SELECT_BY_VALUE: lambda: self.select_by_value(operate),
                be.SWITCH_TO_NEWWINDOW: lambda: self.switch_to_newwindow(operate),
                be.SWITCH_TO_FRAME: lambda: self.switch_to_frame(operate),
                be.SWITCH_TO_DEFAULTFRAME: lambda: self.switch_to_defaultframe(),
                be.CONFIRM_ALERT: lambda: self.confirm_alert(),
                be.CANCEL_ALERT: lambda: self.cancel_alert(),
                be.ADD_COOKIE: lambda: self.add_cookie(operate),
                be.DOUBLE_CLICK: lambda: self.double_click(operate),
                be.OPEN_URL: lambda: self.open_url(operate),
                be.BACK_PAGE: lambda: self.back_page(),
                be.FORWARD_PAGE: lambda: self.forward_page(),
                be.REFRESH_PAGE: lambda: self.refresh_page(),
                be.MAXIMIZI_WINDOW: lambda: self.maximize_window(),
                be.ASSERT_RESULT: lambda: self.assert_result(operate)
            }
            return elements[operate.get("operate_type")]()

        except IndexError:
            # print(operate["element_info"] + "索引错误")
            return {"result": False, "type": be.INDEX_ERROR}

        except selenium.common.exceptions.NoSuchElementException:
            # print(operate["element_info"] + "页面元素不存在或没有加载完成")
            return {"result": False, "type": be.NO_SUCH}
        except selenium.common.exceptions.StaleElementReferenceException:
            # print(operate["element_info"] + "页面元素已经变化")
            return {"result": False, "type": be.STALE_ELEMENT_REFERENCE_EXCEPTION}
        except KeyError:
            # 如果key不存在，一般都是在自定义的page页面去处理了，这里直接返回为真
            return {"result": True}

    # 单击事件
    @allure.step('单击')
    def click(self, operate):
        self.elements_by(operate).click()
        return {"result": True}

    # 双击事件
    def double_click(self, operate):
        if operate["find_type"] == be.find_element_by_id or operate["find_type"] == be.find_element_by_xpath \
                or be.find_element_by_css_selector or operate["find_type"] == be.find_element_by_class_name or \
                        operate["find_type"] == be.find_element_by_link_text:
            ActionChains(self.driver).double_click(self.elements_by(operate)).perform()

        elif operate.get("find_type") == be.find_elements_by_id:
            self.elements_by(operate)[operate["index"]].click()
        return {"result": True}

    def open_url(self, operate):
        self.driver.get(operate["url"])
        return {"result": True}

    def back_page(self):
        self.driver.back()
        return {"result": True}

    def forward_page(self):
        self.driver.forward()
        return {"result": True}

    def refresh_page(self):
        self.driver.refresh()
        return {"result": True}

    def maximize_window(self):
        self.driver.maxmizi_window()
        return {"result": True}

    def upload_file(self, operate):
        pass

    @allure.step('发送文本')
    def send_keys(self, operate):
        """
        :param operate:
        :return:
        """
        time.sleep(0.5)
        self.elements_by(operate).clear()
        self.elements_by(operate).send_keys(operate["msg"])
        if operate["defaultframe"]:
            self.driver.switch_to.default_content()
        return {"result": True}

    @allure.step('清空文本')
    def clear_text(self, operate):
        self.elements_by(operate).clear()
        return {"result": True}

    @allure.step('获取text')
    def get_text(self, operate):
        '''
        :param operate:
        :return: {}
        '''

        if operate.get("find_type") == be.find_elements_by_id:
            element_info = self.elements_by(operate)[operate["index"]]

            result = element_info.get_attribute("text")
            re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)  # 只匹配中文，大小写，字母
            return {"result": True, "text": "".join(re_reulst)}

        element_info = self.elements_by(operate)
        result = element_info.get_attribute("text")

        re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)
        return {"result": True, "text": "".join(re_reulst)}

    @allure.step('获取value')
    def get_value(self, operate):
        if operate.get("find_type") == be.find_elements_by_id:
            element_info = self.elements_by(operate)[operate["index"]]

            result = element_info.get_attribute("value")
            re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)  # 只匹配中文，大小写，字母
            return {"result": True, "text": "".join(re_reulst)}

        element_info = self.elements_by(operate)
        result = element_info.get_attribute("value")

        re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)
        return {"result": True, "text": "".join(re_reulst)}

    @allure.step('鼠标悬停')
    def move_to_element(self, operate):
        ActionChains(self.driver).move_to_element(self.elements_by(operate)).perform()
        return {"result": True}

    '''
    通過index進行下拉選擇
    '''

    def select_by_index(self, operate):
        select_element = Select(self.elements_by(operate))
        all_options = select_element.options
        if all_options[operate["index"]].is_enabled() and not all_options[operate["index"]].is_selected():
            select_element.select_by_index(operate["index"])
        return {"result": True}

    def select_by_value(self, operate):
        select_element = Select(self.elements_by(operate))
        all_options = select_element.options
        if all_options[operate["value"]].is_enabled() and not all_options[operate["index"]].is_selected():
            select_element.select_by_value(operate["value"])
        return {"result": True}

    @allure.step('执行JS代码')
    def js_excute(self, operate):
        js = operate["js"]
        self.driver.execute_script(js)
        return {"result": True}

    @allure.step('切换窗口')
    def switch_to_newwindow(self, operate):
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[1])
        return {"result": True}

    @allure.step('切换frame')
    def switch_to_frame(self, operate):
        if operate["find_type"] == be.find_element_by_id or operate["find_type"] == be.find_element_by_xpath \
                or be.find_element_by_css_selector or operate["find_type"] == be.find_element_by_class_name or \
                        operate["find_type"] == be.find_element_by_link_text:
            self.driver.switch_to.frame(self.elements_by(operate))
        return {"result": True}

    @allure.step('增加cookie')
    def add_cookie(self, operate):
        cookie_name = operate["cookiename"]
        cookie_value = operate["cookievalue"]
        self.driver.add_cookie({"name": cookie_name, "value": cookie_value})
        return {"result": True}

    @allure.step('切换至默认frame')
    def switch_to_defaultframe(self):
        self.driver.switch_to.default_content()
        return {"result": True}

    @allure.step('确定弹窗')
    def confirm_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            return {"result": True}
        except selenium.common.exceptions.NoAlertPresentException:
            return {"result": False, "type": be.NO_SUCH}

    @allure.step('取消弹窗')
    def cancel_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
            return {"result": True}
        except selenium.common.exceptions.NoAlertPresentException:
            return {"result": False, "type": be.NO_SUCH}

    @allure.step('获取验证码')
    def get_validate_code(self):
        pass

    @allure.step('断言')
    def assert_result(self, operate):
        if operate["assert_point"] == 'in_title':
            assert operate["assert_value"] in self.driver.title
        elif operate["assert_point"] == 'in_page':
            assert operate["assert_value"] in self.driver.page_source
        return {"result": True}

    # 封装常用的标签
    def elements_by(self, operate):
        elements = {
            be.find_element_by_id: lambda: self.driver.find_element_by_id(operate["element_info"]),
            be.find_element_by_xpath: lambda: self.driver.find_element_by_xpath(operate["element_info"]),
            be.find_element_by_class_name: lambda: self.driver.find_element_by_class_name(operate['element_info']),
            be.find_elements_by_id: lambda: self.driver.find_elements_by_id(operate['element_info']),
            be.find_element_by_css_selector: lambda: self.driver.find_element_by_css_selector(operate['element_info']),
            be.find_element_by_link_text: lambda: self.driver.find_element_by_link_text(operate['element_info'])
        }
        return elements[operate["find_type"]]()
