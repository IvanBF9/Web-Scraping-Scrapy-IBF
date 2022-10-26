import scrapy
from scrapy import Request
from WebCrawler.items import BoursoramaItem
import time

class BoursoramaSpider(scrapy.Spider):
    name = 'boursorama'
    allowed_domains = ['finance.yahoo.com', 'www.boursorama.com']
    start_urls = ['https://www.boursorama.com/bourse/actions/palmares/france/page-1?france_filter%5Bmarket%5D=1rPCAC', 'https://www.boursorama.com/bourse/actions/palmares/france/page-2?france_filter%5Bmarket%5D=1rPCAC']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_boursorama)
            
    def parse_boursorama(self, response):
        liste_indices = response.css('tr.c-table__row')[1:]
        
        for indices in liste_indices:
            item = BoursoramaItem()
            
            #indice boursier
            try: 
              item['indice'] = indices.css('div div a::text').extract()[0]
            except:
              item['indice'] = 'None'
            
            #indice cours de l'action
            try: 
              item['cours'] = indices.css('td span::text').extract()[1]
            except:item['cours'] = 'None'
            
            #Variation de l'action
            try: 
              item['var'] = indices.css('td span::text').extract()[2]
            except:
              item['var'] = 'None'
            
            #Valeur la plus haute
            try: 
              item['hight'] = indices.css('td span::text').extract()[4]
            except:
              item['hight'] = 'None'
            
            #Valeur la plus basse
            try: 
              item['low'] = indices.css('td span::text').extract()[5]
            except:
              item['low'] = 'None'

            #Valeur d'ouverture
            try: 
              item['open_'] = indices.css('td span::text').extract()[3]
            except:
              item['open_'] = 'None'

            #Date de la collecte
            try: 
              # Time in ms
              item['time'] = round(time.time() * 1000)
            except:
              item['time'] = 'None'

            
            yield item