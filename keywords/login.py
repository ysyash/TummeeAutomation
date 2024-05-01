from pages.login import PageLogIn
from utilities.element_interactions import ElementInteractions


class LogIn:
    @staticmethod
    def log_in(driver, username, password):
        ElementInteractions.input_text(driver, PageLogIn.input_email, username)

        ElementInteractions.input_text(driver, PageLogIn.input_password, password)

        ElementInteractions.click_object(driver, PageLogIn.btn_login)