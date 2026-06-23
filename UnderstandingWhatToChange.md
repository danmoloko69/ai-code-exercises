# Exercise: Understanding What to Change with AI

## Exercise 1: Code Readability Improvement (Java)

* AI suggestion for improvements name,methods names and codee structure.

- AI suggested eliminate the cryptic naming  in the code like the `Usermsg`  can be `UserMeanager` and `U` that can be `user` etc. 

- Then it identified the security vulnerabilities which is the SQL injection that stores passwords in plain text and  weak email validation that just checks the for `@`. It suggested using the Regular Expression(Regex) that checks the whole format of the email address. 

- It identiffied the the magic numbers and duplications ofusername loopup logic being uploaded to the database anyway. It suggested function and error handlers that ensures not duplications.

* Readability issues the AI identified that I might have missed

- I would have missed the email validation method that lead to an securitty issue. 

## Exercise 2: Function Refactoring (Python)

* Identify how the function can be broken down into smaller more focused function.

- The main function can be split into smaller fucntions like `validate_order()` function that check if order can be processed. Then `calculate_base_price()` that calculates the basee price. Then `calculate_shipping()`one that calculate shipping price. Then `calculate_tax` responsible for tax. Then `process_single_order()`and `process_order` that loops the aggregates result and total revenue. 

* Compare your AI generated refactoring with your own ideas

-  The AI generated refactoring include functions that still have functions that contains multiple processes which makes sense as it groups all validation rulees into 1. As for mine mostly they are separated.

## Exercise 3: Code Duplication Detection (JavaScript)

* Identify the repeated patterns in this code

- In this code the structure for age, income and score netrics is repeated 3 times. With eeach metric that repeats two kinds of work which is calculating the average with a loop and finding the highest value in another loop. 

* AI suggestion for consolidating these patterns 

- AI suggested to create an helper that calculates stats for one field, loop over a  list of field names then builds the result object dynamically. That retuns three copies of anlogic innto one reusable path.

* Evaluate which approach might be most readable for a teaam of junior developers

- The refactored one with an helper it keeps the repeated logic in one place.It stills reads normal, avoids more advance patterns and the main function stays short.  
