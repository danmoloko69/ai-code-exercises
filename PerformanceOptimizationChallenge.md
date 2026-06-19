# Exercise: Performance Optimization Challenge 

## Slow Code Analysis: Python data processing function


**Measurement of performance before changes is made.**

- So I ran the code and it took about 20 minutes to process from 1 to 401 products.

**Document your optimization process, results, and key learnings**

- So, what happens is that the `for i in range(len(products)):` and `for j in range(len(products)):` creates 25 million iterations for 5000 products. Instead of looping over every `, j` on check current one using `for j in range(i + 1, len(products)):`.

- For the next improvement It added the min_price and max_price so it does not recalculate them every loop.

- After created the `sort_products = sorted(products, key=lambda product: products['price']) this creates a new list that where products are sorted from cheapest to most expensive. This eliminates the checking for combinations part.

- Then change the `for i in range(len(products));` to `for i in range(len(sorted_products)):` this means loop now uses `sorted_products` that goes through product according to price.

- Then moved the `product1 = products[i]` to `product2 = sorted_products[i]` before this was repeated in the inner loop. Also migrated product2 to use the sorted list so now the inner list compare the current price to the next expensive one. This also showed me how 1 method can change a lot in a code,

- And the most important change is because now products are sorted by price omce this the `product['price'] + product2['price'] . max_price` happens every later product2 will be the same price or more expensive so the is no reason to check, that breaks the inner loop immediately.

- In the last step, removed the duplication checks that verified whether the reverse pair was already saved. Which is now done by the loop: `for j in range(i + 1, len(sorted_products)):` that means product2 comes after 1.

**Measurement of performance after the change is made**

- So now the code goes throungh the whole 5000 products in 3.17 seconds meaning the performance was drastically improved from the initial 20 minutes.

* So overall the code is faster becauese it does less unneccessary work . As now the it sort first that reduces future work. This showed me that the structure of the code really matters if it poor the the app wil be inefficient resulting in very poor result. 



 