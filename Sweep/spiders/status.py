# -*- coding: utf-8 -*-
import config

import time
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StatusSpider(scrapy.Spider):
    name = "status"
    allowed_domains = ["www.twitter.com"]
    start_urls = ['http://www.twitter.com/']

    # TEST PAGE
    # allowed_domains = ["http://localhost:8080"]
    # start_urls = ['http://localhost:8080']

    def __init__(self, statuses=[]):
        self.driver = webdriver.Chrome()
        self.statuses = statuses

    def parse(self, response):
        self.login(response)
        self.wait_for(self.page_has_loaded)
        self.retweet_statuses()
        # self.driver.close()

    def login(self, response):
        self.driver.get(response.url)
        self.set_old_page()
        email_form = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'signin-email')]"))
        )
        password_form = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'signin-password')]"))
        )
        email_form.send_keys(config.account['email'])
        password_form.send_keys(config.account['password'])
        login_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'flex-table-btn')]")
        if login_button:
            login_button.click()

    def retweet_statuses(self):
        # self.driver.get(self.status_url(self.statuses[0]))

        for s in self.statuses:
            # self.wait_for(self.page_has_loaded)
            self.driver.get(self.status_url(s))
            retweet_button = self.driver.find_element(By.CSS_SELECTOR, ".opened-tweet .Icon--retweet")
            if retweet_button:
                retweet_button.click()
                time.sleep(0.5) # wait for modal
                action_button = self.driver.find_element(By.CSS_SELECTOR, ".retweet-action")
                if action_button:
                    action_button.click()

    def status_url(self, status):
        # TODO: Might be able to get URL from Status class
        return "http://www.twitter.com/%s/status/%s" % (status['user'], status['id'])

    def set_old_page(self):
        self.old_page = self.driver.find_element_by_tag_name('html')

    def page_has_loaded(self):
        # TODO: Find out what class these find_by methods return
        new_page = self.driver.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id

    def wait_for(self, condition_function):
        start_time = time.time()
        while time.time() < start_time + 3:
            if condition_function():
                return True
            else:
                time.sleep(0.1)
        raise Exception(
            'Timeout waiting for {}'.format(condition_function.__name__)
        )


# EXAMPLES
# el = self.driver.find_element_by_xpath("//button[contains(@class, 'main-butt')]")
# if el:
#     el.click()
# form = WebDriverWait(self.driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "fill-me-in"))
# )
# form.send_keys("hello world")
# retweet_button = $('span.Icon--retweet')[0]
# follow_button = $('button.user-actions-follow-button')