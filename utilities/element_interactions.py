from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class ElementInteractions:
    @staticmethod
    def click_object(driver, locator):
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(locator)).click()

    @staticmethod
    def input_text(driver, locator, text):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    @staticmethod
    def select_by_option_text(driver, locator, option_text):
        select = Select(WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(locator)))

        select.select_by_visible_text(option_text)

    @staticmethod
    def get_text(driver, locator):
        return WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(locator)).text
