class Rectangle:
    def __init__(self,side_a:float,side_b:float) -> None:
        self.side_a=side_a
        self.side_b=side_b
    def __str__(self) -> str:
        return f"'rectangle  {self.side_a} x {self.side_b}"