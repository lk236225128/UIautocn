#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import os
import pytest

from appium import webdriver
from PageObject.Android.HomePage.BasePage import BasePage

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


@allure.feature('安卓业务')
class TestWebViewAndroid(object):

    @allure.story('登录Android')
    def test_add_contacts(self, getDriver):
        app = {"driver": getDriver,"path": PATH("/Users/luokai/PycharmProjects/UIautocn/Yamls/Android/loginTest.yaml")}
        page = BasePage(app)
        page.operate()

if __name__ == '__main__':
    pytest.main(['./tests/android_test_case/'])