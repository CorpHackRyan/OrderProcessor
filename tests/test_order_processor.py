# Invite your instructor to the github project.
# Include a readme.md that tells me what your production function is and how to run your tests.
# Test Good Cases: check the state amounts are correct for each state
# Test Bad Cases: send something bad in, and assert it was bad,
# Test edge cases: garble
# Research other style of automated testing

import order_processor

MA = "MA"
VT = "VT"
NH = "NH"


def test_verify_bad_state():
    new_record1 = order_processor.Record('shirt', 10, 'Clothing')
    new_record2 = order_processor.Record('baby formula', 50, 'Wic Eligible food')
    new_record3 = order_processor.Record('TV', 200, 'everything else')
    all_records = [new_record3, new_record2, new_record1]
    assert (order_processor.calculate_total_charge("BAD STATE", all_records) == -1)

def test_verify_good_states():
    new_record1 = order_processor.Record('pant', 175, 'Clothing')
    new_record2 = order_processor.Record('diaper', 50, 'Wic Eligible food')
    new_record3 = order_processor.Record('pc', 600, 'everything else')
    all_records = [new_record3, new_record2, new_record1]
    assert (order_processor.calculate_total_charge(MA, all_records) == 862.50)
    assert (order_processor.calculate_total_charge(NH, all_records) == 825.00)
    assert (order_processor.calculate_total_charge(VT, all_records) == 861.00)

    for all_recs in all_records:
        # print(all_recs)
        pass

