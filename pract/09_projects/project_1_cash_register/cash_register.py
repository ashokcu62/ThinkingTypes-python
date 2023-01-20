from costomer import Costomer
from invoice_item import InvoiceItem
from datetime import datetime
from item import Item
import json


class CashRegister:
    def __init__(self, costomer: Costomer) -> None:
        self.costomer = costomer
        self.items: dict[str, InvoiceItem] = {}
        self.purchase_date = datetime.now()
        self.invoice_total: float = 0

    def __repr__(self) -> str:
        return "<class CashRegister>"

    def __str__(self) -> str:
        return f"Costomer :{self.costomer} total_items:{len(self.items)}"

        # increment invoice sub total
    def _inc_invoice_total(self, item: InvoiceItem):
        """increment the total invoice each time the new item added"""
        self.invoice_total += item.get_sub_total()

    def _dec_invoice_subtotal(self, item: InvoiceItem):
        """decrement the total invoice each time the item is removed """
        self.invoice_total -= item.get_sub_total()

    def add_item(self, item: Item, qty: int = 1, discount: int = 0) -> None:
        """ adding an item to cash register"""
        if item.name not in self.items:
            new_item = InvoiceItem(item, qty, discount)
        # self.items[item.name] >>  is key assigning and the value is new  item
        # in here key and value assinging to the item dic[] as the dic syntax

            self.items[item.name] = new_item
            self._inc_invoice_total(new_item)

        else:
            print(f"{item.name} already in cart")

    def update_item(self, item: Item, qty: int = 1, discount: int = 0) -> None:
        """ updating a specific item  alredy added to cash register"""
        if item.name in self.items:
            old_item = self.items[item.name]
            # to update 1st we need to take it from the list to get its subtotal
            # to decrese the main subtotal variable
            self._dec_invoice_subtotal(old_item)

            #  taking values from the update fn and adding the new value
            new_item = InvoiceItem(item, qty, discount)
            self.items[item.name] = new_item
            self._inc_invoice_total(new_item)

        else:
            print(f"{item.name} not in cart purchase insted")

    def remove_item(self, item: Item) -> None:
        """remove the item to the cash register"""
        if item.name in self.items:
            old_item = self.items[item.name]
            self._dec_invoice_subtotal(old_item)
            del self.items[item.name]

        else:
            print(f"{item.name} not in cart purchase insted")

    def get_invoice_total(self) -> float:
        """ returns invoice total """
        return self.invoice_total

    def display_invoice(self) -> None:
        print()
        print("+"*70)
        print(self)
        print(f"Date :{self.purchase_date.strftime('%B,%d,%Y')}")
        print("-"*70)
        for item in self.items.values():
            print(item)
        print("-"*70)
        print(f"Total Price :${self.get_invoice_total():.2f}..")

    def bugshw(self):
        print(type(self.items.items()))

    def _get_items_as_dict(self) -> dict:
        items_dict = {}
        for item_name, invoice_item in self.items.items():
            items_dict[item_name] = invoice_item.dict()
        return items_dict


    def dict(self) -> dict:
        """Returns dictionary representation of Cash Register"""
        print("hii")
        cash_register = {
            "customer": self.costomer.dict(),
            "items": self._get_items_as_dict(),
            "purchase_date": self.purchase_date.strftime("%B %d, %Y"),
            "invoice_total": self.get_invoice_total(),
        }
        return cash_register

    def toJSON(self) -> str:
        """Returns JSON formatted string of Cash Register"""
        return json.dumps(self.dict(), indent=4, sort_keys=True)
