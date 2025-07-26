# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CourtlistenerRagItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    case_title = scrapy.Field()
    court_name = scrapy.Field()
    docket_number = scrapy.Field()
    citations = scrapy.Field()
    judges = scrapy.Field()
    opinion_author = scrapy.Field()
    opinion_text = scrapy.Field()
