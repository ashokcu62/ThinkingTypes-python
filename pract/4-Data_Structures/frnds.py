

frnds: list[str] = ["popo", "chiko", "momo", "zoyo", "babo"]
for x in frnds:
    print(f"{[x]}{x} zolo")

# fried length
print(f"friends length is {len(frnds)}")

# unfrnd
# pop
unfriend = frnds.pop()
print(f"unfrended {unfriend}")
#make new friend
#apppend()
frnds.append("sasi")
print(frnds[4])
# ______________________
# remove a friend
frnds.remove("chiko")
print(frnds)

# -----------------
#  adding the removed friend
frnds.insert(1,"chiko")
print(frnds)



#  to conform chiko in friends list
if "chiko" in frnds:
    print("chiko is your friend")

#making chiko as 1st frnd
frnds.insert(0,"chiko")
print(frnds)

#making friends alphabetic order
frnds.sort()
print(frnds)

#making reverse alphabetic
frnds.reverse()
print(frnds)
#pop with index
unfriend = frnds.pop(4)
print(f"unfrended {unfriend}")
print(frnds)
