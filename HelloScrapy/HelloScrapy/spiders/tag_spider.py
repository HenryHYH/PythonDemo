import scrapy


class TagSpider(scrapy.Spider):
    name = 'tag'

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first().strip(),
                'author':
                quote.css("small.author::text").extract_first().strip()
            }

        next_page = response.css("li.next a::attr(href)").extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
