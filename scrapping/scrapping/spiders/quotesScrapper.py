import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'paste the url here'
    ]

    def parse(self, response):

        items = QuotetutorialItem()

        all_div_quotes = response.css('table')
        print(all_div_quotes)

        for quotes in all_div_quotes:

            page_id = quotes.css('i.item-count::text').extract()

            page_name = quotes.css('span.show-name::text').extract()
            #print("page_name", page_name)
            page_country = quotes.css('span.show-country::text').extract()
            #print("page_country", page_country)
            page_url = quotes.css('div.item a::attr(href)').extract()
            #print("page_url", page_url)

            items['page_id'] = page_id
            items['page_name'] = page_name
            items['page_country'] = page_country
            items['page_url'] = page_url

            yield items

        next_page = response.css('div.more-center-link a::attr(href)').get()

	#to go through all the following link "next" in this case
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
