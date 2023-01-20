from typing import Final
from random import randint
# annote class
Charactor = dict[str, str | int]

# Super heros
IRONMAN: Final[Charactor] = {
    "name": "Ironman", "attack_power": 250, "life": 1000}
BLACKWIDOW: Final[Charactor] = {
    "name": "BlackWidow", "attack_power": 180, "life": 800}
SPIDERMAN: Final[Charactor] = {
    "name": "spiderman", "attak_power": 190, "life": 700}
HULK: Final[Charactor] = {"name": "Hulk", "attack_power": 300, "life": 1100}

# Super Villains
TANOS: Final[Charactor] = {"name": "Thanos",
                           "attack_power": 1500, "life": 1500}
REDSKULL: Final[Charactor] = {
    "name": "Redskull", "attack_power": 300, "life": 800}
PROXIMA: Final[Charactor] = {
    "name": "Proxima", "attack_power": 320, "life": 800}
# powers
IRONMAN_ATTACKING: Final[int] = 250
BLCKWIDOW_ATTACKING: Final[int] = 180
SPIDERMAN_ATTACKING: Final[int] = 190
HULKS_ATTACKING: Final[int] = 300

# All Super heros And Supervillains
superheros: list[Charactor] = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
supervillans: list[Charactor] = [TANOS, REDSKULL, PROXIMA]

thanos_life: int = 1500
choice: int = 0
attack_num: int = 0
hero_life:int=0
villain_life:int=0

# Help Messages
WIN_MS: Final[str] = "You are successfully saved Zortan"
LOST_MS: Final[str] = "Thanos killed Avengers and captured Zortan"

# Attack
for attack in range(3):
    # each iteration get a new hero and  villain
    hero_index = randint(0, 3)
    villain_index = randint(0, 2)

    # helper variables
    current_superhero = superheros[hero_index]
    current_villain = supervillans[villain_index]
    print(
        f" {attack} attack >>{current_superhero['name']} finghing with {current_villain['name']}")
    
    # life
    hero_life += current_superhero["life"]
    villain_life  += current_villain["life"]
    print(f"life {hero_life}  : {villain_life}")

    
    #attack
    hero_life-=current_villain["attack_power"]
    villain_life-=current_superhero["attack_power"]
    choice+=1

    print(f"attack poer = {hero_life} : {villain_life}")


#print  a nice seperate
print("="*70)
if hero_life>=villain_life:
    print(WIN_MS)
else:
    print(LOST_MS)
