import scrapy # import this module to use scrapy.Spider for creating spiders
# import this module to use HtmlResponse class for response argument in parse method
from scrapy.http.response.html import HtmlResponse

class BookSpider(scrapy.Spider):
    # name of the spider so that we can run it from the terminal 
    # by using `scrapy crawl book`
    name = 'book'

    # start_urls attribute contains a list of URLs that will be used
    # for the spider to begin crawling from.
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response: HtmlResponse): 
        '''
        The parse method is in charge of processing the response and
        returning scraped data and/or more URLs to follow.

        parse method will be called automatically by scrapy after making
        a request to the start_urls.

        response parameter is an instance of TextResponse that holds the
        page content of the URLs we requested and has further helpful methods to handle it.
        '''
        print("[ OUR RESPONSE ]")
        print(response)