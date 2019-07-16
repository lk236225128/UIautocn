import unittest
from appium import webdriver

#unittest example
class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'J5AZB760T547H5K'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['appPackage'] = 'com.addcn.car8891'
        desired_caps['appWaitActivity'] = 'com.addcn.car8891.view.ui.activity.WelcomeActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        desired_caps["autoGrantPermissions"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        btn=self.driver.find_element_by_id("action1")
        btn.click()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase('test_something'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class HelloWorld(unittest.TestCase):
    def test_addContact(self):
        pass


if __name__ == '__main__':
    suite=unittest.TestLoader().loadTestsFromTestCase(HelloWorld)
    unittest.TextTestRunner(verbosity=2).run(suite)