class Pokemon():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp  # hit points/health
        self.damage = damage  # The amount of damage this pokemon does to its opponent every attack

    def attack(self, opponent):
        opponent.hp -= self.damage
        if opponent.hp < 0:
            print(f"{opponent.name} fainted.")
        else:
            print(f"{self.name} dealt {self.damage} damage to {opponent.name}.")
        print(f"Now {opponent.name} has {opponent.hp} health points.\n")


pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30)

opponent = bulbasaur
pikachu.attack(opponent)
pikachu.attack(opponent)
pikachu.attack(opponent)
