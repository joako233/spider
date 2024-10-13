# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class FiverrPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)
        field_names = adapter.field_names()

        for field_name in field_names:
            # print("Eston son los field names:",field_name)
            if field_name == 'Sección':
                valor = adapter.get('Sección')
                adapter[field_name] = valor[0].upper() + valor[1:]
            if field_name == 'Marca':
                total = ""
                if adapter.get('Marca') == "volkswagen_aktiengesellschaft":
                    valor = "volkswagen"
                else:
                    valor = adapter.get('Marca')
           
                if "_" in valor:
                    palabras = valor.split("_")
            
                    for p in palabras:
                        nueva = p[0].upper() + p[1:]
                        total = total + " "+nueva
                    total = total.strip()
                elif "-" in valor:
                    palabras = valor.split("-")
            
                    for p in palabras:
                        nueva = p[0].upper() + p[1:]
                        total = total + " "+nueva
                    total = total.strip()
                else:
                    total = valor[0].upper() + valor[1:]

                adapter[field_name] = total
            
            if field_name == 'Links':
                marca = adapter.get('Marca')
                
                if "_" in marca:
                    palabras = marca.split("_")
            
                    # marca = "".join(palabras)
        
                elif "-" in marca:
                    palabras = marca.split("-")
            
                    # marca = "".join(palabras)
                else:
                    palabras = [marca]
                
                links = adapter.get('Links').split(" ")
                link_elegido = ""
                
                for link in links:
                    for palabra in palabras:
                        if palabra in link and link not in link_elegido:
                            link_elegido = (link_elegido + " " + link).strip()
                     
        
                if link_elegido == "":
                    for link in links:
                        link_elegido = (link_elegido + " " + link).strip()

                if link_elegido == "":
                    link_elegido = 'LINK NO DISPONIBLE'
                adapter[field_name] = link_elegido
                # print(f"La marca es {marca}")
                # print(f"El link es {link_elegido}")

        ordered_item = {
            'Sección': item.get('Sección'),
            'Marca': item.get('Marca'),
            'Nombre': item.get('Nombre'),
            'Actividad': item.get('Actividad'),
            'Links': item.get('Links')
        }
        
        return ordered_item
       

   
      



