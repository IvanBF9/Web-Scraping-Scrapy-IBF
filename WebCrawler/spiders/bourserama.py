import scrapy


class BourseramaSpider(scrapy.Spider):
    name = 'bourserama'
    allowed_domains = ['www.boursorama.com']
    start_urls = ['http://www.boursorama.com/']

    def parse(self, response):
        pass
