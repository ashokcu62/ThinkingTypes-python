"""
Save Zortan:
------------

The war has just intensified, Thanos army has reach Zortan and are going to
fight along with him. With his army, this time Thanos is going to attach Avengers
and the battle is going to be intense!!!

Since, everything is going in real-time, we don't have control over characters,
instead our characters will choose their own fight.

This time each character gets it own structure and defined parameters, so as you
can see our code is getting better and certainly we are going to make is awesome
as we progress with future modules.
"""

# we need this for generating random nos.
from random import randint
from typing import Final

# -------------------------------------------------------------------------
# TYPE ALIAS:
# ===========
# Each time typing type as dict[str, str | int] is so boring, so we instead
# create a type alias and make our lives simpler.
# -------------------------------------------------------------------------
Character = dict[str, str | int]

# -----------------------------------
# Using function
# ----------------------------------

# Helper Variables
hero_life = 0
villain_life = 0


def get_all_superheros():
    IRONMAN: Final[Character] = {
        "name": "Ironman", "attack_power": 250, "life": 1000}
    BLACKWIDOW: Final[Character] = {
        "name": "Blackwidow", "attack_power": 180, "life": 800}
    SPIDERMAN: Final[Character] = {
        "name": "Spiderman", "attack_power": 190, "life": 700}
    HULK: Final[Character] = {"name": "Hulk",
                              "attack_power": 300, "life": 1100}

    superheros: list[Character] = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
    return superheros


def get_all_supervillains():
    # Super Villains
    THANOS: Final[Character] = {
        "name": "Thanos", "attack_power": 400, "life": 1500}
    REDSKULL: Final[Character] = {
        "name": "Redskull", "attack_power": 300, "life": 800}
    PROXIMA: Final[Character] = {
        "name": "Proxima", "attack_power": 320, "life": 800}

    villains: list[Character] = [THANOS, REDSKULL, PROXIMA]
    return villains





# getting specfic hero and villain

def get_superhero(index: int):
    superhero = get_all_superheros()
    if index < len(superhero):
        return superhero[index]
    else:
        return None


def get_supervillain(index: int):
    supervillain = get_all_supervillains()
    if index < len(supervillain):
        return supervillain[index]
    else:
        return None


#------------life-------------------

def inc_hero_life(life):
    global hero_life
    hero_life += life
    return hero_life


def inc_villain_life(life):
    global villain_life
    villain_life += life
    return villain_life


def dec_hero_life(attack: int):
    global hero_life
    hero_life -= attack


def dec_villain_life(attack):
    global villain_life
    villain_life -= attack


#--------------simulating attack-----------

def simulate_attack(villain, hero, attact_num):

    # set life

    inc_hero_life(hero["life"])
    inc_villain_life(villain["life"])

    # display

    print(
        f"Attack: {attact_num + 1} => {hero['name']} is going to fight with {villain['name']}."
    )
    # actual attack
    dec_hero_life(villain["attack_power"])
    dec_villain_life(hero["attack_power"])


#---------------- Attack----------
def attack():

    
    for attack_num in range(3):
        # each iteration get a new hero & villain
        hero_index = randint(0, 3)
        villain_index = randint(0, 2)
       
        current_superhero = get_superhero(hero_index)
        current_villain = get_supervillain(villain_index)

        if current_superhero and current_villain:
            simulate_attack(current_villain, current_superhero, attack_num)
        else:
            print("no super heros or villians to fight")

        print("=" * 58)


#---------win or loose----

def win_or_lose():
    WIN_MSG: Final[str] = "Avengers successfully saved Zortan!!! ✨ ✨ ✨"
    LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!! 💀 💀 💀"

    if hero_life >= villain_life:
        print(WIN_MSG)
    else:
        print(LOST_MSG)

# -------------------------------------------------------------------------
#                   MAIN
# --------------------------------------------------------------------------
       
def main()->None:
    attack()
    win_or_lose()

#--------------starting the game---------------------------------------------

main()

