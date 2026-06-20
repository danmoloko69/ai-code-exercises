from datetime import datetime, timedelta

from models import Task, TaskPriority, TaskStatus
from task_priority import calculate_task_score


def test_calculate_task_score_low_priority_basic():
    task = Task(
        title="Basic task",
        priority=TaskPriority.LOW,
        due_date=None,
        tags=[]
    )

    task.status = TaskStatus.TODO
    task.updated_at = datetime.now() - timedelta(days=2)

    score = calculate_task_score(task)

    assert score == 10