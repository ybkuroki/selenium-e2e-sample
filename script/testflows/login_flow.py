#!/usr/local/bin/python3
from pages import PageObject, LoginPage

# ログイン画面
class LoginFlow():

    # ログイン
    def login(self, driver, username, password, capture):
        login_page = LoginPage()

        login_page.set_driver(driver)

        if capture:
            # ログイン前のキャプチャ取得
            login_page.save_screenshot('1_login')

        # ユーザ名とパスワードに「test」を入力
        login_page.set_user_name(username)
        login_page.set_password(password)

        if capture:
            # ユーザ名とパスワード入力後のキャプチャ取得
            login_page.save_screenshot('2_login_input')

        # ログインボタンを押下する
        login_page.click_login_button()

        if capture:
            # ログインボタンを押下後のキャプチャ取得
            login_page.save_screenshot('3_login_top')
