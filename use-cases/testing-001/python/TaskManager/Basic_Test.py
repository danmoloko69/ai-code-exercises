from datetime import datetime, timedelta

from models import Task, TaskPriority, TaskStatus
from task_priority import calculate_task_score

def test_low_priority_todo_task_without_modifiers_gets_base_score():

    no_due_date_modifier = None
    no_tag_modifier = []
    old_update_date = datetime.now() - timedelta(days=2)

    task = Task(
        title="Basic task",
        priority=TaskPriority.LOW,
        due_date=no_due_date_modifier,
        tags=no_tag_modifier
    )

    task.status = TaskStatus.TODO
    task.updated_at = old_update_date

    score = calculate_task_score(task)

    base_score_for_low_priority = 10

    assert score == base_score_for_low_priority