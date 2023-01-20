# used to implement particular bahaviour for our class
from __future__ import annotations
from enum import Enum, auto
from datetime import datetime


class Person:
    def __init__(self, fname: str, lname: str):
        self.fname = fname
        self.lname = lname

    def __str__(self) -> str:
        return f"name is :{self.fname}{self.lname}"

    def nano(d):  # argumant that 1st come in a method  is always self
        print(f"its from nano{d.lname}  {d.fname}")

    @property  # imp  also can call self
    def full_name(self) -> str:
        return f"{self.fname}{self.lname}"


# ==============================================================================
# staff roles


class Role(Enum):
    ASSOCIATE = auto()
    SUPERVISOR = auto()
    MANAGER = auto()


print(Role.MANAGER.value)


# =============================================================================

#  final decorator =" if thisis my final class nobody can in herit it "

class Staff(Person):
    def __init__(self, fname: str, lname: str, staff_id: int, role: Role) -> None:
        super().__init__(fname, lname)
        self.staff_id = staff_id
        self.role = role
        self.is_staff = True

        # privet var by using in front of (_) dash as var
        self._date_of_joined = datetime.now()


        # #  Dinamic salary    meth changed by line 80 salarysett
        match role:
            case Role.ASSOCIATE:
                self.__salary: float = 15
            case Role.SUPERVISOR:
                self.__salary: float = 20
            case Role.MANAGER:
                self.__salary: float = 25



    def __str__(self) -> str:
        # printing vals
        data = f""" name { self.full_name}
         id :{self.staff_id} 
         role : {self.role} 
        """
        return data

    # decoratiom
    @classmethod
    def new(cls, person: Person, staff_id: int, role: Role) -> Staff:
        """
        creating a new  staff instance

        Note: it takes class as the 1st argument and returns a inistance of the class
        """
        return cls(person.fname, person.lname, staff_id, role)

    @property
    def join_date(typeAny_it_must_be_self) -> str:
        return f"{typeAny_it_must_be_self._date_of_joined.strftime(' %T %d %B %Y')}"

    @property
    def salary(self) -> float:
        return self.__salary

    # setter method -decoration
    @salary.setter
    def salary(self, amt: float):
        # setting salary after vallidation
        if self.role == Role.ASSOCIATE and amt < 15:
            print("Error ! Associate cannot have  salary less than $15/hr")
        elif self.role == Role.SUPERVISOR and amt < 20:
            print("Error ! SUPERVISOR nnot have  salary less than $15/hr")
        elif self.role == Role.MANAGER and amt < 30:
            print("Error ! Mannager cannot have  salary less than $15/hr")
        else:
            self.__salary=amt
            print(f"{self.full_name}  salry {self.__salary}")
                @staticmethod
    def describe():
        print("hi its static method demo")

# -------------------------------------------------------------------------------

Staff.describe()

p1 = Person("ashok", "yagami")
# print(p1.lname)
# p1.nano()


st1 = Staff("lite", "yagami", 22, Role.ASSOCIATE)
print(st1)
print(st1.join_date)

print(f"salary {st1.salary}")



st2 = Staff.new(p1, 1234, Role.MANAGER)

print(f"st2 date  :{st2.join_date}")
print(f"salary {st2.salary}")

st2.salary=18
st1.salary=40

# art 2
# (def __str__(self)->str:
#     #printing vals
#     data=f""" name { self.full_name}
#      id :{self.staff_id}
#      role : {self.role}
#     date of joining:{self._date_of_joining}
#      salary :{self.__salary}"""

#     return data)
# ---------------------------------------------------------------------------
class Hr(Staff):
    pass