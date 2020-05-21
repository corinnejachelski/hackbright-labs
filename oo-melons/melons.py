import random
from datetime import datetime

"""Classes for melon orders."""
class AbstractMelonOrder():
    """"Abstract melon class"""
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.base_price = 5


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


    # def get_total(self):

    #     total = (1 + self.tax) * self.qty * self.base_price 

    #     return total


    def get_base_price(self):
        """Dynamic pricing update to base price"""
        self.base_price = random.randint(5,9)


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()
        
        if self.species == "Christmas Melon":
            self.base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * self.base_price 

        return total


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code


    def get_total(self):
        """Calculate price, including tax."""
        fee = 0
        base_price = self.get_base_price()

        if self.qty < 10 :
            fee = 3

        total = (1 + self.tax) * self.qty * self.base_price + fee

        return total


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A US Government melon order"""
    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.tax = 0 
        self.order_type = "government"
        self.passed_inspection = False


    def mark_inspection(self, passed):
        if passed:
            self.passed_inspection = True


