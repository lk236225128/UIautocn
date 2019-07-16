from Base.BaseYaml import getYam
from PageObject import Pages


class BasePage:
    '''
    会员中心的page层
    isOperate: 操作失败，检查点就失败,kwargs: WebDriver driver, String path(yaml配置参数)
    '''

    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "test_msg": getYam(kwargs["path"])}
        self.page = Pages.PagesObjects(_init)

    def operate(self):  # 操作步骤
        self.page.operate()

    # def checkPoint(self):  # 检查点
    #     self.page.checkPoint()


if __name__ == "__main__":
    pass
