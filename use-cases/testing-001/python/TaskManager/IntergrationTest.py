from datetime import datetime, timedelta

from models import Task, TaskPriority, TaskStatus
from task_priority import ( calculate_task_score, sort_tasks_by_importance, get_top_priority_tasks)

def make_task(
    title,
    priority,
    status=TaskStatus.TODO,
    due_date=None,
    tags=None,
    assigned_to=None,
    updated_days_ago=2,
):
    task = Task(
        title=title,
        priority=priority,
        due_date=due_date,
        tags=tags or []
    )
    task.status = status
    task.assigned_to = assigned_to
    task.updated_at = datetime.now() - timedelta(days=updated_days_ago)
    return task


def test_task_priority_workflow_scores_sorts_and_returns_top_tasks():
    current_user = "alice"

    overdue_blocker = make_task(
        title="Overdue blocker",
        priority=TaskPriority.HIGH,
        due_date=datetime.now() - timedelta(days=2),
        tags=["blocker"],
    )

    my_urgent_task = make_task(
        title="My urgent task",
        priority=TaskPriority.URGENT,
        assigned_to=current_user,
        updated_days_ago=0,
    )

    review_task = make_task(
        title="Review task",
        priority=TaskPriority.HIGH,
        status=TaskStatus.REVIEW,
    )

    ordinary_task = make_task(
        title="Ordinary task",
        priority=TaskPriority.LOW,
    )

    tasks = [
        ordinary_task,
        review_task,
        my_urgent_task,
        overdue_blocker,
    ]

    assert calculate_task_score(overdue_blocker, current_user=current_user) == 83
    assert calculate_task_score(my_urgent_task, current_user=current_user) == 77
    assert calculate_task_score(review_task, current_user=current_user) == 25
    assert calculate_task_score(ordinary_task, current_user=current_user) == 10

    sorted_tasks = sort_tasks_by_importance(tasks)

    assert [task.title for task in sorted_tasks] == [
        "Overdue blocker",
        "My urgent task",
        "Review task",
        "Ordinary task",
    ]

    top_tasks = get_top_priority_tasks(tasks, limit=2)

    assert [task.title for task in top_tasks] == [
        "Overdue blocker",
        "My urgent task",
    ]