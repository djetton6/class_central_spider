# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

('//*[@class="head-3 large-up-head-2 text--bold block"]/@href')


class SubjectsSpider(scrapy.Spider):
    name = 'subjects'
    allowed_domains = ['classcentral.com']
    start_urls = ('http://classcentral.com/subjects',)

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
            for subject in subjects:
                yield Request(response.urljoin(subject), callback=self.parse_subject)

    def parse_subject(self, response):
        subject_name = response.xpath('//title').extract_first().split(' | ')[0]
        subject_name = subject_name.split(' | ')
        subject_name = subject_name[0]

        courses = response.xpath('//*[@class="course-name-text text--bold"]')
