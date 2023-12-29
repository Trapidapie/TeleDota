# Ну типоё классы для фильтров

class Skin:
    def __init__(self, hero, image, price, rarity, availability, skin_type):
        self.hero = hero
        self.image = image
        self.price = price
        self.rarity = rarity
        self.availability = availability
        self.skin_type = skin_type

    def info(self):
        return f"Скин ({self.image}, {self.price}, {self.rarity}, {self.availability}, {self.skin_type})"


