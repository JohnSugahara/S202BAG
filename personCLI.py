class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

class PersonCLI(SimpleCLI):  # Mantendo o nome PersonCLI, mas agora é BagCLI
    def __init__(self, bag_model):
        super().__init__()
        self.bag_model = bag_model  # Usando o bag_model em vez de person_model
        self.add_command("create", self.create_item)
        self.add_command("read", self.read_item)
        self.add_command("update", self.update_item)
        self.add_command("delete", self.delete_item)

    def create_item(self):
        # Criação de um novo item
        item_name = input("Enter the item name: ")
        item_type = input("Enter the item type: ")
        item_weight = float(input("Enter the item weight: "))
        item_properties = input("Enter the item properties (as JSON-like string): ")
        
        # Chamando o método do modelo de bag para criar o item
        self.bag_model.create_item(item_name, item_type, item_weight, item_properties)

    def read_item(self):
        # Leitura de um item pelo ID
        item_id = input("Enter the item ID: ")
        itens = self.bag_model.read_item_by_id(item_id)
        if itens:
            print(f"Item ID: {itens['_id']}")
            print(f"Name: {itens['nome']}")
            print(f"Type: {itens['tipo']}")
            print(f"Weight: {itens['peso']}")
            print(f"Properties: {itens['propriedades']}")
        else:
            print("Item not found.")

    def update_item(self):
        # Atualização de um item existente
        item_id = input("Enter the item ID: ")
        new_name = input("Enter the new item name: ")
        new_type = input("Enter the new item type: ")
        new_weight = float(input("Enter the new item weight: "))
        new_properties = input("Enter the new item properties (as JSON-like string): ")
        
        self.bag_model.update_item(item_id, new_name, new_type, new_weight, new_properties)

    def delete_item(self):
        # Exclusão de um item
        item_id = input("Enter the item ID: ")
        self.bag_model.delete_item(item_id)

    def run(self):
        print("Welcome to the bag CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
