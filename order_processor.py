# Calculate the total to charge a customer at checkout based on which state its purchased from and if the item is
# eligible to be taxed.
# 4/24/21 - 10 mins
# 4/25/21 - 45 minutes invested
# 4/26/21 - 1st sesh: 1 hr 15 mins,
#           2nd sesh: 25 mions
#           3rd sesh: 25 mins
#           4th sesh: 25 mins
#           5th sesh:

from dataclasses import dataclass


@dataclass
class Record:
    item_name: str
    item_price: float
    item_type: str


def calculate_total_charge(abbr_state, list_of_records):
    state_tax = {'MA': 0.0625,
                 'VT': 0.06}
    total_cost = 0.0
    print('\n')

    # Types of goods accepted: Wic Eligible food, Clothing, everything else
    # NH = tax exempt from: Clothing, WIC, Everything else
    # VT = tax exempt from: Clothing, WIC
    # MA = tax exempt from: Clothing(everything after $175 is taxed), WIC

    for each_record in list_of_records:
        if abbr_state == "NH":
            total_cost = total_cost + each_record.item_price

        elif abbr_state == "VT":
            if each_record.item_type == "Wic Eligible food":
                total_cost = total_cost + each_record.item_price
            elif each_record.item_type == "Clothing":
                total_cost = total_cost + each_record.item_price
            elif each_record.item_type == "everything else":
                total_cost = total_cost + (each_record.item_price * state_tax[abbr_state]) + each_record.item_price

        elif abbr_state == "MA":
            if each_record.item_type == "Wic Eligible food":
                total_cost = total_cost + each_record.item_price
            elif each_record.item_type == "Clothing":
                if each_record.item_price > 175:
                    taxable_amt = each_record.item_price - 175
                    tax_total = taxable_amt * state_tax[abbr_state]
                    total_cost = total_cost + tax_total + each_record.item_price
                else:
                    total_cost = total_cost + each_record.item_price
            elif each_record.item_type == "everything else":
                total_cost = total_cost + (each_record.item_price * state_tax[abbr_state]) + each_record.item_price

        else:
            print(abbr_state, "State is not valid")
            return -1

    print(total_cost)
    return total_cost



if __name__ == '__main__':
    pass
