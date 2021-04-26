from dataclasses import dataclass


# 4/25/21 - 45 minutes invested


@dataclass
class Record:
    item_name: str
    item_price: float
    item_type: str


def calculate_total_charge(abbr_state, list_of_records):
    # Calculate the total to charge a customer at checkout.
    # Function should take the users state and a list of records* of items to be purchased,
    state_tax = {'MA': '0.0625',
                 'NH': '0.0',
                 'VT': "0.06"}

    # print(list_of_records)
    print('\n')

    for each_record in list_of_records:
        print(each_record.item_name, each_record.item_price, each_record.item_type)

    # Types of goods accepted: Wic Eligible food, Clothing, everything else
    # print(abbr_state, list_of_records[2].item_price)
    # print(len(list_of_records))

    # return 'total that user will be charged'
    # It should return the total that the user will be charged (including sales tax).

    # if abbr_state
    # // Code to calculate total user will be charged here
    # remember to check how each state handles each particular item


if __name__ == '__main__':
    pass
    # calculate_total_charge('MA', new_item)
    # print(calculate_total_charge(abbr_state=state, items=list_of_food))
