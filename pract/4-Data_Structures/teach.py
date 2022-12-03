#set
magicWord="abrakdabra"

#sorting uniqe words

# set has {} like dict but only it has values init
unqword=set(magicWord)
print(type(unqword))

#add more words to set
#unique words
sentense:str="ashok has a car  and a girl friend her name is kivi"
uniqsentense=sentense.split()   # spliting the string and making new sentence  but its not unique
print(uniqsentense)             # split will make list 
print(f" sentence type{type(uniqsentense)}")


# extract the unique words
uniqwords=set(uniqsentense)
print(uniqwords)

#updating new values  in set is  
uniqwords.update(["one","two","three"])
print(uniqwords)

# remove words
uniqwords.remove("ashok")
print(uniqwords)
