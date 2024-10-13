# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy


class ItemsFiver(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    Sección = scrapy.Field()
    Marca = scrapy.Field()
    Nombre = scrapy.Field()
    Actividad = scrapy.Field()
    Links = scrapy.Field()


    