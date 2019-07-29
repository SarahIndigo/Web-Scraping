import scrapy


class QuotetutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page_id = scrapy.Field()
    page_name = scrapy.Field()
    page_country = scrapy.Field()
    page_url = scrapy.Field()

