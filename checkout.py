import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from pageObject.loginPage import loginData,  loginPage
from pageObject.checkoutPage import checkoutData, cart
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import login

class Checkout(unittest.TestCase):
    
    def setUp(self): #python test method, this cannot be modified (not recognized as testcase)
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_a_successCo(self):
        browser = self.browser
        browser.get(loginPage.url)
        self.assertIn(loginPage.title, self.browser.title) #validate tab title
        login.DemowebShop.test_baseLogin(browser, loginData.email_valid, loginData.passw_valid)
        element_to_hover_over = browser.find_element(By.XPATH, checkoutData.ccomputer)
        hover = ActionChains(browser).move_to_element(element_to_hover_over)
        hover.perform()
        browser.find_element(By.XPATH, checkoutData.scdesktop).click()
        self.assertIn(checkoutData.title_scdesktop, self.browser.title)
        browser.find_element(By.XPATH, checkoutData.product3).click()
        browser.find_element(By.ID, 'product_attribute_74_5_26_82').click()
        browser.find_element(By.ID, 'product_attribute_74_6_27_85').click()
        browser.find_element(By.ID, 'product_attribute_74_3_28_87').click()
        browser.find_element(By.ID, 'product_attribute_74_8_29_88').click()
        browser.find_element(By.ID, 'product_attribute_74_8_29_89').click()
        browser.find_element(By.ID, 'product_attribute_74_8_29_90').click()
        browser.find_element(By.ID, cart.qty_xpath).send_keys('3')
        browser.find_element(By.ID, cart.atc_btn).click()
        browser.implicitly_wait(5)
        browser.find_element(By.XPATH, checkoutData.cart).click()
        price = browser.find_element(By.XPATH, cart.price_xpath).text
        subtotal = browser.find_element(By.XPATH, cart.subtotal_xpath).text
        self.assertEqual(price, subtotal)
        browser.find_element(By.ID, cart.tos).click()
        browser.find_element(By.ID, cart.co_btn).click()
        #browser.find_element(By.ID, 'BillingNewAddress_CountryId').click()
        #browser.find_element(By.XPATH, '//*[@id="BillingNewAddress_CountryId"]/option[100]').click()
        #browser.find_element(By.ID, checkoutData.city_id).send_keys(loginData.city)
        #browser.find_element(By.ID, checkoutData.address1_id).send_keys(loginData.address)
        #browser.find_element(By.ID, checkoutData.zip_id).send_keys(loginData.zip)
        #browser.find_element(By.ID, checkoutData.phone_id).send_keys(loginData.phone)
        browser.find_element(By.XPATH, '//*[@id="billing-buttons-container"]/input').click()
        browser.find_element(By.XPATH, '//*[@id="shipping-buttons-container"]/input').click()
        browser.find_element(By.XPATH, '//*[@id="shipping-method-buttons-container"]/input').click()
        browser.find_element(By.XPATH, '//*[@id="payment-method-buttons-container"]/input').click()
        browser.find_element(By.XPATH, '//*[@id="payment-info-buttons-container"]/input').click()
        browser.find_element(By.XPATH, '//*[@id="confirm-order-buttons-container"]/input').click()
        browser.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/ul/li[2]/a').click()

if __name__ == '__main__':
    unittest.main()