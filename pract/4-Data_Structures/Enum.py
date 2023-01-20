# e num is perfect data structure
# for creating choice or varieties
from enum import Enum, auto


class pizza(Enum):
    small = 20
    medum = 30
    large = 10


p = pizza.small
print(p.value)


class colors(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    one=auto()
    two=auto()
c=colors.RED

print(type(c))
print(c.one.value)
print(c.two.value)


#not work like that
for i in range(6):
    c=auto(Enum)
    print(c.value)
