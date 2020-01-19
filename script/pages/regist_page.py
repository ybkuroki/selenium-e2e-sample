#!/usr/local/bin/python3
from selenium.webdriver.common.keys import Keys
from pages import PageObject
from time import sleep

# 登録画面
class RegistPage(PageObject):

    # 新規登録メニューを押下する。
    def click_regist_menu(self):
        self.find_element_by_xpath("//div[contains(@class, 'ui fixed top menu')]/a[contains(@class, 'item')][2]").click()
        sleep(1)

    # 書籍タイトルを入力する。
    def set_title(self, title):
        self.find_element_by_xpath("//div[contains(@class, 'ui modal visible active')]/div[contains(@class, 'content')]/div[contains(@class, 'ui form')]/div[contains(@class, 'field')][1]/input").send_keys(title)

    # ISBNを入力する。
    def set_isbn(self, isbn):
        self.find_element_by_xpath("//div[contains(@class, 'ui modal visible active')]/div[contains(@class, 'content')]/div[contains(@class, 'ui form')]/div[contains(@class, 'field')][2]/input").send_keys(isbn)

    # カテゴリを設定する。
    def set_category(self, category):
        self.find_element_by_xpath("//div[contains(@class, 'ui modal visible active')]/div[contains(@class, 'content')]/div[contains(@class, 'ui form')]/div[contains(@class, 'field')][3]/div[contains(@class, 'ui selection dropdown')]").click()
        sleep(0.5)
        self.find_element_by_xpath("//div[contains(@class, 'menu transition  visible')]/div[contains(text(), '" + category + "')]").click()
        sleep(0.5)
    
    # 形式を設定する。
    def set_format(self, format):
        self.find_element_by_xpath("//div[contains(@class, 'ui modal visible active')]/div[contains(@class, 'content')]/div[contains(@class, 'ui form')]/div[contains(@class, 'field')][4]/div[contains(@class, 'ui selection dropdown')]").click()
        sleep(0.5)
        self.find_element_by_xpath("//div[contains(@class, 'menu transition  visible')]/div[contains(text(), '" + format + "')]").click()
        sleep(0.5)
    
    # 登録ボタンを押下する。
    def click_regist_button(self):
        self.find_element_by_xpath("//div[contains(@class, 'ui modal visible active')]/div[contains(@class, 'actions')]/div[contains(text(), '登録')]").click()
        sleep(5)
