#!/usr/local/bin/python3
import pytest
import allure
from pages import PageObject
from testflows import LoginFlow, RegistFlow
from commons import ResourceLoader
from time import sleep

class TestRegist(object):

    def setup_method(self):
        self.yml = ResourceLoader.get_instance().get_object()
        self.page_object = PageObject()
        self.page_object.connect_chrome_browser()
        self.driver = self.page_object.get_driver()

        self.page_object.get(self.yml['url'])
        sleep(1)

        login_flow = LoginFlow()
        login_flow.login(self.driver, self.yml['username'], self.yml['password'], False)
        sleep(1)

    @allure.epic('sample')
    @allure.feature('regist')
    @allure.story('success')
    def test_regist_success(self):
        """regist success testcase"""
        regist_flow = RegistFlow()
        regist_flow.regist(self.driver, "テスト1", "123-234-345-1", "雑誌", "電子書籍")
        assert self.page_object.is_exist_element("//a[contains(text(), 'テスト1')]")

    def teardown_method(self):
        self.page_object.close_browser()
