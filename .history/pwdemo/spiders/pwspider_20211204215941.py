import scrapy


class PwspiderSpider(scrapy.Spider):
    name = 'pwspider'

    def start_requests(self):
        yield scrapy.Request('https://www.myheritage.com/research')
        meta=
    
    def parse(self, response):
        pass
