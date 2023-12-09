from scrapy import Item, Field


class BookScraperItem(Item):
    image_path_url = Field()
    price = Field()
    title = Field()
    in_stock = Field()
    rating = Field()
