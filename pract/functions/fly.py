# Since Zortan has less gravity residents can fly
# if they are less than or equal to 15kgs in Zortan  weight

# luis want to check his friends can fly  there or not

# -----------------------------------------
# SINGLE RESPONSIBILITY PRINCIPLE
# ------------------------------------------

from typing import Final

MAX_FLYING_WEIGHT: Final[float] = 15



def canfly(weight: float) -> bool:
    # checking who can fly
    #returning a bool value
    return weight <= MAX_FLYING_WEIGHT
      


# earth weight to zortan calculate

def calculate_Zortan_weight(earth_weight: float):
    # returning the calculated value
    return (earth_weight+32)/8


# flying check function
def flying_friends(friends: dict[str, float]):

    # loop for map the dict from main fn
    for name, earth_weight in friends.items():
        # geting value from calzor fn
        zortan_weight = calculate_Zortan_weight(earth_weight)
        #seinding to canfly fn
        if canfly(zortan_weight):
            print(f"{name}: w :{zortan_weight} can fly in zortan ")
        else:
            print(f"{name}: w :{zortan_weight} cannot fly in zortan ")


#-----------------main----------
def main() -> None:
    friends: dict[str, float] = {
        "sonu": 54,
        "monu": 88,
        "damu": 50,
        "sasi": 102,
        "ramu": 90
    }
    flying_friends(friends)


main()
