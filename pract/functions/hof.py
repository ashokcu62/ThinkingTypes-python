from typing import Callable
# ----------lambda_ARE FUNCTION

#                    syntax   lambda input:return
# -----------------LAMBDA CALCULATOR


add: Callable[[int, int], int] = lambda num1, num2: num1+num2
subs: Callable[[int, int], int] = lambda num1, num2: num1-num2
mult: Callable[[int, int], int] = lambda num1, num2: num1*num2
div: Callable[[int, int], int] = lambda num1, num2: num1//num2

def calc(num:int,num2:int,operation:Callable[[int,int],int]):
    result=operation(num,num2)
    print(result)


calc(20,20,add)
calc(20,20,mult)


# print(add(40,50))
# print(subs(40,50))
# print(mult(40,50))
# print(div(50,50))