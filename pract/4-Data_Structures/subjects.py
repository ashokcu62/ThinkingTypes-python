# tuple :
# onece we create a tuple it cannot change
subjects: tuple[str, str, str, str] = ("maths", 'science', "english", "it")
print(subjects)
# len
for subject in subjects:
    print(subject)

# len
print(f" length {len(subject)}")

# incresing tupple size
n1: tuple[str, str, str] = ("english", "python", "physics")
print(n1)
subjects = n1+subjects
print(subjects)

#check vals
if "python"in subjects:
    print("ys have")
else:
    print("dont have")

    
