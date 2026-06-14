# Exercise: Code Documentation

## 1. Task priority score

**Prompt 1: Comprehensive Function Documentation**

* def calculate_task_score(task):

    """
    Calculate a numeric priority score for a task based on several importance factors.

    This function assigns a score to a task by combining its priority level, due date,
    current status, tags, and most recent update time. Higher scores indicate tasks
    that should be treated as more important and shown earlier in priority-based
    task lists.

    Parameters:
        task (Task):
            The task object to evaluate.

            Expected attributes:
            - priority (TaskPriority): The task's priority level.
              Supported values are TaskPriority.LOW, TaskPriority.MEDIUM,
              TaskPriority.HIGH, and TaskPriority.URGENT.

            - due_date (datetime | None): The task's due date.
              If present, tasks due sooner receive a higher score. Overdue tasks
              receive the largest due-date boost.

            - status (TaskStatus): The current status of the task.
              Tasks marked as DONE or REVIEW are reduced in score because they are
              less likely to need immediate active work.

            - tags (list[str]): A list of task tags.
              Tags such as "blocker", "critical", or "urgent" increase the score.

            - updated_at (datetime): The timestamp when the task was last updated.
              Recently updated tasks receive a small score boost.

    Returns:
        int:
            The calculated task priority score.

            A higher score means the task is considered more important. The score
            may be negative if the task is completed or in review, especially when
            it has a low base priority.

    Raises:
        AttributeError:
            Raised if the task object is missing required attributes such as
            priority, due_date, status, tags, or updated_at.

        TypeError:
            Raised if due_date or updated_at is not a datetime-compatible value,
            or if tags is not iterable.

    Example:
        >>> from datetime import datetime, timedelta
        >>> from models import Task, TaskPriority
        >>>
        >>> task = Task(
        ...     title="Fix checkout bug",
        ...     priority=TaskPriority.URGENT,
        ...     due_date=datetime.now() + timedelta(days=1),
        ...     tags=["blocker"]
        ... )
        >>>
        >>> score = calculate_task_score(task)
        >>> print(score)
        88

    Notes:
        - Priority is the base scoring factor:
          LOW = 10, MEDIUM = 20, HIGH = 40, URGENT = 60.

        - Due-date scoring is based on the number of full days between now and
          the due date:
          overdue = +35, due today = +20, due within 2 days = +15,
          due within 7 days = +10.

        - The function uses datetime.now(), so results may change over time.

        - The urgent tag check is case-sensitive. For example, "urgent" matches,
          but "Urgent" or "URGENT" does not.

        - If task.priority is not found in the priority weight mapping, the task
          receives a base priority score of 0.

        - This function does not modify the task object. It only reads task data
          and returns a calculated score.

    """

**Prompt 2: Intent and Logic Explanation**

* Task Priority Score

    The task priority scoring code is designed to calculate how important a task is by assigning it a numeric score. A higher score means the task should be treated as more urgent or important. This score is based on multiple factors, including the task's priority level, due date, current status, tags, and how recently it was updated.

    The main function, `calculate_task_score(task)`, evaluates a single task and returns an integer score. This score can then be used to sort tasks from most important to least important.

* How The Score Is Calculated

    The function begins by assigning a base score from the task's priority.

    - `TaskPriority.LOW` starts with a weight of `1`

    - `TaskPriority.MEDIUM` starts with a weight of `2`

    - `TaskPriority.HIGH` starts with a weight of `4`

    - `TaskPriority.URGENT` starts with a weight of `6`

    This weight is multiplied by `10`, so the actual base scores are:

    - `LOW`: `10`

    - `MEDIUM`: `20`

    - `HIGH`: `40`

    - `URGENT`: `60`

    If the task has an unknown priority, the function uses a default value of `0`.

    After the base priority score is calculated, the function checks whether the task has a due date. Tasks that are due sooner receive extra points because they are more time-sensitive.

    - Overdue tasks receive `+35`

    - Tasks due today receive `+20`

    - Tasks due within the next 2 days receive `+15`

    - Tasks due within the next 7 days receive `+10`

    - Tasks due later than 7 days receive no additional due-date score

    The function then adjusts the score based on task status. Completed tasks are reduced heavily because they usually no longer need active work. Tasks in review are also reduced, but by a smaller amount.

    - `TaskStatus.DONE` subtracts `50`
    
    - `TaskStatus.REVIEW` subtracts `15`

    Next, the function checks the task's tags. If the task contains one of the tags `"blocker"`, `"critical"`, or `"urgent"`, it receives an additional `+8` points. This helps highlight tasks that may affect other work or need immediate attention.

    Finally, the function checks when the task was last updated. If the task was updated less than one day ago, it receives a small freshness boost of `+5`. This keeps recently active tasks more visible in the priority list.

