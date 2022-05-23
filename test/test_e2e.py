import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def test_e2e(self):
        
        self.driver.find_element(By.ID, "FirstName").click()
        self.driver.find_element(By.ID, "FirstName").clear()
        self.driver.find_element(By.ID, "FirstName").send_keys("Philip")
        self.driver.find_element(By.ID, "LastName").click()
        self.driver.find_element(By.ID, "LastName").clear()
        self.driver.find_element(By.ID, "LastName").send_keys("Debrah")
        self.driver.find_element(By.ID, "Email").click()
        self.driver.find_element(By.ID, "Email").clear()
        self.driver.find_element(By.ID, "Email").send_keys("Pdebrah32@yahoo.com")
        self.driver.find_element(By.ID, "Email").click()
        self.driver.find_element(By.ID, "Email").clear()
        self.driver.find_element(By.ID, "Email").send_keys("phildebrah32@gmail.com")
        self.driver.find_element(By.ID, "Password").click()
        self.driver.find_element(By.ID, "Password").clear()
        self.driver.find_element(By.ID, "Password").send_keys("Akwasi1!")
        self.driver.find_element(By.ID, "ReferralSource").click()
        Select(self.driver.find_element(By.ID, "ReferralSource")).select_by_visible_text("Newspaper Advert")
        self.driver.find_element(By.ID, "HasOptedOutOfMarketingMaterial").click()
        self.driver.find_element(By.NAME, "RegistrationForm").click()
        self.driver.get_screenshot_as_file("screen.png")
