# Calculate the total to charge a customer at checkout based on which state its purchased from and if the item is
# eligible to be taxed.

from dataclasses import dataclass
# 4/24/21 - 10 mins
# 4/25/21 - 45 minutes invested
# 4/26/21 - 1st sesh: 1 hr 15 mins,
#           2nd sesh: 25 mions
#           3rd sesh: 25 mins
#           4th sesh:

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
            print('NH')  # works fine

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
                total_cost = total_cost + (total_cost * state_tax[abbr_state])

        elif abbr_state == "VT":
            print("VT was submitted")
        else:
            print(abbr_state, "state is not valid")
            return "State is not valid."

            # print(each_record.item_name, each_record.item_price, each_record.item_type)

        # elif (state doesn't exist, return an error message state isn't valid)


    print('Total cost is: $', round(total_cost, 2))

    # print(len(list_of_records))
    # It should return the total that the user will be charged (including sales tax).


if __name__ == '__main__':
    pass
    # calculate_total_charge('MA', new_item)
    # print(calculate_total_charge(abbr_state=state, items=list_of_food))
