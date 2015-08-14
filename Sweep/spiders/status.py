# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config

class StatusSpider(scrapy.Spider):
    name = "status"
    allowed_domains = ["www.twitter.com"]
    start_urls = ['http://www.twitter.com/']
    # allowed_domains = ["http://localhost:8080"]
    # start_urls = ['http://localhost:8080']

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self, response):
        self.driver.get(response.url)
        email_form = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'signin-email')]"))
        )
        password_form = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'signin-password')]"))
        )
        email_form.send_keys(config.account['email'])
        password_form.send_keys(config.account['password'])
        login_button = self.driver.find_element_by_xpath("//button[contains(@class, 'flex-table-btn')]")
        if login_button:
            login_button.click()

    def parse(self, response):
        self.login(response)
        # self.driver.close()


# NOTES
# input#signin-email
# input#signin-password
# button.flex-table-btn

# EXAMPLES
# el = self.driver.find_element_by_xpath("//button[contains(@class, 'main-butt')]")
# if el:
#     el.click()
# form = WebDriverWait(self.driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "fill-me-in"))
# )
# form.send_keys("hello world")