from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass
import pytest


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://dev.id.netwealth.com/Account/RegisterCompleted?ReturnUrl=https%3A%2F%2Fdev.netwealth.com%2Flogin")
# driver.get("https://dev.id.netwealth.com/Account/LogIn")
# print(driver.title)
# print(driver.current_url)
# driver.maximize_window()


class TestTwo(BaseClass):
    #def __init__(self, driver):
        #self.driver = driver

    def test_e2e(self):
        self.driver.find_element(By.LINK_TEXT, "Log In").click()
        self.driver.find_element(By.ID, "Password").click()
        self.driver.find_element(By.ID, "Password").clear()
        self.driver.find_element(By.ID, "Email").send_keys("pdebrah32@yahoo.com")
        self.driver.find_element(By.ID, "Password").send_keys("Akwasi1!")
        self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
        self.driver.get("https://dev.app.netwealth.com/app/dashboard")
        self.driver.get_screenshot_as_file("screen.png")
