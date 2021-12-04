import scrapy


class PwspiderSpider(scrapy.Spider):
    name = 'pwspider'

    def start_requests(self):
        yield scrapy.Re
    
    def parse(self, response):
        pass
