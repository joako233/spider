import scrapy
import json
import time
from fiverr.items import ItemsFiver


class FivSpider(scrapy.Spider):
    name = "fiv"
    allowed_domains = ["en.wheelsage.org"]
    start_urls = ["https://en.wheelsage.org/api/brands"]
    
    def parse(self, response):
        lista = json.loads(response.body)
        items = lista.get('items')
        
        for item in items:
            for i in item:
                marcas = i.get('brands')
                for m in marcas:

                    id = m.get('id')
                    url = f'https://en.wheelsage.org/api/brands/{id}/sections'
        
                    yield response.follow(url,callback=self.analizando)
                    # return
                  
    dicc = {}
    identidades = {}
    links = {}
    def analizando(self,response):

        lista = json.loads(response.body)

        fi = ItemsFiver()

    
        for l in lista:
            cat = l.get('name')
            if cat is not None:
                if 'catalogue' in cat:
                    seccion = l.get('name').split('/')[2]
            else:
                seccion = 'Cars'

            grupos = l.get('groups')
      
            for g in grupos:
        
                if g.get('item_id'):
              
                    la_id = g.get('item_id')

                    nombre = g.get('name')
                    routers = g.get('routerLink')
                    marca = routers[1]
                    nueva_url = f'https://en.wheelsage.org/api/item/{la_id}?fields=name_html,preview_pictures.picture.name_text'
        
                    if marca in self.links and marca in self.dicc:
                        link = self.links[marca]
                        compañia = self.dicc[marca]

                        if  compañia == 'ACTIVA':
                            fi["Sección"] = seccion
                            fi["Marca"] = marca
                            fi["Nombre"] = nombre
                            fi["Actividad"] = compañia
                            fi['Links'] = link
                            
                            yield fi
                            
                            # yield {'Seccion':seccion,'Marca':marca,'Nombre':nombre,'Actividad':compañia,'Links':link}
                        else:
                            yield response.follow(nueva_url,callback=self.sacando_identity,meta={'marca':marca,'nombre':nombre,'seccion':seccion})
        

                    else:
    
                        yield response.follow(nueva_url,callback=self.sacando_identity,meta={'marca':marca,'nombre':nombre,'seccion':seccion})
          
                
    def sacando_identity(self,response):
        diccionario = json.loads(response.body)
        fi = ItemsFiver()
        nombre = response.meta['nombre']
        marca = response.meta['marca']
        seccion = response.meta['seccion']

        año_compañia = diccionario.get('name_html')

      
        if 'pr.' in año_compañia:
            compañia = 'ACTIVA'
            self.dicc[marca] = compañia
        else:
            compañia = ''
        
        if compañia == '':
            preview_pictures = diccionario.get('preview_pictures')
        
            pictures = preview_pictures.get('pictures')
        
            for p in pictures:
                if p is not None:
                    nomb = p.get('picture').get('name_text')
              
                    if 'pr.' in nomb:
                        compañia = 'ACTIVA'
                        self.dicc[marca] = compañia
                        print(nomb)
                        break

            

        if marca in self.links:
            link = self.links[marca]

            fi["Sección"] = seccion
            fi["Marca"] = marca
            fi["Nombre"] = nombre
            fi["Actividad"] = compañia
            fi['Links'] = link

            yield fi

            # yield {'Seccion':seccion,'Marca':marca,'Nombre':nombre,'Actividad':compañia,'Links':link}
        else:
            lista_pictures = diccionario.get('preview_pictures').get('pictures')
        
            identity = None
            for picture in lista_pictures:
                if picture is None:
                    continue

                identity = picture.get('picture').get('identity')
                if identity != None:
                    self.identidades[marca] = identity
                    break

            url_link = f'https://en.wheelsage.org/api/picture?identity={identity}&fields=of_links'
                    
            yield response.follow(url_link,callback=self.sacando_link,meta={'seccion':seccion,'marca':marca,'nombre':nombre,'actividad':compañia})

           
    def sacando_link(self,response):

        diccionario = json.loads(response.body)
        fi = ItemsFiver()
        nombre = response.meta['nombre']
        marca = response.meta['marca']
        seccion = response.meta['seccion']
        actividad = response.meta['actividad']
        

        lista_pictures = diccionario.get('pictures')
        links = "".strip()
        for p in lista_pictures:
            lista_links = p.get('of_links')
            for link in lista_links:
                links = links + link.get('url') + " "

        if marca not in self.links:
            self.links[marca] = links

     
        fi["Sección"] = seccion
        fi["Marca"] = marca
        fi["Nombre"] = nombre
        fi["Actividad"] = actividad
        fi['Links'] = links

        yield fi
        # yield {'Seccion':seccion,'Marca':marca,'Nombre':nombre,'Actividad':actividad,'Links':links}

        
                   
        
                       
    

            


        
   
    

        

