import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.homePage import regisPage
from pageObject.loginPage import loginData, loginPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class DemowebShop(unittest.TestCase):
    def setUp(self): #python test method, this cannot be modified (not recognized as testcase)
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_a_emptyregister(self):
        print('1. Failed Register - empty field testcase')
        browser = self.browser
        browser.get(regisPage.url)
        self.assertIn(regisPage.title, self.browser.title) #validate tab title
        browser.find_element(By.ID, regisPage.regis_btn).click()
        fnamerr_msg = browser.find_element(By.XPATH, regisPage.fname_errmsg).text
        #print(fnamerr_msg)
        self.assertEqual('First name is required.', fnamerr_msg) #validate error message
        lnamerr_msg = browser.find_element(By.XPATH, regisPage.lname_errmsg).text
        self.assertEqual('Last name is required.', lnamerr_msg) #validate error message
        emailerr_msg = browser.find_element(By.XPATH, regisPage.email_errmsg).text
        self.assertEqual('Email is required.', emailerr_msg) #validate error message
        passerr_msg = browser.find_element(By.XPATH, regisPage.passw_errmsg).text
        self.assertEqual('Password is required.', passerr_msg) #validate error message
        confpassmerr_msg = browser.find_element(By.XPATH, regisPage.confpassw_errmsg).text
        self.assertEqual('Password is required.', confpassmerr_msg) #validate error message
    
    def test_b_wrongemailreg(self):
        print('2. Failed Register wrong email format testcase')
        browser = self.browser
        browser.get(regisPage.url)
        self.assertIn(regisPage.title, self.browser.title) #validate tab title
        browser.find_element(By.ID, regisPage.fname).send_keys(loginData.fName_valid)
        browser.find_element(By.ID, regisPage.lname).send_keys(loginData.lName_valid)
        browser.find_element(By.ID, regisPage.email).send_keys(loginData.email_invalid)
        browser.find_element(By.ID, regisPage.passw).send_keys(loginData.passw_valid)
        browser.find_element(By.ID, regisPage.confpass).send_keys(loginData.passw_valid)
        browser.find_element(By.ID, regisPage.regis_btn).click()
        emailerr_msg = browser.find_element(By.XPATH, regisPage.email_errmsg).text
        print(emailerr_msg)
        self.assertEqual('Wrong email', emailerr_msg) #validate error message

    def test_c_diffpasswreg(self):
        print('4. Failed Register password not match testcase')
        browser = self.browser
        browser.get(regisPage.url)
        self.assertIn(regisPage.title, self.browser.title)
        browser.find_element(By.ID, regisPage.fname).send_keys(loginData.fName_valid)
        browser.find_element(By.ID, regisPage.lname).send_keys(loginData.lName_valid)
        browser.find_element(By.ID, regisPage.email).send_keys(loginData.email_valid)
        browser.find_element(By.ID, regisPage.passw).send_keys(loginData.passw_valid)
        browser.find_element(By.ID, regisPage.confpass).send_keys(loginData.passw_unmatch)
        browser.find_element(By.ID, regisPage.regis_btn).click()
        passerr_msg = browser.find_element(By.XPATH, regisPage.confpassw_errmsg).text
        print(passerr_msg)
        self.assertEqual('The password and confirmation password do not match.', passerr_msg) #validate error message
    
    def test_d_wrgpasswreg(self):
        print('5. Failed Register wrong password format under 6 char testcase')
        browser = self.browser
        browser.get(regisPage.url)
        self.assertIn(regisPage.title, self.browser.title)
        browser.find_element(By.ID, regisPage.fname).send_keys(loginData.fName_valid)
        browser.find_element(By.ID, regisPage.lname).send_keys(loginData.lName_valid)
        browser.find_element(By.ID, regisPage.email).send_keys(loginData.email_valid)
        browser.find_element(By.ID, regisPage.passw).send_keys(loginData.passw_invalid)
        browser.find_element(By.ID, regisPage.regis_btn).click()
        passerr_msg = browser.find_element(By.XPATH, regisPage.passw_errmsg).text
        print(passerr_msg)
        self.assertEqual('The password should have at least 6 characters.', passerr_msg) #validate error message

if __name__ == '__main__':
    unittest.main()