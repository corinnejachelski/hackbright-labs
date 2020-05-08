############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, 
                is_bestseller):
        """Initialize a melon."""
        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code 


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", "Muskmelon", 1998, "green", True, True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    casaba = MelonType("cas", "Casaba", 2003, "orange", False, False)
    casaba.add_pairing("strawberry")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    casaba = MelonType("cas", "Casaba", 2003, "orange", False, False)
    casaba.add_pairing("strawberry")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", "Crenshaw", 1996, "green", False, False)
    casaba.add_pairing("proscuitto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("yw", "Yellow Watermelon", 2013, "yellow", 
                                 False, True)
    casaba.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:

        name = melon.name
        pairings = str(melon.pairings)

        print(f"{name} pairs with:") 

        for pairing in melon.pairings:
            if pairings == []:
                pairings = "None"
            else:
                pairings[0]

            print(f"- {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    d = {}

    for melon in melon_types:
        d[melon.code] = melon

    return d
    

############
# Part 2   #
############

class Melon(object):

    def __init__(self, melon_type, shape_rating, color_rating, field_num, harvester):
        """A melon in a melon harvest."""
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_num = field_num
        self.harvester = harvester


    def is_sellable(self):

        sellable = self.shape_rating > 5 and self.color_rating > 5 and self.field_num != 3
        
        return sellable


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)

    melons = []

    melons.append(Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila'))
    melons.append(Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila'))
    melons.append(Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila'))
    melons.append(Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila'))
    melons.append(Melon(melons_by_id['cren'], 8, 9, 35, 'Michael'))
    melons.append(Melon(melons_by_id['cren'], 8, 2, 35, 'Michael'))
    melons.append(Melon(melons_by_id['cren'], 2, 3, 4, 'Michael'))
    melons.append(Melon(melons_by_id['musk'], 6, 7, 4, 'Michael'))
    melons.append(Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila'))

    return melons       

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            print(f"Harvested by {melon.harvester} from Field {melon.field_num} (CAN BE SOLD)")
        else:
            print(f"Harvested by {melon.harvester} from Field {melon.field_num} (NOT SELLABLE")


print(get_sellability_report(make_melons(make_melon_types())))
