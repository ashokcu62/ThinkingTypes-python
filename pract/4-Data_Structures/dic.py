marks = {
    "maths": 0,
    "science": 22,
    "biology": 25,
    "physics": 23
}

# for x in marks:
#     print(marks)

print(marks)

# print key only and value
print(marks.keys())
print(marks.values())


# CHECK OUT ALL ITEMS
for sub, mark in marks.items():
    print(f"subject :{sub} | mark :{mark}")

for sub,mark in marks.items():
    print(f" sub:{sub} = {mark}")

print(marks.items())


#check pass or not

for sub,mark in marks.items():
     if mark>=23:
        print(f"passed {sub}")
     else:

        print(f"faild  {sub}")

marks["suology"]=500

print(marks)


#alt 1
#check score'
maths_score=marks["maths"]
print(f"maths score{maths_score}")

#alt 2
alr=marks.get("maths")
print(f"2 {alr}")

#for error less value   imp in get 
alr=marks.get("maths")

if alr != None:
    print(f"maths score{alr}")
else:
    print("invalid subject")

# delete key and pair in the dictionary
# del key
del marks["maths"]
print(marks)