import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.homePage import regisPage
from pageObject.loginPage import loginData,  loginPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class DemowebShop(unittest.TestCase):
    
    def setUp(self): #python test method, this cannot be modified (not recognized as testcase)
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_a_successregister(self):
        print('1. Success Register testcase')
        browser = self.browser
        browser.get(regisPage.url)
        self.assertIn(regisPage.title, self.browser.title) #validate tab title
        browser.find_element(By.ID, regisPage.gender).click()
        browser.find_element(By.ID, regisPage.fname).send_keys(loginData.fName_valid)
        browser.find_element(By.ID, regisPage.lname).send_keys(loginData.lName_valid)
        browser.find_element(By.ID, regisPage.email).send_keys(loginData.email_valid)
        browser.find_element(By.ID, regisPage.passw).send_keys(loginData.passw_valid)
        browser.find_element(By.ID, regisPage.confpass).send_keys(loginData.passw_valid)
        browser.find_element(By.ID, regisPage.regis_btn).click()

if __name__ == '__main__':
    unittest.main()        