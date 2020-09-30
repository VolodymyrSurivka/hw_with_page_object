import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()