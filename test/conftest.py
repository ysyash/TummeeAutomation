import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
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

# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#     driver.get(ProdProfile.base_url)
#     driver.maximize_window()
#     driver.set_page_load_timeout(ProdProfile.page_timeout)
#     driver.implicitly_wait(ProdProfile.max_timeout)
#     yield driver
#     driver.quit()

# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     driver.get(ProdProfile.base_url)
#     driver.maximize_window()
#     driver.set_page_load_timeout(ProdProfile.page_timeout)
#     driver.implicitly_wait(ProdProfile.max_timeout)
#     yield driver
#     driver.quit()

