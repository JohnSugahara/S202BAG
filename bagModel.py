import pymongo
from bson import ObjectId

class BagModel:
    def __init__(self, database):
        self.db = database.db  # Supondo que você tenha um 'db' no objeto Database
        self.collection = self.db["bagofholding"]  # A coleção de itens na bag

    def create_item(self, name, item_type, weight, properties):
        # Método para criar um item na bag
        item = {
            "nome": name,
            "tipo": item_type,
            "peso": weight,
            "propriedades": properties
        }
        self.collection.insert_one(item)
        print("Item criado com sucesso!")

    def read_item_by_id(self, item_id):
        # Método para ler um item da bag usando o ID
        item = self.collection.find_one({"_id": ObjectId(item_id)})
        return item

    def update_item(self, item_id, new_name, new_type, new_weight, new_properties):
        # Método para atualizar um item da bag
        self.collection.update_one(
            {"_id": pymongo.ObjectId(item_id)},
            {
                "$set": {
                    "nome": new_name,
                    "tipo": new_type,
                    "peso": new_weight,
                    "propriedades": new_properties
                }
            }
        )
        print("Item atualizado com sucesso!")

    def delete_item(self, item_id):
        # Método para deletar um item da bag
        self.collection.delete_one({"_id": pymongo.ObjectId(item_id)})
        print("Item deletado com sucesso!")
