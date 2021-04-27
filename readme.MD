## Summary
_Simple program design using automated tests to calculate the total cost to charge a customer including sales tax._

## Production code

This production code has a single function called calculate_total_charge() that accepts two parameters (a state and list of records). 
This function, when given the proper inputs, will calculate the total to charge a customer at checkout. The total that is charged
to the customer will depend on what type of item which is being purchased and which state they are buying that item in. 

This function will take in 2 parameters. The first parameter is an abbreviated state. Since we are only dealing with
New Hampshire, Maine and Massachusetts, these will be the only 3 abbreviations allowed as input (NH, ME & MA respectively).

The second parameter of this function will take a list of records (using dataclasses) that contain an item type, price and name. 
For the types of goods, the only ones used are: 
- “Wic Eligible food”
- "Clothing"
- “everything else”
## Output
Each state has its own rules for sales tax and this code takes that into account. Some items will be taxed, not taxed 
or taxed when a certain threshold is met. Each states rules are as follows:

- New Hampshire: All items are exempt from sales tax
- Maine: Wic Eligible food is exempt from sales tax. Clothing & everything else is taxed a 5.5%.
- Massachusetts: Wic Eligible food is exempt from sales tax. For clothing, anything over $175 is taxed and everything 
else is taxed at 6.25%.
  
## Tests
This has built in automated testing using pytest and GitHub actions. To run the tests, execute the 
test_order_processor.py script to begin testing. 

## Requirements
You must have dataclasses installed in order to run this code.
