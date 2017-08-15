"""
在父级HelloScrapy目录中执行scrapy crawl quotes即可看到效果
"""
import scrapy


class QuotesSpider(scrapy.Spider):
    """quotes"""

    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/'
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as file:
            file.write(response.body)