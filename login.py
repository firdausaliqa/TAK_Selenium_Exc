import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pageObject.homePage import regisPage
from pageObject.loginPage import loginData,  loginPage

class DemowebShop(unittest.TestCase):
    
    def setUp(self): #python test method, this cannot be modified (not recognized as testcase)
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_a_successlogin(self):
        browser = self.browser
        delay = 5 #in seconds
        browser.get(loginPage.url)
        self.assertIn(loginPage.title, self.browser.title) #validate tab title
        browser.find_element(By.ID, loginPage.email).send_keys(loginData.email_valid)
        browser.find_element(By.ID, loginPage.passw).send_keys(loginData.passw_valid)
        browser.find_element(By.ID, loginPage.rme).click()
        browser.find_element(By.XPATH, loginPage.login_btn).click()
        login_log = browser.find_element(By.CSS_SELECTOR, regisPage.cust_info).text
        self.assertEqual(loginData.email_valid, login_log) #validate logged in email

if __name__ == '__main__':
    unittest.main()