import json

#ruta del archivo
read_json = 'C:\\Users\\rhespinoza\\OneDrive - Logicalis\\Documentos\\Ansible\\Reportes\\20-03-23\\prueba.json'
archivo_json = (read_json)


#Leemos el archivo formato Json
with open(archivo_json) as archivo:
    datos = json.load(archivo)

# print(type(datos), datos)

#Creamos un diccionario vacio
d = {}

#Iteramos los valores Name y Valor, si el Name no esta en d = {} Se agrega NOmbre y Valor en caso contrario se agrega el valor
for item in datos:
    if item["Name"] not in d:
        d[item["Name"]] = str(item["Valor"])
    else:
        d[item["Name"]] = d[item["Name"]] + "-" + str(item["Valor"])

print(d)


#Exportamos el resultado en formato Json
with open(f'C:\\Users\\rhespinoza\\OneDrive - Logicalis\\Documentos\\Ansible\\Reportes\\20-03-23\\data_ospf.json', 'w') as archivo_salida:
    # for i in range(len(resultado)):
        json.dump(d, archivo_salida )
