class regisPage():
    url = 'https://demowebshop.tricentis.com/register'
    title = 'Demo Web Shop. Register'
    #id
    gender = 'gender-male'
    fname = 'FirstName'
    lname = 'LastName'
    email = 'Email'
    passw = 'Password'
    confpass = 'ConfirmPassword'
    regis_btn = 'register-button'
    #xpath
    fname_errmsg = "/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[2]/span[2]/span"
    lname_errmsg = "/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[3]/span[2]/span"
    email_errmsg = "/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[4]/span[2]/span"
    passw_errmsg = "/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div[1]/span[2]/span"
    confpassw_errmsg = "/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div[2]/span[2]/span"