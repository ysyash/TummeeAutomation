from selenium.webdriver.common.by import By


class PageUser:
    a_builder = (By.XPATH, '(//a[text()="Builder"])[1]')

    btn_create_sequence = (By.ID, 'createSequenceGetStarted')

    input_sequence_title = (By.ID, 'txtSequenceTitle')

    select_yoga_type = (By.ID, 'js-yoga-type')
