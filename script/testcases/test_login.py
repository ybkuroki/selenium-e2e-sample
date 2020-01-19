#!/usr/local/bin/python3
import pytest
import allure
from pages import PageObject
from testflows import LoginFlow
from commons import ResourceLoader
from time import sleep

class TestLogin(object):

    def setup_method(self):
        print('login')
        self.yml = ResourceLoader.get_instance().get_object()
        self.page_object = PageObject()
        self.page_object.connect_chrome_browser()
        self.driver = self.page_object.get_driver()

    @allure.epic('sample')
    @allure.feature('login')
    @allure.story('success')
    def test_login_success(self):
        """login success testcase"""
        self.page_object.get(self.yml['url'])
        sleep(1)

        login_flow = LoginFlow()
        login_flow.login(self.driver, self.yml['username'], self.yml['password'], True)
        assert self.page_object.is_exist_element("//div[contains(@class, 'ui fixed top menu')]/a[contains(text(), '新規登録')]")

    def teardown_method(self):
        self.page_object.close_browser()
