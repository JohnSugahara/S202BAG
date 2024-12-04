from pymongo import MongoClient
from bson.objectid import ObjectId

class PersonModel:
    def __init__(self, database):
        self.database = database
        self.collection = database.collection  # Use a coleção fornecida pela classe Database

    def create_person(self, name, bag_id):
        try:
            person = {"name": name, "bag_id": bag_id}
            result = self.collection.insert_one(person)
            return result.inserted_id
        except Exception as e:
            print(f"Erro ao criar personagem: {e}")

    def read_person(self, person_id):
        try:
            return self.collection.find_one({"_id": ObjectId(person_id)})
        except Exception as e:
            print(f"Erro ao obter personagem: {e}")

