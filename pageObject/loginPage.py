class loginData():
    url = 'https://demowebshop.tricentis.com/login'
    fName_valid = 'Firdaus'
    lName_valid = 'Ali'
    email_valid = 'fird@gmail.com'
    passw_valid = 'firdTAK'
    fName_invalid = ''
    lname_invalid = ''
    email_invalid = 'xxxx.com'
    email_unreg = 'firdaus@gmail.com'
    passw_invalid = '1234'
    passw_unmatch = '12345678'
    city = 'Malang'
    address = 'Simpang Danau Limboto A4'
    zip = '65111'
    phone = '08123456789'

class loginPage():
    url = 'https://demowebshop.tricentis.com/login'
    title = 'Demo Web Shop. Login'
    #id
    email = 'Email'
    passw = 'Password'
    rme = 'RememberMe'
    #xpath
    login_btn = '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input'
    nomail_ermsg = "//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']/div[@class='center-2']/div//form[@action='/login']//div[@class='validation-summary-errors']/span"
    wrgpass_ermsg = "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[1]/div/ul/li"
    noacc_ermsg = "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[1]/div/ul/li"