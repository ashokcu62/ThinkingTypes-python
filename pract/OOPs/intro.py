class stuents:
    pass


# --------------------------------
class persons:
    def __init__(self, name: str, name2: str) -> None:
        self.name = name
        self.name2 = name2

    # def __repr__(self)->str:
    #     """ official representation of the class"""
    #     return "<this is clss of persons>"

    def __str__(self) -> str:
        return (
            f"hii mownoose "
            f"hello its me"
        )

    def show(self):
        print(self.name+self.name2)

    def p(self):
        print(type(self))


p1 = persons("surya", "vijay")
print(p1)
p1.p()

# ------------check instance-----------
print(isinstance(p1, stuents))
