age=int(input("enter your age :"))
planet=str(input("enter your planet :"))

if age > 16 and planet == "earth":
	print("eligble for license in earth")
elif age < 16 and planet == "earth":
	print("dont have license in earth  can apply zortan")
elif age < 16 or planet == "zortan":
	print("you can have lices in  zortan")