* Sorting Tasks By Importance

    The `sort_tasks_by_importance(tasks)` function uses `calculate_task_score()` to score every task in a list. It creates score-task pairs, sorts them by score from highest to lowest, and then returns only the task objects in sorted order.

    This means that tasks with higher calculated scores appear first.

* Getting The Top Priority Tasks

    The `get_top_priority_tasks(tasks, limit=5)` function builds on the sorting function. It first sorts all tasks by importance, then returns only the first `limit` tasks.

    By default, it returns the top `5` priority tasks.

* Assumptions And Edge Cases

    This code assumes that each task object has the following attributes:

    - `priority`

    - `due_date`

    - `status`

    - `tags`

    - `updated_at`

    If any of these attributes are missing, the code may raise an `AttributeError`.

    The code also assumes that `due_date` and `updated_at` are compatible with `datetime.now()`. If either value is not a valid `datetime` object, the code may raise a `TypeError`.

    There are a few important edge cases to be aware of:

    - Unknown priority values receive a base score of `0`

    - Tag matching is case-sensitive, so `"urgent"` matches but `"Urgent"` does not

    - A completed urgent task may still have a positive score if it is overdue or has urgent tags

    - The function calls `datetime.now()` more than once, so tiny timing differences are possible

    - The `.days` property counts full days, so a task due in less than 24 hours may be treated as due today

* Suggested Inline Comments

    def calculate_task_score(task):
        """Calculate a priority score for a task based on priority, due date, status, tags, and recency."""

        # Assign each priority level a weight. Higher priority means a larger base score.
        priority_weights = {
            TaskPriority.LOW: 1,
            TaskPriority.MEDIUM: 2,
            TaskPriority.HIGH: 4,
            TaskPriority.URGENT: 6
        }

        # Start with the priority-based score.
        # Unknown priorities receive a base score of 0.
        score = priority_weights.get(task.priority, 0) * 10

        # Increase the score for tasks that are due soon or already overdue.
        if task.due_date:
            days_until_due = (task.due_date - datetime.now()).days

            if days_until_due < 0:
                score += 35
            elif days_until_due == 0:
                score += 20
            elif days_until_due <= 2:
                score += 15
            elif days_until_due <= 7:
                score += 10

        # Lower the score for tasks that are finished or already in review.
        if task.status == TaskStatus.DONE:
            score -= 50
        elif task.status == TaskStatus.REVIEW:
            score -= 15

        # Add a small boost for tags that indicate urgent or blocking work.
        if any(tag in ["blocker", "critical", "urgent"] for tag in task.tags):
            score += 8

        # Add a freshness boost for tasks updated within the last day.
        days_since_update = (datetime.now() - task.updated_at).days
        if days_since_update < 1:
            score += 5

        return score

* Potential Improvements

    The original functionality works, but there are a few improvements that could make the code clearer and more reliable.

    One improvement would be to store datetime.now() in a variable once at the start of the function. This would make all time calculations use the exact same reference time.

    "URGENT_TAGS = {"blocker", "critical", "urgent"}". This would make the tag logic easier to reuse and maintain. The tag check could also be made case-insensitive if tags like "Urgent" or "URGENT" should count the same as "urgent".
    
    Finally, tests would be useful for confirming how scores are calculated in different situations, such as overdue urgent tasks, completed tasks, recently updated tasks, and tasks with unknown priority values.