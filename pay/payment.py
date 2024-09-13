from typing import Protocol
from pay.credit_card import CreditCard
from pay.order import Order
from pay.processor import PaymentProcessor

class PaymentProcessor(Protocol):
    def charge(self, card: CreditCard, amount: int) -> None:
        """Charges the card with the given amount."""
        pass
    

def pay_order(order: Order,card:CreditCard,payment_processor: PaymentProcessor) -> None:
    if order.total == 0:
        raise ValueError("Can't pay an order with total 0.")

    payment_processor.charge(card.card, amount=order.total)
    order.pay()
