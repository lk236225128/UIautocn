# import pytest
# import allure
# from selenium import webdriver
# import os
#
#
# @allure.feature('百度feature2')
# class TestClass2(object):
#     @allure.story('访问百度首页2')
#     def test_one(self, getDriver):
#         input_box = getDriver.find_element_by_id("kw")
#         input_box.send_keys("test222222")
#         submit = getDriver.find_element_by_id("su")
#         submit.click()
#         title = getDriver.title
#         assert '百度一下' in title
#
#     @allure.story('判断是否有attr2')
#     def test_two(self, getDriver):
#         input_box = getDriver.find_element_by_id("kw")
#         input_box.clear()
#         input_box.send_keys("abc2222")
#         submit = getDriver.find_element_by_id("su")
#         submit.click()
#         title = getDriver.title
#         assert '百度' in title
#
#     @allure.step('success判断')
#     def test_success(self):
#         assert True
#
#     @allure.step
#     def test_failure(self):
#         assert False
#
#     @allure.step
#     def test_skip(self):
#         assert False
#
#     @allure.step
#     def test_success2(self):
#         assert True
