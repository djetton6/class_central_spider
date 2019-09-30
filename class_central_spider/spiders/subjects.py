# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

('//*[@class="head-3 large-up-head-2 text--bold block"]/@href')


class SubjectsSpider(scrapy.Spider):
    name = 'subjects'
    allowed_domains = ['class-central.com']
    start_urls = ('http://class-central.com/subjects',)

    def __init__(self, subject=None):
        self.subject = subject

    def parse(self, response):
        if self.subject:
            subject_url = response.xpath(
                '//*[contains(@title, "' + self.subject + '")]/@href').extract_first()
            yield Request(response.urljoin(subject_url), callback=self.parse_subject)
        else:
            self.logger.info('Scraping all subjects')
            subjects = response.xpath(
                '//*[@class="text--blue"]/@href').extract()

    def parse_subject(self, response):
        pass
