import pytest
import allure
import yaml
import os
from selenium import webdriver
from run import PATH
from Base.WebBaseYaml import getYaml


# @pytest.fixture(scope="session",autouse=True)
# def env(request):
#     root_dir=request.config.rootdir
#     config_path='{0}/config/env_config.yml'.format(root_dir)
#     with open(config_path) as f:
#         env_config=yaml.load(f)
#
#     allure.environment(host=env_config['host']['domain'])
#     allure.environment(browser=env_config['host']['browser'])
#
#     return env_config

@pytest.fixture(scope="session")
def getDriver():
    chromedriver = PATH("chromedriver")
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.maximize_window()  # 将浏览器最大化
    openurl = getYaml(PATH("./Yamls/Web/config.yaml"))[1]["url"]
    driver.get(openurl)
    print("conftest run")
    return driver

