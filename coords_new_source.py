import csv
def getHeaders(source):
    with open(source, mode='r', encoding='ISO-8859-1') as file:
        data = csv.reader(file, delimiter=",")
        return next(data)
    

def getCoords(source):
    with open(source, mode='r', encoding='ISO-8859-1') as file:
        data = csv.reader(file, delimiter=",")
        latitud = ["latitud"]
        longitud = ["longitud"]
        next(data)
        for row in data:
            spaceCounter = 0
            latitudIndividual = ""
            longitudIndividual = ""
            for letter in row[1]:
                if letter is " ":
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


headers = getHeaders('data/granjas_peninsula.csv')
print(headers)



latitud, longitud = getCoords('data/granjas_peninsula.csv')



print(latitud, longitud)

coords = [(lat, lon) for lat, lon in zip(latitud, longitud)]


print(coords)


writeCoords('data/coordsgeneral.csv', latitud, longitud)