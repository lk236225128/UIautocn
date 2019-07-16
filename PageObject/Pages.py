from Base.BaseOperate import OperateElement
import time
from Base.BaseElementEnmu import Element as be
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class PagesObjects:

    '''
    page层
    kwargs: WebDriver driver, String yaml(yaml配置参数)
    isOperate: 操作失败，检查点就失败
    testInfo：
    testCase：
    '''

    def __init__(self, kwargs):
        self.driver = kwargs["driver"]
        self.operateElement = OperateElement(self.driver)
        self.isOperate = True
        self.test_msg = kwargs["yaml"]
        # self.testInfo = self.test_msg[1]["testinfo"]
        # self.testCase = self.test_msg[1]["testcase"]
        # self.testcheck = self.test_msg[1]["check"]
        self.get_value = []
        self.is_get = False  # 检查点特殊标志，结合get_value使用。若为真，说明检查点要对比历史数据和实际数据
        self.msg = ""

    '''
     操作步骤
    '''

    def operate(self):
        if self.test_msg[0] is False: # 如果用例编写错误
            self.isOperate = False
            return False
        for item in self.testCase:
            result = self.operateElement.operate(item)
            if not result["result"]:
                self.isOperate = False
                return False

            if item.get("is_time", "0") != "0":
                time.sleep(item["is_time"])  # 等待时间

            if item.get("operate_type", "0") == be.GET_VALUE or item.get("operate_type", "0") == be.GET_CONTENT_DESC:
                self.get_value.append(result["text"])
                self.is_get = True  # 对比数据

        return True
