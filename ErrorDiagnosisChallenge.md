# Exercise: Error Diagnosis Challenge

## Off by One Error (Python)

**Error description and what it means**

- The problem is that the program is trying to access an item in a list that does not axist. It  happens when it tries to acces item 3 specifically which doe not axist. 

**Root causes identification**

- The error happens on in the for loop when the loop tries to get the third item in the list then it crashes.

**Suggest solution**

- The best solution that will help is removing the manual indexing when possible so it stops when it gets to the last items.

**Learning points that could help prevent similar errors**

- Never use manual indexing when it can be avoided 

- Must be able recognise pattern index vs a  display which will be diffferent.

- Python enumerations are a much better way to do it.

-  Use debug techniques like print before accessing a list.

