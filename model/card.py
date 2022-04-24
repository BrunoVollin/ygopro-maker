import random
from toml_handler import TomlHandler


class Card:
    def __init__(self, name, level, atk, defense, **kwargs):
        self.name = name
        self.level = level
        self.atk = atk
        self.defense = defense
        self.toml_handler = TomlHandler("../toml/test.toml")
        self.card_name: str = self.generate_name(self.name)
        self.args = kwargs

    @staticmethod
    def generate_id():
        random_number = ""
        for i in range(9):
            random_number += str(random.randint(0, 9))
        return int(random_number)

    @staticmethod
    def generate_name(string):
        return 'card' + "." + string.replace(" ", "").lower()

    def create_card(self):
        card_id = self.generate_id()

        card_data2 = {
            'title': self.card_name,
            'id': card_id,
            'name': self.name,
            'level': self.level,
            'atk': self.atk,
            'defense': self.defense
        }

        for i in self.args:
            card_data2[i] = self.args[i]

        data = self.toml_handler.dict_to_toml_string(card_data2)
        self.toml_handler.append_toml_string(data)

    def __str__(self):
        return f"{self.name} {self.level} {self.atk} {self.defense}"