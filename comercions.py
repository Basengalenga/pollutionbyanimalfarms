import csv
def read_csv(filename):
    with open(filename, mode='r', encoding='ISO-8859-1') as file:
        data = csv.reader(file, delimiter=",")
        names= []
        for row in data:
            names.append(row[5])
        comercialNames = set(names)
        print(comercialNames)
read_csv("denue_inegi_31_.csv")
