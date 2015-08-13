# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StatusSpider(scrapy.Spider):
    name = "status"
    # allowed_domains = ["www.twitter.com"]
    # start_urls = (
    #     'http://www.www.twitter.com/',
    # )
    allowed_domains = ["http://localhost:8080"]
    start_urls = ['http://localhost:8080']

    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(response.url)
        el = self.driver.find_element_by_xpath("//button[contains(@class, 'main-butt')]")
        if el:
            el.click()
        form = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "fill-me-in"))
        )
        form.send_keys("hello world")

        # self.driver.close()
