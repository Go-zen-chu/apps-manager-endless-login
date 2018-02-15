# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os, argparse, pickle, time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def login_apps_manager_quit(driver, url, user, cred):
    driver.get(url)
    time.sleep(3)
    username = driver.find_element_by_xpath("//input[@name='username']")
    username.send_keys(user)
    passwd = driver.find_element_by_xpath("//input[@name='password']")
    passwd.send_keys(cred)
    time.sleep(1)

    signin = driver.find_element_by_xpath("//input[@type='submit']")
    signin.click()

if __name__ == '__main__':
    # プラットフォームごとのdriverを用いる
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--driver', choices=["chrome", "phantomjs"], default='chrome')
    parser.add_argument('--height', default=1000)
    parser.add_argument('--width', default=680)
    args = parser.parse_args()

    # driver の作成 (chrome はデバッグ用)
    if args.driver == "phantomjs":
        user_agent = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) " +
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"
        )
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = user_agent
        driver = webdriver.PhantomJS(desired_capabilities=dcap)
    else:
        driver = webdriver.Chrome("driver/darwin/chromedriver")
    driver.set_window_size(args.width, args.height)

    access_url = "your apps manager url"
    user = "user"
    cred = "password" # changeme
    cnt = 1
    login_apps_manager_quit(driver, access_url, user, cred)
    while True:
        print("Refreshing apps manager : ", cnt)
        time.sleep(20)
        driver.refresh()
        cnt += 1
