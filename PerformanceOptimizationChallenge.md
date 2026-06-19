# Exercise: Perfomance Optimization Challenge 

## Slow Code Analysis: Python data processing function


**Measurement of perfomance before changes I made.**

- So I ran the code and it took about 20 minutes to process from 1 to 401 products.

**Document your optimization process, results, and key learnings**

- So what happens is that the `for i in range(len(products)):` and `for j in range(len(products)):` creates 25 million iteratios for 5000 products. Instead of looping over every `, j` on check current one using `for j in range(i + 1, len(products)):`.

- 