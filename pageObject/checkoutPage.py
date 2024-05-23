class checkoutData():
    url_scdesktop = 'https://demowebshop.tricentis.com/desktops'
    title_scdesktop = 'Demo Web Shop. Desktops'
    
    
    #id
    city_id = 'BillingNewAddress_City'
    address1_id ='BillingNewAddress_Address1'
    zip_id = ''
    phone_id = ''
    #xpath
    ccomputer = '/html/body/div[4]/div[1]/div[2]/ul[1]/li[2]/a'
    scdesktop = '/html/body/div[4]/div[1]/div[2]/ul[1]/li[2]/ul/li[1]/a'
    product3 = '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[3]/div/div[1]'

class cart():
    #id
    tos = 'termsofservice'
    co_btn = 'checkout'
    countrydd_xpath = 'BillingNewAddress_CountryId'

    #xpath
    qty_xpath = '//*[@id="addtocart_74_EnteredQuantity"]'
    atc_btn = 'add-to-cart-button-74'
    price_xpath = '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/table/tbody/tr/td[6]/span[2]'
    subtotal_xpath = '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[2]/span/span'
    
    con_btn = '//*[@id="billing-buttons-container"]/input'