import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient.list_database_names()
print("Folgende Datenbanken sind vorhanden", dblist)

mydb = myclient["mydatabase"]  # neue leere Datenbank angelegt

neuer_inhalt = mydb["customers"]

neuer_datensatz = {"name": "Hans Meier", "Straße": "Schlossallee 10"}
x = neuer_inhalt.insert_one(neuer_datensatz)
