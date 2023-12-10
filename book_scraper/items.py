from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst

def get_price(txt):
    return float(txt.replace('£', ''))

def get_rating(txt):
    if(txt == 'One'):
        return 1
    elif(txt == 'Two'):
        return 2
    elif(txt == 'Three'):
        return 3
    elif(txt == 'Four'):
        return 4
    elif(txt == 'Five'):
        return 5

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
        input_processor=MapCompose(get_rating),
        output_processor=TakeFirst(),
    )
