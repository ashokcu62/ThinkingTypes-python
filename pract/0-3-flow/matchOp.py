# while traveling zorton luis packed lot of stuff,lets check luis has anything in your favorate color

fav_color:str=input("enter your fav color :").lower()
match fav_color:  #match fav_color.lower:
    case "blue":
        print("luis has a blue shrit")
    case "white":
        print("luis has a white hat")
    case "red":
        print("luis has a red pant")
    case _:
        print(f"luis has nothing with {fav_color} color")
