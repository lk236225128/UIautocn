#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from Business.Android.firstBusiness import FirstBusiness
from Base import utils
import sys


@allure.feature('安卓首頁业务')
class TestFirstAndroid(object):
    pass

    @allure.story('首頁-頂部搜尋')
    def test_search(self, getDriver):
        result = FirstBusiness(getDriver).close_mask().serch_keyword("測試")
        assert "測試" == result

    @allure.story('首頁-四大金剛')
    def test_four_nav(self, getDriver):
        result = FirstBusiness(getDriver).check_four_nav()
        assert "便捷的汽車買賣交易平台" in result

    @allure.story('首頁-8891看板')
    def test_8891news(self, getDriver):
        result = FirstBusiness(getDriver).check_8891news()
        assert result != None


if __name__ == '__main__':
    pytest.main(['./tests/android_test_case/', '--setup-show', '--html=./report/html/report.html'])
