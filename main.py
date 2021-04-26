from dataclasses import dataclass

# 4/25/21 - 45 minutes invested


# calculate the total to charge a customer at checkout.
# function should take the users state and a list of records* of items to be purchased,
# it should return the total that the user will be charged (including sales tax).

# Let’s limit the states we do business in to Massachusetts. New Hampshire and Maine.
# We will limit the types of goods we sell (in the record type field) to these three for simplicity:
# “Wic Eligible food”, Clothing, and “everything else”

# data class in python, a record or something similar in java – with data
# members but no useful methods, put the basic record class in your file so your tests can create test work.
# The record should have three fields, the item name, the price, and the item type.

# Write automated tests


@dataclass
class Record:
    item_name: str
    item_price: float
    item_type: str


def calculate_total_charge(abbr_state, list_of_records):
    state_tax = {'MA': '0.0625',
                 'NH': '0.0',
                 'VT': "0.06" }

    print(abbr_state, list_of_records.item_type)
    # return 'total that user will be charged'

    # if abbr_state
    # // Code to calculate total user will be charged here
    # remember to check how each state handles each particular item


if __name__ == '__main__':
    new_item = Record('shirt', 1.50, 'Clothing')
    calculate_total_charge('MA', new_item)

    #print(calculate_total_charge(abbr_state=state, items=list_of_food))
