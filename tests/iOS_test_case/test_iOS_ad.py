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
        assert True


    @allure.story('顶部banner')
    def test_top_banner(self, getDriver):
        result=[]
        elementValue="name == 'home_banner0'"

        getDriver.find_element_by_ios_predicate("name == 'home_banner0'").click()

      # 截取banner图片，并加入list
      #   TEMP_FILE1 = PATH("./tmp/usedCar_screenshot/top_banner1.png")
      #   TEMP_FILE1 = utils.getElementImgHashByPredicate(getDriver, TEMP_FILE1, elementValue)
      #   result.append(TEMP_FILE1)
      #   getDriver.find_element_by_ios_predicate("name == 'home_banner0'").click()

        assert True

if __name__ == '__main__':
    pytest.main(['./tests/iOS_test_case/'])
