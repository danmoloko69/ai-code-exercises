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

