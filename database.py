from typing import Collection
import pymongo
from item_dataset import dataset

import pymongo

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connection_string = "mongodb://localhost:27017"
            self.cluster_connection = pymongo.MongoClient(connection_string)
            self.db = self.cluster_connection[database]
            self.collection = self.db[collection]  # Aqui a coleção é atribuída corretamente
            print(f"Conectado ao banco de dados: {database}, coleção: {collection}")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

