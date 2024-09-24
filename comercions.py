import csv
def read_csv(filename):
    with open(filename, mode='r', encoding='ISO-8859-1') as file:
        data = csv.reader(file, delimiter=",")
        names= []
        for row in data:
            names.append(row[5])
        comercialNames = set(names)
        print(comercialNames)

def countfarms(filename):
    with open(filename, mode='r', encoding='ISO-8859-1') as file:
        data = csv.reader(file, delimiter=",")
        farms= []
        for row in data:
            if row[5] == 'Servicios relacionados con la cría y explotación de animales' or row[5] == 'Matanza de ganado, aves y otros animales comestibles':
                farms.append(row[2])
        
        print(farms)
        print(len(farms))

def buscadorkeken(filename):
    with open(filename, mode='r', encoding='ISO-8859-1') as file:
        data = csv.reader(file, delimiter=",")
        farms= []
        for row in data:
            if  "KEK" in row[2]:
                farms.append(row[2])
        
        print(farms)
        print(len(farms))

def typeKeken(filename):
    with open(filename, mode='r', encoding='ISO-8859-1') as file:
        data = csv.reader(file, delimiter=",")
        farms= []
        for row in data:
            if  "RASTRO UMAN KEKEN" in row[2]:
                farms.append(row[5])
        
        print(farms)
        print(len(farms))

def getCoords(filename):
    with open(filename, mode='r', encoding='ISO-8859-1') as file:
        data = csv.reader(file, delimiter=",")
        latitud= ["latitud"]
        longitud= ["longitud"]
        coords = []
        for row in data:
            if row[5] == 'Servicios relacionados con la cría y explotación de animales' or row[5] == 'Matanza de ganado, aves y otros animales comestibles':
                latitud.append(row[39])
                longitud.append(row[40])
        for i in range(len(longitud)):
            coord = [latitud[i], longitud[i]]
            coords.append(coord)
        return coords
    
def buscarTipoDeComercioPorRastros(filename):
        with open(filename, mode='r', encoding='ISO-8859-1') as file:
            data = csv.reader(file, delimiter=",")
            farms= []
            for row in data:
                if  "RASTRO " in row[2]:
                    farms.append(row[5])
            
            print(set(farms))
            print(len(farms))

def buscarNombresRastros(filename):
        with open(filename, mode='r', encoding='ISO-8859-1') as file:
            data = csv.reader(file, delimiter=",")
            farms= []
            for row in data:
                if  "RASTRO " in row[2]:
                    farms.append(row[2])
            
            print(farms)
            print(len(farms))

"""countfarms("denue_inegi_31_.csv")
buscadorkeken("denue_inegi_31_.csv")
typeKeken("denue_inegi_31_.csv")
coords = getCoords("denue_inegi_31_.csv")
print(coords)


# Nombre del archivo
nombre_archivo = 'coords.csv'

# Escribir en el archivo CSV
with open(nombre_archivo, mode='w', newline='', encoding='ISO-8859-1') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(coords)

print(f"Archivo {nombre_archivo} creado y datos escritos correctamente.")"""


buscarNombresRastros("denue_inegi_31_.csv")
