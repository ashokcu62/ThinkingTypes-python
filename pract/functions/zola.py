from typing import Callable

# returning fun are known as Callable ->Callable[[input-type],return-type]
def zola(name: str):
    return f"{name} zola"


def gdmrg(name: str):
    return f"{name} good morng"


def gdafter(name: str):
    return f"{name} gdafter noon"

#important 
def universal_greeter(name: str, greeter: Callable[[str], str]):
    ms = greeter(name)
    print(ms)


universal_greeter('sasi', gdmrg)


#-----------function returning function

def show(name:str)->Callable[[],str]:
    def pshow():
        print(name)
    return pshow

jj=show("monster")
jj()

# three-----------

def add_by2(num1:int)->Callable[[int],int]:
    def by2(num2:int):
        sum=num1+num2
        return sum
    return by2

sum=add_by2(2)
print(sum(6))

# four -------------
