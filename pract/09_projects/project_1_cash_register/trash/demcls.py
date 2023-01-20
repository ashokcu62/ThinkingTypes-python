class dem:
    def __init__(self,name:str,lname:str):
        self.name=name
        self.lname=lname

    def __str__(self) -> str:
       return f"{self.name}{self.lname}"
    def display(self):
        print(f"self:{self}")
    def math(self):
        return 40
d=dem("ashok","yagami")
d.display()
print(d.math())

