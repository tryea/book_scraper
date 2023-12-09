from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst

def get_price(txt):
    return float(txt.replace('£', ''))

class BookScraperItem(Item):
    image_path_url = Field(
        output_processor=TakeFirst(),
    )

    price = Field(
        input_processor=MapCompose(get_price),
        output_processor=TakeFirst(),
    )
    title = Field(
        output_processor=TakeFirst(),
    )
    in_stock = Field(
        output_processor=TakeFirst(),
    )
    rating = Field(
        output_processor=TakeFirst(),
    )
