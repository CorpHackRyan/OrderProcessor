# Calculate the total to charge a customer at checkout based on which state its purchased from and if the item is
# eligible to be taxed.

from dataclasses import dataclass
# 4/24/21 - 10 mins
# 4/25/21 - 45 minutes invested
# 4/26/21 - 1st sesh: 1 hr 15 mins,
#           2nd sesh: 25 mions


@dataclass
class Record:
    item_name: str
    item_price: float
    item_type: str


def calculate_total_charge(abbr_state, list_of_records):

    # Function should take the users state and a list of records* of items to be purchased,
    state_tax = {'MA': '0.0625',
                 'VT': "0.06"}
    total_cost = 0.0
    print('\n')

    # Types of goods accepted: Wic Eligible food, Clothing, everything else
    # 'Clothing' is tax exempt in NH and VT. Clothing is taxed in MA after 175$.
    # '(WIC) Grocery' is exempt from all states
    # 'Everything else' is taxed by VT and MA and NOT NH.

    # NH = tax exempt from: ALL
    # VT = tax exempt from: Clothing, WIC
    # MA = tax exempt from: Clothing(past $175), WIC

    for each_record in list_of_records:
        if abbr_state == "NH":
            total_cost = total_cost + each_record.item_price

        elif each_record.item_type == "Clothing":
            total_cost = total_cost + (each_record.item_price * state_tax[abbr_state])

        elif each_record.item_type == "VT":
            pass
            # print(each_record.item_name, each_record.item_price, each_record.item_type)
        total_cost = total_cost + each_record.item_price

    print('Total cost is: $', total_cost)

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
