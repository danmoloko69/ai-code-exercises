# Exercise: Algorithm Deconstruction Challenge

## 1. Task priority sorting and filtering algorithm 

## ** Prompt 1: Understand an Algorithm Through Step-by-Step Analysis **

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

    So task that are lower priority but overdue can outrank a higher-priority task that is not time-sensitive.

* We look at status penalty with completed task being pushed down. Tasks in reviw are also reduced less than completed task. Ensuring that comppleted task never appears at the top of the important list.

* With tagged task they are are boosted up by +8 regardless whether is has more than 1 tag or not. Then if a task was updated within the last day, it will get a +5 boost.

* Whe sorting it start by giving each task a score, then follows with ordering the task from highest score to lowest score. In the sort_task_by_important function the code bulid (score, task) then calls sorted() so bigger score comes first. After sorting it removes away the score and returns only the task in ranked order. The core pattern used is weighted scoring algorithm instead of writing rules it converts factors into points.

* This prompt gave me insight on other methods of implementing a rule based algorithm using simple method line weighted point allocation.

