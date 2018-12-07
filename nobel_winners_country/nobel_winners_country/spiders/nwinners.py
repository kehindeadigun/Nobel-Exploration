
import scrapy
import re

#from nwinner.items import NWinnerItem 

class NWinner(scrapy.Spider):
    """"Scrapes the country and link text of the Nobel-winners."""
    
    name = 'nwinners_list'
    allowed_domains = ['en.wikipedia.org']
    start_urls = [
        "https://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_country"
    ]
    
    def parse(self, response):
        h3s = response.xpath('//h3')
        
        for h3 in h3s: #find the h3 headers with user countries
            country = h3.xpath('span[@class="mw-headline"]/text()')[0].extract()
            winners = h3.xpath('following-sibling::ol[1]') #find the ordered list which is a sibling of said headers
            
            for winner in winners.xpath('li'): #search through the ordered list of winners
                text = winner.xpath('descendant-or-self::text()').extract() #extract winner data
                yield NWinnerItem(
                    country = country[0], 
                    name = text[0],
                    link_text = ' '.join(text)
                )