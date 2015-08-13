# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

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
        el = self.driver.find_element_by_xpath("//button")
        if el:
            el.click()
        self.driver.close()
