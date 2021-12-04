import scrapy


class PwspiderSpider(scrapy.Spider):
    name = 'pwspider'

    def start_requests(self):
        yield scrapy.Request('https://kubnews.ru/proisshestviya',meta={'playwright': True})
    
    def parse(self, response):
        yield {
            'text': response.text
        }
