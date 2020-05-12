"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}
    class_name = "Cupcake"


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<{self.class_name} name="{self.name}" qty={self.qty}>'  


    def __init__(self, name, flavor, price):
        """Create a cupcake object"""
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0 
        Cupcake.cache[self.name] = self


    def add_stock(self, amount):

        self.qty += amount
        return


    def sell(self, amount):

        if self.qty == 0:
            print(f"Sorry, these {self.class_name.lower()}s are sold out")
            return
        elif amount > self.qty:
            # print(f"Sorry you asked for {amount} cupcakes and {self.qty}")
            # print("are available.")
            self.qty = 0
        else:
            self.qty -= amount
            


    @staticmethod
    def scale_recipe(ingredients, amount):

        ingred_dict = {}

        for tup in ingredients:
            ingred_dict[tup[0]] = tup[1] * amount

        return list(ingred_dict.items())
 

    @classmethod
    def get(cls, name):
        if name in cls.cache:
            return cls.cache[name]
        else:
            print(f"Sorry, that {cls.class_name.lower()} doesn't exist")
            return



class Brownie(Cupcake):
    """A Brownie"""

    class_name = "Brownie" 
    cache = {}


    def __init__(self, name, price):
        super().__init__(name, "chocolate", price)
        Brownie.cache[self.name] = self



if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')