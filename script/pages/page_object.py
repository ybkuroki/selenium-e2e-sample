#!/usr/local/bin/python3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import datetime
import allure

# ページオブジェクトクラス
class PageObject(object):

    # Chrome Headlessブラウザに接続
    def connect_chrome_browser(self):
        self.driver = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    # driverを取得する
    def get_driver(self):
        return self.driver

    # driverを設定する
    def set_driver(self, driver):
        self.driver = driver

    # ブラウザアクセス
    def get(self, url):
        self.driver.get(url)

    # XpathによるDOM要素取得
    def find_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # Xpathによる単一のDOM要素取得
    def find_element(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    # Xpathによる複数のDOM要素取得
    def find_elements(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)

    # 指定した要素の親要素を取得
    def find_parent_element(self, element):
        return element.find_element_by_xpath('..')

    # 指定した要素数を返す
    def get_count_elements(self, xpath):
        return len(self.find_elements(xpath))

    # 指定した要素が存在するかどうか
    def is_exist_element(self, xpath):
        if self.get_count_elements(xpath) > 0:
            return True
        else:
            return False

    # スクリーンショット取得
    def save_screenshot(self, filename):
        # スクリーンショットのファイル名用に日付を取得
        dt = datetime.datetime.today()
        dtstr = dt.strftime("%Y%m%d%H%M%S")
        self.driver.save_screenshot('/tmp/allure-results/images/' + filename + '_' + dtstr + '.png')
        allure.attach.file('/tmp/allure-results/images/' + filename + '_' + dtstr + '.png', attachment_type=allure.attachment_type.PNG)
    
    # ブラウザを閉じる
    def close_browser(self):
        self.driver.close()
        self.driver.quit()
