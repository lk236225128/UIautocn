from PageObject import WebPages
from Base.WebBaseYaml import getYaml


class BasePage:
    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "test_msg": getYaml(kwargs["path"])}

        self.page = WebPages.PagesObjects(_init)


    def operate(self):  # 操作步骤
        self.page.operate()
        print("BasePage run")

        # def checkPoint(self):  # 检查点
        #     self.page.checkPoint()


if __name__ == "__main__":
    pass
