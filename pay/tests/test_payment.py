from datetime import date
from pay.credit_card import CreditCard
from pay.order import LineItem, Order
from pay.payment import pay_order
import pytest

class PaymentProcessorMock:
    def charge(self, card: CreditCard, amount: int) -> None:
        print(f"Charging card number {card} for ${amount/100:.2f}")

@pytest.fixture
def card()->CreditCard:
    year=date.today().year+2 
    return CreditCard("1249190007575069", 12, year,)

def test_pay_order(card:CreditCard):
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order,  card, PaymentProcessorMock())
    
def test_invalid_pay_order(card:CreditCard):
    with pytest.raises(ValueError):
        order = Order()
        pay_order(order,card, PaymentProcessorMock())     