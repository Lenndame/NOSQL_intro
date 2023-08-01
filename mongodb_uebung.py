import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# ---------------------------------------------------------
# Aufgabe 1
# ---------------------------------------------------------
mydb = myclient["Pferde"]

# ---------------------------------------------------------
# Aufgabe 2
# ---------------------------------------------------------
inhalt_pferd = mydb["Großbritannien"]

# ---------------------------------------------------------
# Aufgabe 3
# ---------------------------------------------------------
inhalt_pferd.insert_one(
    {"Name": "SHAGYA",
        "Rasse": "ARABER",
        "Stockmaß": "156 cm",
        "Intelligenz": "2",
        "Geschwindigkeit": "60 km/h",
        "Preis": "10.000 Euro"}
)

# ---------------------------------------------------------
# Aufgabe 4
# ---------------------------------------------------------
many_pferde = (
    {"Name": "Schwedisches Warmblut",
        "Stockmaß": "168 cm",
        "Intelligenz": "4",
        "Geschwindigkeit": "56 km/h",
        "Preis": "9.000 Euro"},
    {"Name": "Württemberger",
        "Stockmaß": "165 cm",
        "Intelligenz": "2",
        "Geschwindigkeit": "55 km/h",
        "Preis": "8.000 Euro"},
    {"Name": "Noriker",
        "Stockmaß": "172 cm",
        "Intelligenz": "1",
        "Geschwindigkeit": "40 km/h",
        "Preis": "6.000 Euro"}
)

inhalt_pferd.insert_many(many_pferde)

# ---------------------------------------------------------
# Aufgabe 5
# ---------------------------------------------------------
value_pferd = {"SHAGYA": "Hofgut Allberg",
               "Schwedisches Warmblut": "von der Tann",
               "Württemberger": "Bergfeld",
               "Noriker": "Auhof",
                }

for pferd, gestuet in value_pferd.items():
    query = {"Name": pferd}
    update = {"$set": {"Gestüt": gestuet}}
    inhalt_pferd.update_one(query, update)

# ---------------------------------------------------------
# Aufgabe 6
# ---------------------------------------------------------
for schnellstes_pferd in inhalt_pferd.find().sort("Geschwindigkeit", pymongo.DESCENDING).limit(1):
    print("Pferd mit der höchsten Geschwindigkeit: ", pferd)

# ---------------------------------------------------------
# Aufgabe 7
# ---------------------------------------------------------
# Alle verschiedenen Intelligenzwerte abrufen
intelligenz_values = inhalt_pferd.distinct("Intelligenz")

# Ergebnisse nach Intelligenz und Geschwindigkeit sortieren und ausgeben
for intelligenz in sorted(intelligenz_values, reverse=True):
    pferde = inhalt_pferd.find({"Intelligenz": intelligenz}).sort("Geschwindigkeit", pymongo.DESCENDING)

    print(f"Pferde mit Intelligenz {intelligenz}:")
    for pferd in pferde:
        print(pferd)

# ---------------------------------------------------------
# Aufgabe 8
# ---------------------------------------------------------
preis_query = {"Name": "Noriker"}
update = {"$set": {"Preis": 7000}}

result = inhalt_pferd.update_one(preis_query, update)
