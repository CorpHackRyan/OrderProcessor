# Write automated tests to thoroughly test the function your are writing above.

# Upload the production and test code to github and invite your instructor to the github project.
# Include a readme.md that tells me what your production function is and how to run your tests.

# Test Good Cases
# Test Bad Cases
# Test edge cases
# Research other style of automated stesting

import main


def test_calculate_total_charge():
    new_record1 = main.Record('shirt', 1.50, 'Clothing')
    new_record2 = main.Record('baby formula', 3.00, 'Wic Eligible food')
    new_record3 = main.Record('TV', 6.00, 'everything else')
    all_records = [new_record3, new_record2, new_record1]

    for all_recs in all_records:
        #print(all_recs)
        pass

    main.calculate_total_charge('MA', all_records)
