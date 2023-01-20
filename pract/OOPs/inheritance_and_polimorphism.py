class Animal():
    def __init__(self, name: str, age: int, legs: int) -> None:
        self.name = name
        self.age = age
        self.legs = legs

    def __str__(self) -> str:
        return f"name  :{self.name}"

    def talk(self) -> None:
        "makes the animal talk"
        print(f"{self.name} cant talk yet")


# inheritance

class Dog(Animal): 
    def __init__(self, name: str, age: int, legs: int, breed: str):
        # take the common features pass it to the parent (super)class
        super().__init__(name, age, legs)

        self.breed=breed
        self.type="dog"
      
    def __str__(self)->str:
        return(f"its a {self.type} name: {self.name} breed:{self.breed}")

    def talk(self)->None:
        print(f"{self.name}  can talk")
    
    def sniff(self,item:str):
        print(f"{self.name} is siffing a {item}")

    #  self  is not printable
    # def bk(self):
    #     return self
    
    
        
        

 

d = Dog("jonny", 8, 4, "laber")
print(d)
d.talk()
d.sniff("rabbit")
p


#------------check instance-----------
print(isinstance(d,Animal))

# a1 = animal("robin", 28, 2)
# print(a1)
# a1.talk()
