#tuple :
# onece we create a tuple it cannot change
sub:tuple[str,str,str,str]=("maths",'science',"english","it")
print(sub)
#len

print(f"{len(sub)}")

#items
for subs in sub:
    print(subs)


#adding values into tuple
new_sub=("ca","pgdca","Tally")
total_sub=sub+new_sub
print(total_sub)

val="Tally"
if val in total_sub:
    print("in the subject")
else:
    print("not in the tuple")