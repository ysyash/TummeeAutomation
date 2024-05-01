import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from profiles.prodprofile import ProdProfile


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(ProdProfile.base_url)
    driver.maximize_window()
    driver.set_page_load_timeout(ProdProfile.page_timeout)
    driver.implicitly_wait(ProdProfile.max_timeout)
    yield driver
    driver.quit()

