# --------------------------------------------------------
#                   MAGIC METHODS
# --------------------------------------------------------
from __future__ import annotations


class Box():
    def __init__(self, side_a: int, side_b: int) -> None:
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self)->int:
        #area for check lesstha __lt__
        return self.side_a*self.side_b

    def __repr__(self) -> str:
        return f"its from rpr"

    def __str__(self) -> str:
        return f"{self.side_a+self.side_b}"

        # specific fn
    def __contains__(self, num: object) -> bool:

        # in key word
        if not isinstance(num, int):
            raise NotImplemented


        return num in [self.side_a, self.side_b]

    def __eq__(self, other: object) -> bool:
        # checking  two boxes are equal or not
        if not isinstance(other, Box):
            raise  NotImplemented

        return self.side_a == other.side_a and self.side_b == other.side_b

    def __lt__(self,other:object)->bool:
        #checking lessthan 
        if not isinstance(other, Box):
            raise  NotImplemented

        # return self.side_a + self.side_b < other.side_b +other.side_a 
                              #or
        return self.area<other.area

    def __le__(self,other:object)->bool:
        #checking lessthan or eual
        if not isinstance(other, Box):
            raise  NotImplemented

        return self.area<=other.area

    def __add__(self,other:object)->int:
        #adding two objs eual
        if not isinstance(other, Box):
            raise  NotImplemented

        return self.area+other.area

    def __sub__(self,other:object)->int:
        #adding two objs eual
        if not isinstance(other, Box):
            raise  NotImplemented

        return self.area-other.area

    
    def __mul__(self,other:object)->int:
            #adding two objs eual
            if not isinstance(other, Box):
                raise  NotImplemented

            return self.area+other.area

    def __turediv__(self,other:object)->float:
            #adding two objs eual
            if not isinstance(other, Box):
                raise  NotImplemented

            return self.area / other.area

    def __floordiv__(self,other:object)->int:
        #adding two objs eual
        if not isinstance(other, Box):
            raise  NotImplemented

        return self.area//other.area



b = Box(23, 27)
b2 = Box(20, 20)
b3 = Box(23, 27)
b3 = Box(40, 40)

print(b)
print(b2)


# magic  fn calling
print(23 in b)

#equal or not 
print(b==b2)
print(b==b3)

print(b<b2)

#b1 <b2 or b1<=b2
#lessthan or equal2
print(b<=b3)

#calc
print(b+b2)
print(b-b2)

print(b//b2)
print(b*b2)
print(b/b2) #have to check