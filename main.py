import copy
from datetime import date
from statistics import mean

from data import Order
from rules import get_rules


def get_order_with_discount(o: Order, rules: tuple) -> Order:
    discount_price = mean([rule.calculator(o) for rule in rules if rule.qualifier(o)][:3] or [o.price])
    discount_order = copy.copy(o)
    discount_order.price = discount_price
    return discount_order


if __name__ == '__main__':
    orders = (
        Order(_id='Order1', description='First order', expiration_date=date(2022, 1, 1), price=1200),
        Order(_id='Order2', description='Second order', expiration_date=date(2021, 7, 30), price=850),
        Order(_id='Order3', description='Third order', expiration_date=date(2023, 1, 1), price=700),
    )

    for order in orders:
        print(f'Price of order {order.id} after discount will be {get_order_with_discount(order, get_rules()).price}'
              f'\nOld price was {order.price}')
