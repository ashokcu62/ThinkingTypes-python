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

# check faild or pass

for sub, mark in marks.items():
    if mark <= 23:
        print(f"{sub} :passed")
    else:
        print(f"{sub}: faild")
# updating value in dict

print(marks["maths"])
marks["maths"] = 27
print(marks["maths"])


# taking values
maths_mark = marks["maths"]
print(f"maths mark {maths_mark}")


# taking values meth 2
physics_score = marks.get("physics")
print(physics_score)

# get bug
# jv=marks["java"]

# in the case of using get method
jv = marks.get("java")
print(f"jv :{jv}")    # get method returning none when the key is not existing

if jv :
    print("had nothing")
else:
    print("have values in jv", type(jv))


# commet on dict
n1:dict[str,int]={
    "one":1,
    "two":2,
    "three":3
}

n1["one"]="True"
print(n1)