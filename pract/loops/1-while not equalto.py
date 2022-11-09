# name = "ashokcu"
# for x in name:
#      print(x)

from multiprocessing.resource_sharer import stop
import re


correct_guss: bool = False
guss: str = ""
planet: str = "zortan"

# guss = input("enter planet name :")
# while guss != planet:
#         guss = input("  enter right planet  :")
# print("message send successfully")
#
#
#  meth2

# while correct_guss != True:

#     guss = input("guss the planet   :")
#     if guss.lower() == planet.lower():
#         print(f" excelent right gus :{planet}")
#         correct_guss = True
#     else:
#         print("wong guss try again ")

#meth3
while True:
         guss=input("planet name :")
         if guss.lower()==planet.lower():
                print("right guss")
                break
         else:
                print("try again")
