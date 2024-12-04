from database import Database
from bagModel import BagModel
from personModel import PersonModel
from personCLI import PersonCLI

db = Database(database="PROJETOS202DB", collection="bagofholding")  # Coleção de personagens
personModel = PersonModel(database=db)  # Passa o objeto Database corretamente
bagModel = BagModel(database=db)  # Coleção de itens compartilhada
personCLI = PersonCLI(bagModel)
personCLI.run()
