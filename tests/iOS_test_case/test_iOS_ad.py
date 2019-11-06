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

from functools import reduce
from appium import webdriver

# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )
from run import PATH


@allure.feature('iOS廣告业务')
class TestAdvertAndroid(object):

    @allure.story('首次启动app')
    def test_first_open(self, getDriver):
        getDriver.find_element_by_accessibility_id("20181026 close").click()


    @allure.story('顶部banner')
    def test_top_banner(self, getDriver):
        getDriver.find_element_by_accessibility_id("20181026 close").click()
        # getDriver.find_element_by_xpath('//XCUIElementTypeApplication[@name="8891中古車"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage[2]/XCUIElementTypeImage').click()
        result=[]

      # 截取banner图片，并加入list
        TEMP_FILE1 = PATH("./tmp/usedCar_screenshot/top_banner1.png")
        elementXpath = '//XCUIElementTypeApplication[@name="8891中古車"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage[2]/XCUIElementTypeImage'
        TEMP_FILE1 = utils.getElementImgHashByXpath(getDriver, TEMP_FILE1, elementXpath)
        result.append(TEMP_FILE1)
        sleep(6)

if __name__ == '__main__':
    pytest.main(['./tests/iOS_test_case/'])
