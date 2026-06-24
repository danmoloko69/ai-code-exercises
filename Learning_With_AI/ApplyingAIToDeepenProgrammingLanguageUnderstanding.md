#  Exercise: Applying AI to deepen programming language understanding

## Activity 1: Idiomatic Code Transformation

**Documents 3 key learning from this exercise**

- In my original code I used `try` which is broad and would be much better using helper functions and avoid repeated logic.

- Then some the variables like `prop` could have been given a more clear name like `property_name`

- Other thing I did not pay attention to on the original code was using tuple for `ETHERIUM_CHAIN_PROPERTIES = ()` as they do not channge to it being a list.

## Activity 2: Code Qulity Detective

**Create checklist of the issues identified**

- Avoid broad silent exception lke `except`

- Move hardcore event names into named constant

- Add a return type hint for the function

- Store reepeated value like `transactionHash` in a local variable

- Add test for matching events, missing fields and failed log fetches

- Avoid scanning for  block 0 unless necessary


**Documents 3 keys learning from this exercise**

- So the events list in my code are fixed inside a function. That leads to use not being able to be reused elsewhere. 

- This piece of code uses `contract` without receiving it as an aargument. That makes the code harder to test and reuse.

- So in the code the is also repeated lookups by `log.get()` calls which would be better if it was  stored once. 

## Activity 3: Understanding Language Feature

**Document 3 key learning from this exercise**

- So the feature I chose was metaclasses in python. First thing I learned was usually avoid when when a simpler toools like a decorator can be used.

- Also find out the are different ways to define metaclasses in python like class `MyMeta(type):` or `class MyClass(metaclass=MyMeta):`.

- I also learned that they can automatically register classes when they are defined. This is used for plugin systems or background jobs.

