import scrapy # import this module to use scrapy.Spider for creating spiders
# import this module to use HtmlResponse class for response argument in parse method
from scrapy.http.response.html import HtmlResponse

class BookWithXPathSpider(scrapy.Spider):
    # name of the spider so that we can run it from the terminal 
    # by using `scrapy crawl book`
    name = 'book_with_xpath'

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
        
        book_card_html = response.xpath('//article[@class="product_pod"]')
        print('[BOOK_CARD_HTML]')
        print(book_card_html)
        for book_card in book_card_html:
            # https://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg
            image_path_raw = book_card.xpath('//img/@src').get()
            image_path_url = 'https://books.toscrape.com/' + str(image_path_raw)
            price = book_card.xpath('//p[@class="price_color"]/text()').get()
            title = book_card.xpath('//h3/a/@title').get()
            in_stock = book_card.xpath('//p[@class="instock availability"]').get()
            rating_raw = book_card.xpath('//p[contains(@class, "star-rating")]/@class').get()
            rating = rating_raw.split(' ')[1]
            if in_stock:
                in_stock = True
            else:
                in_stock = False
            
            yield {
                'image_path_url': image_path_url,
                'price': price,
                'title': title,
                'in_stock': in_stock,
                'rating': rating,
            }