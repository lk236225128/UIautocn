#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import os
import pytest
from PIL import Image
from time import sleep
from Base import utils
import cv2
import numpy as np

from appium import webdriver

# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )
from run import PATH


@allure.feature('安卓廣告业务')
class TestAdvertAndroid(object):
    @allure.story('顶部banner')
    def test_top_banner(self, getDriver):
        getDriver.find_element_by_id("com.addcn.car8891:id/close").click()

        result = []

        # 截取banner轮播图片
        TEMP_FILE1 = PATH("./tmp/usedCar_screenshot/top_banner1.png")
        elementPath = "com.addcn.car8891:id/image"
        TEMP_FILE1 = utils.getElementImgHashById(getDriver, TEMP_FILE1, elementPath)
        result.append(TEMP_FILE1)
        sleep(6)

        TEMP_FILE2 = PATH("./tmp/usedCar_screenshot/top_banner2.png")
        elementPath = "com.addcn.car8891:id/image"
        TEMP_FILE2 = utils.getElementImgHashById(getDriver, TEMP_FILE2, elementPath)
        result.append(TEMP_FILE2)
        sleep(6)

        TEMP_FILE3 = PATH("./tmp/usedCar_screenshot/top_banner3.png")
        elementPath = "com.addcn.car8891:id/image"
        TEMP_FILE3 = utils.getElementImgHashById(getDriver, TEMP_FILE3, elementPath)
        result.append(TEMP_FILE3)
        sleep(6)

        TEMP_FILE4 = PATH("./tmp/usedCar_screenshot/top_banner4.png")
        elementPath = "com.addcn.car8891:id/image"
        TEMP_FILE4 = utils.getElementImgHashById(getDriver, TEMP_FILE4, elementPath)
        result.append(TEMP_FILE4)
        #對結果列表排序
        result.sort()

        #获取预期结果列表
        #TODO 改为请求DFP素材下载保存，再进行相似度对比
        usedCarBannerList = utils.getusedCarBanner()

        #斷言結果是否與預期一致
        assert result == usedCarBannerList

    # 因测试环境api加载不稳定，待调试
    # @allure.story('首页中部广告')
    # def test_mid_banner(self, getDriver):
    #     getDriver.find_element_by_id("com.addcn.car8891:id/close").click()
    #     getDriver.swipe(start_x=75, start_y=2000, end_x=75, end_y=0, duration=800)
    #
    #     TEMP_FILE1 = PATH("./tmp/usedCar_screenshot/mid_banner1.png")
    #     elementPath = "com.addcn.car8891:id/image"
    #     TEMP_FILE1 = utils.getElementImg(getDriver, TEMP_FILE1, elementPath)
    #     sleep(7)
    #
    #     TEMP_FILE2 = PATH("./tmp/usedCar_screenshot/mid_banner2.png")
    #     elementPath = "com.addcn.car8891:id/image"
    #     TEMP_FILE2 = utils.getElementImg(getDriver, TEMP_FILE2, elementPath)
    #     sleep(7)

    @allure.story('列表页广告')
    def test_list_banner(self, getDriver):
        getDriver.find_element_by_id("com.addcn.car8891:id/close").click()

        if getDriver.find_element_by_id("com.addcn.car8891:id/refresh"):
            getDriver.find_element_by_id("com.addcn.car8891:id/refresh").click()
        getDriver.find_element_by_xpath("//android.widget.TextView[@text='Audi嚴選']").click()
        getDriver.find_element_by_id("com.addcn.car8891:id/topdealer").click()

        TEMP_FILE1 = PATH("./tmp/usedCar_screenshot/list_banner1.png")
        elementPath = "com.addcn.car8891:id/image_ad"
        TEMP_FILE1 = utils.getElementImgHashById(getDriver, TEMP_FILE1, elementPath)

        img= PATH("./tmp/usedCar_screenshot/exp_list_banner1.png")
        targetImg = cv2.imread(img)
        hashValue = utils.aHash(targetImg)

        assert TEMP_FILE1==hashValue


if __name__ == '__main__':
    pytest.main(['./tests/android_test_case/'])
