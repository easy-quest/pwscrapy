import scrapy


class PwspiderSpider(scrapy.Spider):
    name = 'pwspider'

    def start_requests(self):
        yield scrapy.Request('https://www.myheritage.com/research')
    
    def parse(self, response):
        pass
