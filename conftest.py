
import pytest
from  selenium import webdriver
from utils import login
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def fixtureDriver():
    
    misOptions= Options()
    misOptions.add_argument("--incognito")
    
    driver = webdriver.Chrome(options= misOptions)
    driver.implicitly_wait(5) 
    yield driver
    driver.quit()


@pytest.fixture
def login_in_driver(fixtureDriver):
    login(fixtureDriver)
    return fixtureDriver
    