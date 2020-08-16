import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MoviesSpider(CrawlSpider):
    name = 'movies'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//td[@class='titleColumn']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'year': response.xpath("//span[@id='titleYear']/a/text()").get(),
            'rating': response.xpath("//span[@itemprop='ratingValue']/text()").get(),
            'genre': response.xpath("(//div[@class='subtext']/a)[1]/text()").get(),
            'time': response.xpath("normalize-space((//time)[1]/text())").get(),
            'url': response.url
        }
