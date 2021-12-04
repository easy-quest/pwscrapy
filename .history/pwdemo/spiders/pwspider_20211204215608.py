import scrapy


class PwspiderSpider(scrapy.Spider):
    name = 'pwspider'

    def start_requests(self):
        yield scrapy.Req
    
    def parse(self, response):
        pass
