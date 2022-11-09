# and / or statement

def che(age, planet):
    if age <= 18 and planet == "earth":
        print("not eligible")
    elif age > 18 and planet == "earth":
        print("eligible for license")

    elif age > 18 or planet == "mars":
        print("eligible for mars license")
    else:
        print("not desided")


che(101, "earth")
che(20,"mars")
che(30,"moon")
