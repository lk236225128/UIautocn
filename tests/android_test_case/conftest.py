import pytest
import allure
import yaml
import os
from selenium import webdriver
from run import PATH


APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
PLATFORM_VERSION = '9'

@pytest.fixture(scope="function")
def getDriver(request):
    desired_caps = {
        'appPackage': 'com.addcn.car8891',
        'appWaitActivity': 'com.addcn.car8891.view.ui.activity.WelcomeActivity',
        'platformName': 'android',
        'platformVersion': PLATFORM_VERSION,
        'deviceName': 'J5AZB760T547H5K',
        'app': PATH('./tests/android_test_case/105.apk'),
        'autoGrantPermissions': True,
        'automationName': "uiautomator2"
    }
    driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)
    #
    # def fin():
    #     driver.quit()
    #
    # request.addfinalizer(fin)
    return driver  # provide the fixture value
