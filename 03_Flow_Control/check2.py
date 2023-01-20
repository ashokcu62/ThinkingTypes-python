# i: int = 1
# T = True
# sum = 0
# while T==True:
# # sum = sum + i
# print(sum)
# if sum == 100:
#     # print("got 100 u lol and t got false")
# T=False

# ash="ABCD"
# print(ash.lower())
# -------------------------------------------------------------------------
# GUS MY MYNAME
# -------------------------------------------------------------------------
MYNAME: str = "ashok"
Currect_guss: bool= False
guss: str = ""

# GAME
# ------

while Currect_guss is not True:
	guss = input("guss my name ")
	if guss.lower() == MYNAME.lower():
		guss = input(f"right guss my name is {MYNAME}")
		Currect_guss = True
	else:
		print("try again")
