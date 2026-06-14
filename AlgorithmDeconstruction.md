Exercise: Algorithm Deconstruction Challenge

1. Task priority sorting and filtering algorithm 

* This algorithm assing each task a score based on the task priority, due date if assigned and task completion status. Then sorts tasks from the highest score to lowest.

* It start by giving task score based on priority:
    Low = 10
    Medium = 20
    High = 40
    Urgent =60

* Moving to due date it checks whether a task has a due date and if it does it gives it an extra points based on urgency:
    Overdues = +35
    Due today = +20
    Due in 1-2 days = +15
    Due within week = +10
    No due date = +0