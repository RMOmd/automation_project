import pytest
from config.data import Data
from pages.login_page import  LoginPage
from pages.personal_page import PersonalPage
from pages.dashboard import DashboardPage


class BaseTest:

    data: Data

    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage()
        request.cls.dashboard_page = DashboardPage()
        request.cls.personal_page = PersonalPage()
