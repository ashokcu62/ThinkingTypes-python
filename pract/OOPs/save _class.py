class Charactor:
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        self.name = name
        self.attack_power = attack_power
        self.life = life
    def __repr__(self) -> str:
        return"<class Charactor>"
    def __str__(self) -> str:
        return f"name {self.name}  attacking_power {self.attack_power} life  {self.life}"

villain=Charactor("thanos",400,1500)
hero=Charactor("hulk",300,800)

print(hero)
print(villain)
