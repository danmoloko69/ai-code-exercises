# Exercise: Using AI to help with testing

## Part 1: Understanding What to Test

**Exercise 1.1: Behaviour Analysis**

* List of 5 cases that should be included

- Test base priority if it start with the score that is stated.

- Test for task with an unknown due date should they receive any due date bonus.

- Test recent udated if task updated less than a day ago gets + 5 points.

- Test for task with empty tags if they receive oints.

- Test for task that is overdue but completed if they get oints or not.

**Exercise 1.2: Testing planning**

**Test Dependencies**

- `Task` model from `models.py`
- `TaskPriority` enum from `models.py`
- `TaskStatus` enum from `models.py`
- `datetime` and `timedelta` for creating due dates and update dates

**1. Base Priority Scoring**

**Type:** Unit test

**Behavior:** A task's priority creates the starting score.

**Setup:** Create tasks with no due date, no important tags, a status that does not reduce the score, and an `updated_at` value old enough to avoid the recent update bonus.

**Expected outcomes:**

- `TaskPriority.LOW` should score `10`
- `TaskPriority.MEDIUM` should score `20`
- `TaskPriority.HIGH` should score `40`
- `TaskPriority.URGENT` should score `60`

**2. Due Date Scoring**

**Type:** Unit test

**Behavior:** Tasks due sooner should receive a higher score.

**Setup:** Create tasks with the same priority, status, tags, and update date, but different due dates.

**Expected outcomes:**

- Overdue task should add `35`
- Task due today should add `20`
- Task due within 2 days should add `15`
- Task due within 7 days should add `10`
- Task due more than 7 days away should add `0`

**3. Status Scoring**

**Type:** Unit test

**Behavior:** Completed and review tasks should have lower scores.

**Setup:** Create tasks with the same priority and no due date, no important tags, and no recent update bonus.

**Expected outcomes:**

- `TaskStatus.DONE` should subtract `50`
- `TaskStatus.REVIEW` should subtract `15`
- `TaskStatus.TODO` or `TaskStatus.IN_PROGRESS` should not subtract points

**4. Important Tag Scoring**

**Type:** Unit test

**Behavior:** Certain tags should add a small priority boost.

**Setup:** Create tasks with tags and keep all other scoring factors neutral.

**Expected outcomes:**

- A task with `"blocker"` should add `8`
- A task with `"critical"` should add `8`
- A task with `"urgent"` should add `8`
- A task with all three important tags should still add only `8`

**5. Sorting Tasks By Importance**

**Type:** Unit test

**Behavior:** `sort_tasks_by_importance()` should return tasks from highest score to lowest score.

**Setup:** Create several tasks with clearly different scores.

**Expected outcome:** Tasks should be returned in descending score order.

**6. Recently Updated Task Scoring**

**Type:** Unit test

**Behavior:** Recently updated tasks should receive a freshness boost.

**Setup:** Create one task updated less than 1 day ago and another task updated more than 1 day ago.

**Expected outcomes:**

- Task updated less than 1 day ago should add `5`
- Task updated more than 1 day ago should add `0`

**7. Top Priority Task Limit**

**Type:** Unit test

**Behavior:** `get_top_priority_tasks()` should sort tasks and return only the requested number.

**Setup:** Create more tasks than the limit.

**Expected outcomes:**

- With the default limit, it should return at most `5` tasks
- With `limit=3`, it should return the top `3` tasks
- If fewer tasks exist than the limit, it should return all available tasks in sorted order

**8. No Due Date**

**Type:** Unit test

**Behavior:** A missing due date should not change the score.

**Setup:** Create a task with `due_date = None`.

**Expected outcome:** The task should receive no due-date bonus.

**9. Normal Tags Do Not Boost Score**

**Type:** Unit test

**Behavior:** Only specific tags should increase the score.

**Setup:** Create a task with ordinary tags such as `"frontend"` or `"homework"`.

**Expected outcome:** The task should not receive the `+8` tag boost.

**10. Unknown Priority**

**Type:** Unit test

**Behavior:** Unknown priority values should not crash the function.

**Setup:** Create a task-like object with a priority value that is not in the priority weight mapping.

**Expected outcome:** The base priority score should be `0`.

**11. Case-Sensitive Tags**

**Type:** Unit test

**Behavior:** Tag matching is case-sensitive.

**Setup:** Create a task with `"Critical"` instead of `"critical"`.

**Expected outcome:** The task should not receive the `+8` tag boost.

**12. Completed But Overdue Task**

**Type:** Unit test

**Behavior:** Multiple scoring rules can apply to the same task.

**Setup:** Create a task that is overdue and has status `DONE`.

**Expected outcome:** The task should receive the overdue bonus and the completed-task penalty.


## Part 2: Improving a single Test

**Exercise 2.1: Writing Your First Test**

* Suggested improvements to my test

- Base on the feedback the name of the task can explain more about the task.

- Other suggestion was to make the set up comunicate deliberately excluded modifiers like due date and tags.

- Also I had to make the assertion more informative when it fails and what is expected.

- It was suggested that I also name why it is expects that certain score.

