import pytest
from selenium import webdriver
from Library.config import Config
from selenium.webdriver.firefox.options import Options


@pytest.fixture(params=["firefox","chrome", "edge"])
def init_driver(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=Config.CHROME_PATH)

    elif browser == "edge":
        driver = webdriver.Edge(executable_path=Config.EDGE_PATH)

    elif browser == "firefox":

        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox(executable_path=Config.FIREFOX_PATH, options=options)


    driver.implicitly_wait(30)
    driver.get(Config.URL)
    driver.maximize_window()
    yield driver
    driver.close()
