from pay.order import LineItem, Order
from pay.payment import pay_order

from typing import Protocol

class Flyable(Protocol):
    def fly(self) -> None:
        ...

class Bird:
    def fly(self):
        print("Flies in the sky")

class Car:
    def drive(self):
        print("Drives on the road")
    def fly(self):
        print("Flies in the sky")    

def use_flyable(f: Flyable):
    f.fly()

bird = Bird()
car = Car()

use_flyable(bird)  # Works fine, as Bird has a fly method
use_flyable(car)   # Raises error in type checker, Car lacks fly method


def main():
    # Test card number: 1249190007575069
    card = input("Please enter your card number: ")
    month = int(input("Please enter the card expiry month: "))
    year = int(input("Please enter the card expiry year: "))
    order = Order()
    order.line_items.append(LineItem(name="Shoes", price=100_00, quantity=2))
    order.line_items.append(LineItem(name="Hat", price=50_00))
    pay_order(order)


if __name__ == "__main__":
    main()
