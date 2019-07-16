import os
import time

from Base.WebBaseElementEnmu import Element as be
from Base.WebBaseOperate import OperateElement

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class PagesObjects:
    '''
    page层
    kwargs: WebDriver driver, String path(yaml配置参数)
    isOperate: 操作失败，检查点就失败
    testInfo：
    testCase：
    '''

    def __init__(self, kwargs):
        self.driver = kwargs["driver"]

        self.operateElement = ""
        self.isOperate = True
        self.test_msg = kwargs["test_msg"]
        self.testInfo = self.test_msg[1]["testinfo"]
        self.testCase = self.test_msg[1]["testcase"]
        # self.test_check = self.test_msg[1]["check"]
        self.get_value = []
        self.is_get = False  # 检查点特殊标志，结合get_value使用。若为真，说明检查点要对比历史数据和实际数据
        self.msg = ""

    '''
     操作步骤
    '''

    def operate(self):

        if self.test_msg[0] is False:
            self.isOperate = False
            return False
        self.operateElement = OperateElement(self.driver) #查找元素的对象
        for item in self.testCase:
            result = self.operateElement.operate(item, self.testInfo)
            if not result["result"]:
                return False
            if item.get("is_time", "0") != "0":
                time.sleep(item["is_time"])  # 等待时间
                print("==等待%s秒==" % item["is_time"])
            if item.get("operate_type", "0") == be.GET_VALUE or item.get("operate_type", "0") == be.GET_TEXT:
                self.get_value.append(result["text"])
                self.is_get = True  # 对比数据

        return True
