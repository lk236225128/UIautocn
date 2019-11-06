import pytest
import allure
import yaml
import os
from appium import webdriver

from run import PATH


APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
PLATFORM_VERSION = '9'

@pytest.fixture(scope="class")
def getDriver(request):
    desired_caps = {
        "platformName": "iOS",
        "automationName": "XCUITest",
        "autoAcceptAlerts": True,
        "noReset": True,
        "platformVersion": "13.0",
        "deviceName": "iPhone Simulator",
        "app": "/Users/kevin/Project/UIautocn/tests/iOS_test_case/3.5.1.1.ipa"
    }
    driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)
    driver.implicitly_wait(5000)

    return driver
