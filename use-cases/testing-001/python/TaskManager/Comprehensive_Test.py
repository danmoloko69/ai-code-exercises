from datetime import datetime, timedelta

from models import Task, TaskPriority, TaskStatus
from task_priority import calculate_task_score


def test_overdue_task_adds_overdue_due_date_bonus():
    # Arrange: use a known base score and deliberately exclude unrelated modifiers.
    # LOW priority gives a base score of 10.
    # TODO status avoids DONE/REVIEW penalties.
    # Empty tags avoid the tag bonus.
    # Updated 2 days ago avoids the recently-updated bonus.
    task = Task(
        title="Report",
        priority=TaskPriority.LOW,
        due_date=datetime.now() - timedelta(days=2),
        tags=[]
    )
    task.status = TaskStatus.TODO
    task.updated_at = datetime.now() - timedelta(days=2)

    # Act
    score = calculate_task_score(task)

    # Assert: be precise about the expected behavior.
    # Base score: 10
    # Overdue due-date bonus: +35
    expected_score = 45

    assert score == expected_score