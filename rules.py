from collections import namedtuple
from datetime import date

from data import Order

Rule = namedtuple(typename='Rule', field_names='qualifier calculator')


def is_qualified_for_expiration_discount(order: Order) -> bool:
    return (order.expiration_date - date.today()).days <= 30


def calculate_expiration_discount(order: Order) -> float:
    return order.price * 0.3


def is_qualified_for_price_discount(order: Order) -> bool:
    return order.price >= 1000


def calculate_price_discount(order: Order) -> float:
    return order.price * 0.9


def get_rules() -> tuple:
    return (
        Rule(qualifier=is_qualified_for_expiration_discount, calculator=calculate_expiration_discount),
        Rule(qualifier=is_qualified_for_price_discount, calculator=calculate_price_discount),
    )
