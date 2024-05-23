import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pageObject.homePage import regisPage
from pageObject.loginPage import loginData,  loginPage

class DemowebShop(unittest.TestCase):
    
    def setUp(self): #python test method, this cannot be modified (not recognized as test)
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_a_emptylogin(self):
        browser = self.browser
        browser.get(loginPage.url)
        self.assertIn(loginPage.title, self.browser.title) #validate tab title
        browser.find_element(By.ID, loginPage.rme).click()
        browser.find_element(By.XPATH, loginPage.login_btn).click()
        error_msg = browser.find_element(By.XPATH, loginPage.nomail_ermsg).text
        nomail_msg = 'Login was unsuccessful. Please correct the errors and try again.'
        self.assertEqual(nomail_msg, error_msg) #validate error message

    def test_b_wrongpass(self):
        browser = self.browser
        browser.get(loginPage.url)
        self.assertIn(loginPage.title, self.browser.title) #validate tab title
        browser.find_element(By.ID, loginPage.email).send_keys(loginData.email_valid)
        browser.find_element(By.ID, loginPage.passw).send_keys(loginData.passw_invalid)
        browser.find_element(By.XPATH, loginPage.login_btn).click()
        error_msg = browser.find_element(By.XPATH, loginPage.wrgpass_ermsg).text
        wrpass_msg = 'The credentials provided are incorrect'
        self.assertEqual(wrpass_msg, error_msg) #validate logged in email

    def test_c_noacc(self):
        browser = self.browser
        browser.get(loginPage.url)
        self.assertIn(loginPage.title, self.browser.title) #validate tab title
        browser.find_element(By.ID, loginPage.email).send_keys(loginData.email_unreg)
        browser.find_element(By.ID, loginPage.passw).send_keys(loginData.passw_valid)
        browser.find_element(By.XPATH, loginPage.login_btn).click()
        error_msg = browser.find_element(By.XPATH, loginPage.noacc_ermsg).text
        noacc_msg = 'No customer account found'
        print(error_msg)
        self.assertEqual(noacc_msg, error_msg) #validate logged in email

if __name__ == '__main__':
    unittest.main()