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
countfarms("denue_inegi_31_.csv")
buscadorkeken("denue_inegi_31_.csv")
typeKeken("denue_inegi_31_.csv")
