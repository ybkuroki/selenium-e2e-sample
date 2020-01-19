#!/usr/local/bin/python3
from selenium.webdriver.common.keys import Keys
from pages import PageObject
from time import sleep

# ログイン画面
class LoginPage(PageObject):

    # ユーザ名を入力する
    def set_user_name(self, username):
        self.find_element_by_xpath("//div[contains(@class, 'field')]/input[@type='text']").send_keys(username)
    
    # パスワードを入力する
    def set_password(self, password):
        self.find_element_by_xpath("//div[contains(@class, 'field')]/input[@type='password']").send_keys(password)
    
    # ログインボタンを押下する
    def click_login_button(self):
        self.find_element_by_xpath("//button").click()
        sleep(1)
