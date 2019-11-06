import pytest
import allure
import yaml
import os
from appium import webdriver

from run import PATH


APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
PLATFORM_VERSION = '9'

@pytest.fixture(scope="function")
def getDriver(request):
    desired_caps = {
        'appPackage': 'com.addcn.car8891',
        'appActivity': 'com.addcn.car8891.view.ui.activity.WelcomeActivity',
        'platformName': 'android',
        'platformVersion': PLATFORM_VERSION,
        'deviceName': '4d9b81a6',
        # 'app': PATH('./tests/android_test_case/105.apk'),
        'autoGrantPermissions': True,
        'automationName': "uiautomator2"
    }
    driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)
    driver.implicitly_wait(5000)
    #
    # def fin():
    #     driver.quit()
    #
    # request.addfinalizer(fin)
    return driver  # provide the fixture value
