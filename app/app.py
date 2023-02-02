import json
from pymongo import MongoClient
 
 
# Making Connection
myclient = MongoClient("mongodb://root:1234@localhost:27017")
  
# database
db = myclient["JDG"]
  
# Created or Switched to collection
Collection = db["Pokedex"]
 
# Chargement du fichier json contenant tout les pokemons
# with open('pokemon.json') as file:
#     file_data = json.load(file)

# Insertion du fichier json
# Collection.insert_many(file_data) 


# Chargement du fichier json contenant un pokemon
with open('new_pokemon.json') as file:
     data = json.load(file)

# Insertion du fichier json pour un pokemon
Collection.insert_one(data)
