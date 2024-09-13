from pay.order import Order, OrderStatus
from pay.order import LineItem
from pay.payment import pay_order


def test_empty_order():
    order = Order()
    assert order.total == 0
    
def test_order_total():
    order = Order()
    order.line_items.append(LineItem(name="Shoes", price=100_00, quantity=2))
    order.line_items.append(LineItem(name="Hat", price=50_00))
    assert order.total == 250_00    
    
    
def test_orderpay():
    order = Order()
    order.line_items.append(LineItem(name="Shoes", price=100_00, quantity=2))
    order.line_items.append(LineItem(name="Hat", price=50_00))
    assert order.status == OrderStatus.OPEN
    
    assert order.total == 250_00    