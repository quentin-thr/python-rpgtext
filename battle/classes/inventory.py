class Item:
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop

    quantity = 0

    def set_quantity(self, value):
        self.quantity = value
