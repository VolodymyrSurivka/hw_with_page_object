from .pages.login_page import LoginPage
from .pages.location_page import LocationPage
import pytest


@pytest.mark.need_test
class TestAddNewLocation:

    def test_user_can_add_new_location(self, browser):
        bo_login_link = "https://back-office.dev.it-banda.com/login"
        page = LoginPage(browser, bo_login_link)
        page.open()
        page.login_in_bo(login="vladimir.surivka", password="1q2w3e4r")
        retail_software_locations_link = "https://back-office.dev.it-banda.com/retail-software/locations"
        page = LocationPage(browser, retail_software_locations_link)
        page.open()
        page.add_new_location()
