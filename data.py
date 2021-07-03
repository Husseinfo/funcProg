from datetime import date


class Order(object):
    id: int
    description: str
    expiration_date: date
    price: float

    def __init__(self, _id, description, expiration_date, price):
        self.id = _id
        self.description = description
        self.expiration_date = expiration_date
        self.price = price
