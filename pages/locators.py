from selenium.webdriver.common.by import By


class BackOfficeLoginPageLocators:
    USER_LOGIN = (By.ID, "input-login")
    USER_PASSWORD = (By.ID, "input-password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".appearance-filled")


class LocationPageLocators:
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, "[routerlink='add']")
    LOCATION_NAME = (By.CSS_SELECTOR, "[formcontrolname='name']")
    SEARCH_ADDRESS = (By.CSS_SELECTOR, "[placeholder='Search address...']")
    BRANCH_FIELD = (By.CSS_SELECTOR, "[formcontrolname='branchId']")
    BRANCH_ELEMENT = (By.CSS_SELECTOR, "nb-option:nth-child(1)")
    REGION_FIELD = (By.CSS_SELECTOR, "[formcontrolname='regionId']")
    REGION_ELEMENT = (By.CSS_SELECTOR, "nb-option:nth-child(2)")
    CITY_FIELD = (By.CSS_SELECTOR, "[formcontrolname='cityId']")
    CITY_ELEMENT = (By.CSS_SELECTOR, "nb-option:nth-child(1)")
    POSTAL_CODE = (By.CSS_SELECTOR, "[formcontrolname='zip']")
    CREATE_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    CREATE_MESSAGE = (By.CSS_SELECTOR, ".content-container")
