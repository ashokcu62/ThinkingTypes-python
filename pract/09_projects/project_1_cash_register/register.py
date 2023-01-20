from cash_register import CashRegister
from costomer import Costomer
from item import Item

milk = Item(100, "Milk", 28, "ltr")
pepsi = Item(102, "pepsi", 40, "ltr")
rise = Item(100, "rise", 46, "ltr")
battery= Item(100, "battery", 15, "pice")
biscut = Item(100, "biscut", 50, "pac")
costomer1=Costomer("ashok","cu")

cr1=CashRegister(costomer1)
cr1.add_item(milk)
cr1.add_item(pepsi)
cr1.add_item(rise)
cr1.add_item(biscut)
cr1.add_item(biscut)
cr1.update_item(battery,4,1)
cr1.remove_item(milk)
cr1.update_item(pepsi,5,40)



cr1.display_invoice()
print(cr1.toJSON())
print("-"*70)
cr1.bugshw()