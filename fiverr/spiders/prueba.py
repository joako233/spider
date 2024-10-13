marcas = ['Mercedes','BMW','Toyota','Lunik','Mercedes','BMW']

diccionario = {}


for marca in marcas:
    if marca in diccionario:
        continue
    else:
        diccionario[marca] = 'ACTIVA'

print(diccionario)