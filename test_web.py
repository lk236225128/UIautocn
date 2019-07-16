from selenium import webdriver
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

chromedriver = PATH("chromedriver")
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()  # 将浏览器最大化
driver.get("https://www.baidu.com")

input_box=driver.find_element_by_id("kw")
input_box.send_keys("test")
submit=driver.find_element_by_id("")