# Exercise: Algorithm Deconstruction Challenge

## 1. Task priority sorting and filtering algorithm 

**Prompt 1: Understand an Algorithm Through Step-by-Step Analysis**

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


**Prompt 2: Decipher Code with Unclear Intent or Poor Documentation**

* With "get_top_priority_task" sounding like it only looks for at task priority but actually considers due date, status, tags and recent updates too.

* So for better naming some function can be changed from for example "calculation_task_score" can be "calculating_task_importance_score", "sort_task_by_importance" to "rank_tasks_by_importance" and "get_top_priority_task" to "get_highest_priority_tasks". 

* Other possible pattern techniques the algorithm can use is the sort-derived-key pattern that calculates a value from each object and sorts by that values. 

* Well for commenting certain function could have more in detail comments:

    - **def calculate_task_score(task):**

    """

    Compute a numeric importance score for a task.
    
    The score is used for ranking tasks in priority order. Higher scores indicate
    tasks that should appear earlier. The score combines explicit priority, due
    date urgency, workflow status, special tags, and recent activity.
    
    Completed tasks are penalized heavily so they usually fall below active work.
    Tasks in review are penalized slightly because they may need less attention
    than tasks still in progress.

    """

    - **def sort_tasks_by_importance(tasks):**

    """

    Return tasks ordered from most important to least important.

    Each task is scored once using calculate_task_score(), then the tasks are
    sorted by that score in descending order.

    """

    - **def get_top_priority_tasks(tasks):**

    """

    Return the highest-ranked tasks according to the task importance score.
    
    By default, this returns the top 5 tasks after applying the same ranking
    rules used by sort_tasks_by_importance().

    """



**Prompt 3: Understand Complex Logic and Control Flow**

* In this particular algorithm there are no loops except for the tags for scoring and sorting statement. What I found are the nested if statement for task due date and other simple if statement.

calculate_task_score(task)

Start

  |

  v

Look up task.priority in priority_weights

  |

  v

score = priority_weight * 10

  |

  v

Does task have a due_date?

  |-- no --> skip due-date scoring

  |

  |-- yes

        |

        v

    Calculate days_until_due

        |
        
        |-- days_until_due < 0  --> add 35

        |-- days_until_due == 0 --> add 20

        |-- days_until_due <= 2 --> add 15

        |-- days_until_due <= 7 --> add 10

        |-- otherwise           --> add 0

  |

  v

Check task.status

  |

  |-- DONE   --> subtract 50

  |-- REVIEW --> subtract 15

  |-- other  --> subtract 0

  |

  v

Does task have any tag in ["blocker", "critical", "urgent"]?

  |

  |-- yes --> add 8

  |-- no  --> add 0

  |

  v

Was task updated less than 1 day ago?

  |

  |-- yes --> add 5

  |-- no  --> add 0

  |

  v

Return final score

* With the refactored version breaks the original scoring logic into small helper functions. Where each helper is responsible task score that might change like get_priority_score that handles score from priority, get_due_date_score that adds urgency points for overdue or soon dues date, get_status_score that subtracts point for task that are done or in review, get_tag_score thats adds a small boots for important tags like critical and urgent and get_recent_activity_score that adds points recently updated task.
Then the calculator_task_score simply adds all those together making it easier to read.

* Potential bugs are that days_until_due = (task.due_date - datetime.now()).days the .days property rounds down based on full 24-hour period. So a task due later today might produce 0 and a task due tomorrow in less than 24 hours might also produce a 0.

* The biggest key desicion priority as it crates base scores. Then due date follows as overdue task can get +35 meaning a low ovedue task will out rank high task. Then status and tags with lower impact, completed task be demoted to the buttom of the list.