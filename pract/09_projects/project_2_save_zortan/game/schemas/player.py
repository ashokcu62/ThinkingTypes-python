class Player:
    def __init__(self,fname:str,lname:str) -> None:
        self.fname=fname
        self.lname=lname
    
    def __repr__(self) -> str:
        return f"<class Player>"

    def __str__(self) -> str:
        return f" {self.fname}  {self.lname}"





        