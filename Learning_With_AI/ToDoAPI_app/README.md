# Beginner Friendly ToDo API

This is a simple FastAPI application that lets you:

- create a to-do item with `title`, `description`, and `due_date`
- list all to-do items
- filter to-do items by `status` (`pending` or `completed`)
- mark a to-do item as completed
- delete a to-do item

## Run the app

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the server from the `ToDoAPI` folder:

```bash
uvicorn app.main:app --reload
```

3. Open the automatic API docs in your browser:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints

- `POST /todos` - create a new to-do item
- `GET /todos` - list all to-do items
- `GET /todos?status=pending` - list only pending items
- `GET /todos?status=completed` - list only completed items
- `PATCH /todos/{todo_id}/complete` - mark an item completed
- `DELETE /todos/{todo_id}` - delete an item

## Example request body

```json
{
  "title": "Buy groceries",
  "description": "Pick up milk, eggs, and bread",
  "due_date": "2026-07-01"
}
```
