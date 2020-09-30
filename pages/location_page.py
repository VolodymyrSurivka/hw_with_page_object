from .login_page import LoginPage
from .locators import LocationPageLocators
from selenium.webdriver.common.keys import Keys
import time


class LocationPage(LoginPage):

    def add_new_location(self):
        add_new_button = self.browser.find_element(*LocationPageLocators.ADD_NEW_BUTTON)
        add_new_button.click()
        location_name = self.browser.find_element(*LocationPageLocators.LOCATION_NAME)
        location_name.send_keys("Autotest3")
        search_address = self.browser.find_element(*LocationPageLocators.SEARCH_ADDRESS)
        search_address.send_keys("Saperne Pole Street, 14/55, Kyiv, Ukraine")
        search_address.send_keys(Keys.ENTER)
        location_branch_field = self.browser.find_element(*LocationPageLocators.BRANCH_FIELD)
        location_branch_field.click()
        location_branch_element = self.browser.find_element(*LocationPageLocators.BRANCH_ELEMENT)
        location_branch_element.click()
        location_region_field = self.browser.find_element(*LocationPageLocators.REGION_FIELD)
        location_region_field.click()
        location_region_element = self.browser.find_element(*LocationPageLocators.REGION_ELEMENT)
        location_region_element.click()
        location_city_field = self.browser.find_element(*LocationPageLocators.CITY_FIELD)
        location_city_field.click()
        location_city_element = self.browser.find_element(*LocationPageLocators.CITY_ELEMENT)
        location_city_element.click()
        location_postal_code_field = self.browser.find_element(*LocationPageLocators.POSTAL_CODE)
        location_postal_code_field.send_keys("112233")
        create_button = self.browser.find_element(*LocationPageLocators.CREATE_BUTTON)
        create_button.click()
        # WebDriverWait(browser, 5).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, ".appearance-filled"))).click()
        create_message = self.browser.find_element(*LocationPageLocators.CREATE_MESSAGE)
        time.sleep(1)
        assert "Error occurred while creating the location" in create_message.text, "Location was created successfully"
        # assert "Location was created successfully" in message.text, "Location with this name already exists"
