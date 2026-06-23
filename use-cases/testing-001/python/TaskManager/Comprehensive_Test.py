from datetime import datetime, timedelta

from models import Task, TaskPriority, TaskStatus
from task_priority import calculate_task_score


def test_overdue_task_adds_overdue_due_date_bonus():

    task = Task(
        title="Report",
        priority=TaskPriority.LOW,
        due_date=datetime.now() - timedelta(days=2),
        tags=[]
    )
    task.status = TaskStatus.TODO
    task.updated_at = datetime.now() - timedelta(days=2)

    score = calculate_task_score(task)

    expected_score = 45

    assert score == expected_score