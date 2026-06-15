# Exercise: README and User Guide Documentation

## Prompt 1: Project README Generation

## TaskManagerProject

A lightweight Python task management application using only built-in libraries for maximum portability.

## Description

TaskManagerProject helps users organize daily work by creating tasks with priorities, tags, and due dates. All data is persisted in JSON format. Best practices in Python development with zero external dependencies.

## Features

- **Create/Update/Delete Tasks** - Manage tasks with titles and descriptions
- **Priority Levels** - 5-level priority system (1=lowest, 5=highest)
- **Tags** - Custom tags for task categorization
- **Due Dates** - Track time-sensitive tasks (YYYY-MM-DD format)
- **Task Filtering** - Sort and filter by priority, tags, or due dates
- **JSON Storage** - Human-readable, easily portable task database
- **Auto-save** - Changes persist automatically to disk

## Requirements

- Python 3.6 or higher
- Windows, macOS, or Linux
- No external dependencies (built-in libraries only)

## Installation

1. **Clone the project**:
   ```bash
   git clone <repository-url>
   cd task-manager/python
   ```

2. **Verify Python**:
   ```bash
   python --version
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## Quick Start

### Create a Task
```
Enter command: create
Task title: Complete project report
Task description: Finish the quarterly report
Priority (1-5): 4
Tags (comma-separated): work,reports
Due date (YYYY-MM-DD): 2024-03-15
```

### List All Tasks
```
Enter command: list
[1] Complete project report - Priority: 4 - Due: 2024-03-15
[2] Review code - Priority: 3 - Due: 2024-03-20
```

### Update a Task
```
Enter command: update
Task ID: 1
New priority: 5
New tags: work,urgent,reports
```

### Filter Tasks
```
Enter command: filter
Filter by (tag/priority): priority
Value: 5
```

## Configuration

### Custom Data File Location

Edit `main.py`:
```python
DATA_FILE = "./custom_path/tasks.json"
```

Or use environment variable:
```bash
export TASK_DB_PATH=/path/to/custom/tasks.json
```

### Priority Levels

- **Level 5**: Critical/Urgent
- **Level 4**: High
- **Level 3**: Medium
- **Level 2**: Low
- **Level 1**: Minimal

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Python not found" | Use `python3 main.py` on macOS/Linux or `py main.py` on Windows |
| "File not found" error | Check directory write permissions and ensure `tasks.json` path exists |
| Tasks not saving | Verify write permissions to data directory and check disk space |
| Corrupted JSON | Validate JSON syntax, restore from backup, or recreate file |
| Special characters display issues | Ensure UTF-8 terminal encoding is enabled |

## Core Commands

| Command | Description |
|---------|-------------|
| `create` | Add a new task |
| `list` | Display all tasks |
| `update` | Modify task properties |
| `delete` | Remove a task |
| `filter` | Filter tasks by priority or tags |
| `exit` | Quit the application |

## Project Structure

```
task-manager/
├── main.py           # Entry point and core logic
├── tasks.json        # Task data storage
├── README.md         # This file
└── LICENSE           # MIT License
```

## Technologies

- **Language**: Python 3.x
- **Data Format**: JSON
- **Dependencies**: None (built-in libraries only)
  - `json` - Data persistence
  - `datetime` - Date/time handling
  - `os` - File operations

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/name`
3. Follow PEP 8 style guidelines
4. Test your changes thoroughly
5. Commit with clear messages
6. Push and create a Pull Request

## License

MIT License - See LICENSE file for details

- ✅ Free to use, modify, and distribute
- ❌ No warranty provided

## Support

For issues or questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review the documentation
3. Open an issue on the repository

## Version History

**v1.0.0** - Initial release with core task management, JSON storage, priority and tag system

---

**Last Updated**: 2024  
**Maintainers**: TaskManagerProject Team


## Prompt 2: Step-by-Step Guide Creation


