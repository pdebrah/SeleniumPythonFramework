from selenium.webdriver.common.by import By



class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.ID, "Email")
    password = (By.ID, "Password")

    def emailItems(self):
        return self.driver.find_element(*LoginPage.email)

    def passwordItems(self):
        return self.driver.find_element(*LoginPage.email)