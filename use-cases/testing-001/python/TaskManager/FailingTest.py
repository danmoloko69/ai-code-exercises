from datetime import datetime, timedelta
from models import Task, TaskPriority, TaskStatus
from task_priority import calculate_task_score

def test_task_assigned_to_current_user_gets_score_boost():
    task = Task(
        title="Write docs",
        priority=TaskPriority.MEDIUM,
        due_date=None,
        tags=[]
    )
    task.status = TaskStatus.TODO
    task.assigned_to = "alice"
    task.updated_at = datetime.now() - timedelta(days=2)

    score = calculate_task_score(task, current_user="alice")

    assert score == 32


def test_task_assigned_to_different_user_does_not_get_score_boost():
    task = Task(
        title="Review docs",
        priority=TaskPriority.MEDIUM,
        due_date=None,
        tags=[]
    )
    task.status = TaskStatus.TODO
    task.assigned_to = "bob"
    task.updated_at = datetime.now() - timedelta(days=2)

    score = calculate_task_score(task, current_user="alice")

    assert score == 20
