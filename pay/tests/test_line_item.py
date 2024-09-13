from pay.order import LineItem

def test_line_item_total():
    item = LineItem(name="Shoes", price=100_00)
    assert item.total == 100_00


def test_line_item():
    line_item = LineItem(name="Shoes", price=100_00, quantity=2)
    assert line_item.total == 200_00 