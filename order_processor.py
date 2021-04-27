from dataclasses import dataclass


@dataclass
class Record:
    item_name: str
    item_price: float
    item_type: str


def calculate_total_charge(abbr_state, list_of_records):
    # Types of goods accepted: Wic Eligible food, Clothing, everything else
    # NH = tax exempt from: Clothing, WIC, everything else
    # ME = tax exempt from: WIC
    # MA = tax exempt from: Clothing (everything after $175 is taxed), WIC

    state_tax = {'MA': 0.0625,
                 'ME': 0.055}
    total_cost = 0.0
    print('\n')

    for each_record in list_of_records:
        if abbr_state == "NH":
            total_cost = total_cost + each_record.item_price

        elif abbr_state == "ME":
            if each_record.item_type == "Wic Eligible food":
                total_cost = total_cost + each_record.item_price
            elif each_record.item_type == "Clothing":
                total_cost = total_cost + (each_record.item_price * state_tax[abbr_state]) + each_record.item_price
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

    total_cost = round(total_cost, 2)
    return total_cost
