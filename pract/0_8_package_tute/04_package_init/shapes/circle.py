class Circle:
    def __init__(self,radius:float) -> None:
        self.radius=radius
    def __str__(self) -> str:
        return f"circle radius is {self.radius}"