# Invite your instructor to the github project.
# Include a readme.md that tells me what your production function is and how to run your tests.
# Test Good Cases: check the state amounts are correct for each state
# Test Bad Cases: send something bad in, and assert it was bad,
# Test edge cases: garble
# Research other style of automated testing

import order_processor

MA = "MA"
NH = "NH"
ME = "ME"


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
    assert (order_processor.calculate_total_charge(ME, all_records) == 867.62)


def test_verify_total_cost_MA():
    new_record1 = order_processor.Record('pant', 100, 'Clothing')
    new_record2 = order_processor.Record('diaper', 50, 'Wic Eligible food')
    new_record3 = order_processor.Record('pc', 400, 'everything else')
    new_record4 = order_processor.Record('shoe', 100, 'Clothing')
    new_record5 = order_processor.Record('tie', 100, 'Clothing')
    new_record6 = order_processor.Record('socks', 100, 'everything else')
    all_records = [new_record3, new_record2, new_record1, new_record6, new_record5, new_record4]
    assert (order_processor.calculate_total_charge(MA, all_records) == 881.25)


def test_verify_total_cost_NH():
    new_record1 = order_processor.Record('peach', 55, 'Wic Eligible food')
    new_record2 = order_processor.Record('pear', 45, 'Wic Eligible food')
    new_record3 = order_processor.Record('rice', 1000, 'Wic Eligible food')
    new_record4 = order_processor.Record('jacket', 2000, 'Clothing')
    new_record5 = order_processor.Record('video games', 10, 'everything else')
    new_record6 = order_processor.Record('monitor', 20, 'everything else')
    all_records = [new_record1, new_record2, new_record3, new_record4, new_record5, new_record6]
    assert (order_processor.calculate_total_charge(NH, all_records) == 3130.00)


def test_verify_total_cost_ME():
    new_record1 = order_processor.Record('apple', 25, 'everything else')
    new_record2 = order_processor.Record('potato', 10, 'Wic Eligible food')
    new_record3 = order_processor.Record('carrots', 500, 'Wic Eligible food')
    new_record4 = order_processor.Record('sneakers', 30, 'Clothing')
    all_records = [new_record1, new_record2, new_record3, new_record4]
    assert (order_processor.calculate_total_charge(ME, all_records) == 568.02)


def test_clothing_below_175_dollars_MA():
    new_record1 = order_processor.Record('jacket', 174, 'Clothing')
    all_records = [new_record1]
    assert (order_processor.calculate_total_charge(MA, all_records) == 174)


def test_clothing_above_175_dollars_MA():
    new_record2 = order_processor.Record('shirts', 176, 'Clothing')
    all_records = [new_record2]
    assert (order_processor.calculate_total_charge(MA, all_records) == 176.06)


def test_verify_no_refund():
    new_record1 = order_processor.Record('sweatshirt', 0, 'Clothing')
    new_record2 = order_processor.Record('soup', 0, 'Wic Eligible food')
    all_records = [new_record1, new_record2]
    assert (order_processor.calculate_total_charge(MA, all_records) == -1)

