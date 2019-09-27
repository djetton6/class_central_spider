# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider


class SubjectsSpider(scrapy.Spider):
    name = 'subjects'
    allowed_domains = ['class-central.com']
    start_urls = ['http://class-central.com/subjects']

    def parse(self, response):
        pass
