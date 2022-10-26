import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsAllocineItem


class AllocineSpider(scrapy.Spider):
    name = 'allocine'
    allowed_domains = ['www.allocine.fr']
    
    #Liste des pages à collecter
    start_urls = [f'https://www.allocine.fr/film/meilleurs/?page={n}' for n in range(1,10)]


    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_manga)
        
        
    def parse_manga(self, response):
        liste_film = response.css('li.mdl')
        
        
        # Boucle qui parcours l'ensemble des éléments de la liste des films
        for film in liste_film:
            item = ReviewsAllocineItem()

            # Nom du film
            try:
                item['title'] = film.css('div div h2 a::text').extract()[0].strip()
            except:
                item['title'] = 'None'
              
            # Lien de l'image du film
            try:
                item['img'] = film.css('img').attrib['src']#.strip()
            except:
                item['img'] = 'None'


            # Auteur du film
            try:
                item['author'] = film.css('div div div div a.blue-link::text').extract()[0].strip()
            except:
                item['author'] = 'None'
           
            # Durée du film
            try:
                item['time'] = film.css('div div div div::text').extract()[0].strip()
            except:
                item['time'] = 'None'

            # Genre cinématographique
            try:
                item['genre'] = '-'.join(film.css('div div div div.meta-body-info span::text').extract()[1:]).strip()
            except:
                item['genre'] = 'None'

            # Score du film
            try:
                item['score'] = film.css('div div div div.rating-item-content div span.stareval-note::text')[0].extract().strip()
            except:
                item['score'] = 'None'

            # Description du film
            try:
                item['desc'] = film.css('div div div.content-txt::text').extract()[0].strip()
            except:
                item['desc'] = 'None'

            # Date de sortie
            try:
                item['release'] = film.css('div div div div span.date::text').extract()[0].strip()
            except:
                item['release'] = 'None'


            yield item