class Costomer:
    """Costomer Details"""
    def __init__(self,fname:str,lname:str) -> None:
        self.fname=fname
        self.lname=lname

    def __repr__(self)->str:
        return"<class for costomer>"

    def __str__(self) -> str:
        return f"{self.fname} {self.lname}"

    def dict(self)->object:
        return{"first_name":self.fname,"last_name":self.lname}
        