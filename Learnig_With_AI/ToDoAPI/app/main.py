from fastapi import FastAPI, HTTPException, Query, status
from typing import List, Optional

from models import TodoCreate, TodoResponse, TodoStatus

app = FastAPI(
    title="Beginner Friendly ToDo API",
    description="A simple FastAPI example for creating, listing, completing, and deleting to-do items.",
    version="0.1.0",
)

# In-memory store for demonstration purposes.
# In a real application, this would be replaced by a database.
todo_items: dict[int, TodoResponse] = {}
next_todo_id = 1


@app.get("/", tags=["root"])
async def read_root():
    """Root endpoint to describe the API."""
    return {
        "message": "Welcome to the beginner-friendly ToDo API",
        "routes": {
            "create": "/todos (POST)",
            "list": "/todos (GET)",
            "complete": "/todos/{todo_id}/complete (PATCH)",
            "delete": "/todos/{todo_id} (DELETE)",
        },
        "documentation": "/docs",
    }


@app.post("/todos", response_model=TodoResponse, status_code=status.HTTP_201_CREATED, tags=["todos"])
async def create_todo(todo: TodoCreate):
    """Create a new to-do item with title, description, and due date."""
    global next_todo_id

    new_todo = TodoResponse(
        id=next_todo_id,
        title=todo.title,
        description=todo.description,
        due_date=todo.due_date,
        status=TodoStatus.pending,
    )
    todo_items[next_todo_id] = new_todo
    next_todo_id += 1
    return new_todo


@app.get("/todos", response_model=List[TodoResponse], tags=["todos"])
async def list_todos(status: Optional[TodoStatus] = Query(
    None,
    description="Optional filter to list only pending or completed to-dos",
)):
    """List all to-do items, optionally filtering by status."""
    todos = list(todo_items.values())
    if status is not None:
        todos = [todo for todo in todos if todo.status == status]
    return todos


@app.patch("/todos/{todo_id}/complete", response_model=TodoResponse, tags=["todos"])
async def complete_todo(todo_id: int):
    """Mark a to-do item as completed."""
    todo = todo_items.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="To-do item not found")
    if todo.status == TodoStatus.completed:
        return todo

    todo.status = TodoStatus.completed
    todo_items[todo_id] = todo
    return todo


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["todos"])
async def delete_todo(todo_id: int):
    """Delete a to-do item by its ID."""
    if todo_id not in todo_items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="To-do item not found")

    del todo_items[todo_id]
    return None
