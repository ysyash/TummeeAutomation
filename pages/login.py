from selenium.webdriver.common.by import By


class PageLogIn:
    input_email = (By.ID, 'email')
    input_password = (By.ID, 'pwd')
    btn_login = (By.ID, 'js-auth')
