class Pokemon:
    def __init__(self, name, types, favorite_saying):
        self.name = name
        self.types = types
        self.is_caught = False
        self.favorite_saying = favorite_saying

    def print_pokemon(self):
        print({
            "name": self.name,  # Output: "name": "Squirtle",
            "types": self.types,  # Output: "types": ["Water"],
            "is_caught": self.is_caught,  # Output: "is_caught": False
            "favorite saying": self.favorite_saying,
        })

    def catch(self):
        self.is_caught = True

    def favorite_saying(self):
        self.favorite_saying()


#  This creates an Instance of the Pokemon class!
fatima = Pokemon('Fatima', 'Speed', "You know da vibes")

fatima.catch()
fatima.print_pokemon()
