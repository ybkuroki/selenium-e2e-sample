#!/usr/local/bin/python3
from pages import PageObject, RegistPage

# 登録画面
class RegistFlow():

    # 登録
    def regist(self, driver, title, isbn, category, format):
        regist_page = RegistPage()

        regist_page.set_driver(driver)

        regist_page.click_regist_menu()

        # ユーザ名とパスワード入力後のキャプチャ取得
        regist_page.save_screenshot('3_regist')

        regist_page.set_title(title)

        regist_page.set_isbn(isbn)
        
        regist_page.set_category(category)
        
        regist_page.set_format(format)
        
        # ユーザ名とパスワード入力後のキャプチャ取得
        regist_page.save_screenshot('4_regist_input')

        regist_page.click_regist_button()

        # ユーザ名とパスワード入力後のキャプチャ取得
        regist_page.save_screenshot('5_regist_success')


