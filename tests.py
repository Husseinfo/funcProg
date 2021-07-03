import unittest
from datetime import date, timedelta
from statistics import mean

from data import Order
from main import get_order_with_discount
from rules import get_rules, is_qualified_for_expiration_discount, is_qualified_for_price_discount


class TestRules(unittest.TestCase):
    def test_expiration_discount_rule(self):
        qualified_order = Order(_id='Qualified1', description='Qualified order',
                                expiration_date=date.today() + timedelta(days=15), price=1000)
        self.assertTrue(is_qualified_for_expiration_discount(qualified_order))

        non_qualified_order = Order(_id='NonQualified1', description='Non qualified order',
                                    expiration_date=date.today() + timedelta(days=60), price=1000)
        self.assertFalse(is_qualified_for_expiration_discount(non_qualified_order))

    def test_price_discount_rule(self):
        qualified_order = Order(_id='Qualified1', description='Qualified order',
                                expiration_date=date.today(), price=1200)
        self.assertTrue(is_qualified_for_price_discount(qualified_order))

        non_qualified_order = Order(_id='NonQualified1', description='Non qualified order',
                                    expiration_date=date.today(), price=400)
        self.assertFalse(is_qualified_for_price_discount(non_qualified_order))


class TestDiscount(unittest.TestCase):

    def test_qualified_expiration(self):
        qualified_order = Order(_id='Qualified1', description='Qualified order',
                                expiration_date=date.today() + timedelta(days=15), price=900)
        self.assertEqual(get_order_with_discount(qualified_order, get_rules()).price, 900 * 0.3)

    def test_qualified_price(self):
        qualified_order = Order(_id='Qualified1', description='Qualified order',
                                expiration_date=date.today() + timedelta(days=45), price=1200)
        self.assertEqual(get_order_with_discount(qualified_order, get_rules()).price, 1200 * 0.9)

    def test_qualified_both(self):
        qualified_order = Order(_id='Qualified1', description='Qualified order',
                                expiration_date=date.today() + timedelta(days=12), price=1500)
        self.assertEqual(get_order_with_discount(qualified_order, get_rules()).price, mean((1500 * 0.9, 1500 * 0.3)))

    def test_non_qualified_both(self):
        non_qualified_order = Order(_id='NonQualified1', description='Non qualified order',
                                    expiration_date=date.today() + timedelta(days=40), price=800)
        self.assertEqual(get_order_with_discount(non_qualified_order, get_rules()).price, non_qualified_order.price)


if __name__ == '__main__':
    unittest.main()
