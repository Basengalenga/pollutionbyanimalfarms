import csv

def readFile(source):                                                           #Source es la ubicacion del archivo en el sistema
    with open(source, mode='r', encoding='ISO-8859-1') as file:
        data = list(csv.reader(file, delimiter=","))
        return data
    
def yucatanización(data):                                       #Filtra los datos de Yucatán
    yucatanData = []
    for row in data:
        if "Yuc" in row[2]:                                    #row[2] indica el estado
            yucatanData.append(row)
    return yucatanData

def pollificación(data):
    chickenData = []
    for row in data:
        if "colas" in row[-3]:                                 #row[-3] indica el tipo de granja, colas es de avícolas, lo modifiqué por el acento
            chickenData.append(row)
    return chickenData

def cerdificación(data):
    porkData = []
    for row in data:
        if "porcinas" in row[-3]:                               #row[-3] indica el tipo de granja
            porkData.append(row)
    return porkData

def getCoords(data):
        latitud = ["latitud"]
        longitud = ["longitud"]

        for row in data:
            spaceCounter = 0
            latitudIndividual = ""
            longitudIndividual = ""
            for letter in row[1]:                             #row[1] ahí se ubican las coordenadas
                if letter == " ":
                    spaceCounter += 1
                if spaceCounter < 2:
                    if letter in "-1234567890.":
                        longitudIndividual += letter
                else:
                    if letter in "-1234567890.":
                        latitudIndividual += letter
            latitud.append(latitudIndividual)
            longitud.append(longitudIndividual)
        return latitud, longitud

    
def writeCoords(source, latitud, longitud):
    coords = [(lat, lon) for lat, lon in zip(latitud, longitud)]
    with open(source, mode='w', newline='', encoding='ISO-8859-1') as file:
        writer = csv.writer(file)
        writer.writerows(coords)
    print(f"Archivo en {source} creado con éxito")

#Getting data

generalData = readFile('data/granjas_peninsula.csv')

yucatanData = yucatanización(generalData)

yucatanPorkData = cerdificación(yucatanData)

yucatanChickenData = pollificación(yucatanData)


#Getting coords

yucatanLatitud, yucatanLongitud = getCoords(yucatanData)

yucatanChickenLatitud, yucatanChickenLongitud = getCoords(yucatanChickenData)

yucatanPorkLatitud, yucatanPorkLongitud = getCoords(yucatanPorkData)

#writing on csv's

writeCoords('data/coordsyucatan.csv', yucatanLatitud, yucatanLongitud)
writeCoords('data/yucatanPorkCoords.csv', yucatanPorkLatitud, yucatanPorkLongitud)
writeCoords('data/yucatanChickenCoords.csv', yucatanChickenLatitud, yucatanChickenLongitud)