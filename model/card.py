import random
from toml_handler import TomlHandler


class Card:
    def __init__(self, name, level, atk, defense):
        self.name = name
        self.level = level
        self.atk = atk
        self.defense = defense
        self.tm = TomlHandler("toml/test.toml")
        self.card_name: str = self.generate_name(self.name)

    def generate_id(self):
        random_number = ""
        for i in range(9):
            random_number += str(random.randint(0, 9))
        return int(random_number)

    def generate_name(self, string):
        return'card' + "." + string.replace(" ", "").lower()

    def create_card(self):
        card_id = self.generate_id()

        card_data = f'''
[[{self.card_name}]]
id = {card_id}
name = {self.name}
level = {self.level}
atk = {self.atk}
defense = {self.defense}      
        '''
        self.tm.append_toml_string(card_data)

    def __str__(self):
        return f"{self.name} {self.lvl} {self.atk} {self.defense}"


c = Card("test", 1, 1, 1)

c.create_card()

print(f'''

type card_name = {type(c.card_name)}
type name = {type(c.name)}
card_name = {c.card_name}
''')
