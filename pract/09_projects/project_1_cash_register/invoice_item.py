from item import Item



class InvoiceItem:
    def __init__(self, item: Item, qty: int, discount: float = 0) -> None:
        self.item = item
        self.qty = qty
        self.discount = discount
        # private
        self._sub_total = (item.price*qty)-discount

    def __repr__(self) -> str:
        return f" < class 'Item'>"

    def __str__(self) -> str:
        return (f"name :{self.item.name}, qty :{self.qty},"
                f" discount: ${self.discount},Sub Total: {self.get_sub_total():.2f} ")

    def get_sub_total(self) -> float:
        "Returns the Sub-total"
        return self._sub_total

    def dict(self) -> dict:
            """Return dictionary representation of the instance"""
            return {
                "name": self.item.name,
                "quantity": self.qty,
                "discount": self.discount,
                "sub_total": self.get_sub_total(),
            }

