#Ну типоё классы для фильтров

class Skin:
    def __init__(self, image, price, rarity, availability, skin_type):
        self.image = image
        self.price = price
        self.rarity = rarity
        self.availability = availability
        self.skin_type = skin_type

    def info(self):
        return f"Скин ({self.image}, {self.price}, {self.rarity}, {self.availability}, {self.skin_type})"

