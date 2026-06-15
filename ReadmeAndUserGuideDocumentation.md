# Exercise: README and User Guide Documentation

## Prompt 1: Project README Generation

## TaskManagerProject

A lightweight Python task management application using only built-in libraries for maximum portability.

## Description

TaskManagerProject helps users organize daily work by creating tasks with priorities, tags, and due dates. All data is persisted in JSON format. Best practices in Python development with zero external dependencies.

## Features

- **Create/Update/Delete Tasks** - Manage tasks with titles and descriptions
- **Priority Levels** - 4-level priority system (1=lowest, 4=highest)
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
Priority (1-4): 4
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
New priority: 4
New tags: work,urgent,reports
```

### Filter Tasks
```
Enter command: filter
Filter by (tag/priority): priority
Value: 4
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

- **Level 4**: Urgent
- **Level 3**: High
- **Level 2**: Medium
- **Level 1**: LOW

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

# Step-by-Step Guide: Creating a Task

Quick guide to creating tasks in TaskManagerProject.

## Prerequisites

- ✅ Python 3.6+ installed
- ✅ TaskManagerProject downloaded
- ✅ Write permissions in application directory
- ✅ Terminal/Command Prompt access

## Overview

1. Open Terminal/Command Prompt
2. Navigate to application directory
3. Launch application (`python main.py`)
4. Enter task details
5. Verify creation

---

## Step-by-Step Instructions

### Step 1: Open Terminal

**Windows**: Press `Win + R` → type `cmd` → Enter  
**macOS/Linux**: Open Terminal from Applications → Utilities

### Step 2: Navigate to Directory

```bash
# Windows
cd C:\Users\YourName\task-manager\python

# macOS/Linux
cd ~/task-manager/python
```

### Step 3: Launch Application

```bash
python main.py
# or try
python3 main.py
```

### Step 4: Select Create Command

Type `create` and press Enter.

### Step 5: Enter Task Title

```
Task title: Complete project report
```

**Guidelines:**
- Keep concise (2-10 words)
- Use clear language
- Avoid: `< > " | \ / : * ?`
- Examples: ✅ "Complete quarterly report" ❌ "stuff"

### Step 6: Add Description (Optional)

```
Task description: Finish Q1 2024 report with sales data and projections
```

Include context and specific details.

### Step 7: Set Priority (1-5)

```
Priority (1-5, where 1=lowest, 5=highest): 4
```

| Level | Meaning |
|-------|---------|
| **5** | Critical/Urgent (today) |
| **4** | High (this week) |
| **3** | Medium (this month) |
| **2** | Low (nice to have) |
| **1** | Minimal (can defer) |

**Tip**: Be realistic—don't set everything as 5.

### Step 8: Add Tags (Comma-Separated)

```
Tags (comma-separated): work,reports,finance
```

**Guidelines:**
- Use 2-4 tags per task
- Use lowercase
- Separate with commas
- Examples: `frontend,backend` or `urgent,weekly`

### Step 9: Enter Due Date

```
Due date (YYYY-MM-DD): 2024-03-15
```

**Format Requirements:**
- Must use `YYYY-MM-DD` format
- ✅ `2024-03-15` (March 15, 2024)
- ❌ `03/15/2024` (wrong format)
- ❌ `2024-3-15` (missing leading zero)

**Remember**: Always pad single-digit months/days with zeros (e.g., `2024-03-05`)

### Step 10: Confirm Creation

Expected message:
```
✓ Task created successfully!
Task ID: 1
Title: Complete project report
Priority: 4
Tags: work,reports,finance
Due Date: 2024-03-15
```

### Step 11: Verify in List

```
Enter command: list
[1] Complete project report - Priority: 4 - Due: 2024-03-15
```

---

## Complete Example

```
Enter command: create
Task title: Prepare budget proposal
Task description: Create 2024 budget with department breakdowns
Priority (1-5): 5
Tags: finance,planning,budget
Due date (YYYY-MM-DD): 2024-03-10

✓ Task created successfully!
Task ID: 2
```

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| "Python not found" | Try `python3 main.py` or `py main.py` (Windows) |
| "File not found" error | Check you're in correct directory; verify permissions |
| App crashes | Maximize terminal window; avoid special characters |
| Task not saved | Check disk space; verify permissions; restart app |
| Invalid date format | Use `YYYY-MM-DD` only (e.g., `2024-03-05`) |
| Special characters fail | Remove: `< > " \| \ / : * ? { } [ ]` |

---

## Date Format Examples

| Date | Correct | Incorrect |
|------|---------|-----------|
| March 15, 2024 | `2024-03-15` | `03-15-2024` |
| January 5, 2024 | `2024-01-05` | `2024-1-5` |
| December 31, 2024 | `2024-12-31` | `12/31/2024` |

---

## Best Practices

### ✅ Do's
- Use clear, descriptive titles
- Set realistic priorities
- Use 2-4 relevant tags
- Double-check dates before confirming
- Create tasks regularly

### ❌ Don'ts
- Create vague tasks
- Set everything as high priority
- Use too many tags (>5)
- Forget due dates for time-sensitive tasks
- Use special characters that cause issues

---

## Task Creation Checklist

- [ ] Application launched successfully
- [ ] Clear, descriptive title entered
- [ ] Priority level selected (1-5)
- [ ] Relevant tags added (2-4)
- [ ] Due date in `YYYY-MM-DD` format
- [ ] Confirmation message received
- [ ] Task appears in list view

---

## After Creating a Task

Next actions:
- **View tasks**: `list` command
- **Update task**: `update` command + task ID
- **Filter tasks**: `filter` command
- **Delete task**: `delete` command
- **Mark complete**: `update` command

---

## Effective Task Titles

| Bad | Good |
|-----|------|
| "Work stuff" | "Complete Q1 financial report" |
| "Thing to do" | "Review code for feature branch" |
| "Urgent" | "Fix login authentication bug" |

---

## Tag Organization

**Project-based**: `website`, `app`, `report`  
**Category-based**: `frontend`, `backend`, `testing`  
**Time-based**: `urgent`, `weekly`, `monthly`  
**Team-based**: `design`, `marketing`, `engineering`

---

## Tips for Success

1. **Use clear titles** - Anyone should understand task at a glance
2. **Be realistic with priorities** - Reserve 5 for genuine emergencies
3. **Keep tags focused** - 2-4 specific tags work better than 10 generic ones
4. **Double-check dates** - Ensure date is in future and in correct format
5. **Create regularly** - Keep task list updated for better organization

---

## Need Help?

- Check main README.md
- Review application's built-in help
- Test with a simple task first
- Verify all formatting is correct
- Restart app if issues persist

---

**Last Updated**: 2024


## Prompt 3: FAQ Document Generation

# TaskManagerProject - FAQ

Quick answers to common questions about TaskManagerProject.

---

## Getting Started

**Q: What is TaskManagerProject?**  
A: A lightweight Python task manager. Create tasks with priorities, tags, and due dates. All data stored locally in JSON format.

**Q: Is it free?**  
A: Yes, completely free and open-source.

**Q: What systems does it work on?**  
A: Windows, macOS, and Linux (Python 3.6+ required).

**Q: Is my data safe?**  
A: Yes. Data stays locally on your computer. No cloud upload or external storage.

**Q: Can I use it on my phone?**  
A: No, desktop/laptop only. Python 3.6+ required.

---

## Installation

**Q: How do I install TaskManagerProject?**  
A: Download → Verify Python installed → Run `python main.py`

**Q: I'm getting "Python not found" error. What do I do?**  
A: Try `python3 main.py` (Mac/Linux) or `py main.py` (Windows). Or install Python from python.org and check "Add Python to PATH."

**Q: Which Python version do I need?**  
A: Python 3.6 or higher. Check with: `python --version`

**Q: Can I install via pip?**  
A: No, just download and run `python main.py` directly.

---

## Task Creation

**Q: What's required to create a task?**  
A: Only the task title. Description, priority, tags, and due date are optional.

**Q: Title vs. Description—what's the difference?**  
A: Title = short name (2-10 words). Description = detailed info about the task.

**Q: How do I set priority correctly?**  
A: Scale 1-5: 5=critical, 4=high, 3=medium, 2=low, 1=minimal. Don't set everything as 5.

**Q: What are tags and how do I use them?**  
A: Labels to categorize tasks. Use 2-4 per task, comma-separated: `work,urgent,finance`

**Q: What date format should I use?**  
A: Always `YYYY-MM-DD`
- ✅ `2024-03-15` 
- ❌ `03/15/2024` (wrong)
- ❌ `2024-3-15` (missing leading zero)

**Q: Can I skip the due date?**  
A: Yes, it's optional. Press Enter to skip.

**Q: What special characters can I use?**  
A: Avoid: `< > " | \ / : * ? { } [ ]`  
Use: Letters, numbers, spaces, hyphens, underscores, periods.

---

## Task Management

**Q: How do I view all tasks?**  
A: Use `list` command to display all tasks with IDs, titles, priorities, dates, and tags.

**Q: How do I update a task?**  
A: Use `update` command, enter task ID, modify fields as needed.

**Q: Can I change priority/tags after creating?**  
A: Yes, use `update` command and change the field.

**Q: How do I mark a task complete?**  
A: Use `update` command and set status to "completed."

**Q: Can I delete a task?**  
A: Yes, use `delete` command. **Warning**: Deletion is permanent.

**Q: How do I find a specific task?**  
A: Use `filter` command to filter by tag or priority.

---

## Features & Data

**Q: How many tasks can I create?**  
A: Unlimited theoretically, but performance slows with 1000+. Normal use (100-500) is fine.

**Q: Does TaskManagerProject sync across devices?**  
A: No, but you can copy `tasks.json` to another device to use there.

**Q: Can I export my tasks?**  
A: Yes! Tasks are in `tasks.json` (JSON format). Copy the file or open in any text editor.

**Q: Where is task data stored?**  
A: In `tasks.json` file in the application directory. Local, human-readable, portable.

**Q: How do I backup my tasks?**  
A: Copy `tasks.json`: `cp tasks.json tasks_backup.json` (Mac/Linux) or `copy tasks.json tasks_backup.json` (Windows)

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| App won't start | Check Python version; verify directory; check permissions |
| "File not found" | Verify correct directory; check write permissions; create a new task |
| Task not saved | Check disk space; verify permissions; restart app |
| Invalid date format | Use `YYYY-MM-DD` only (e.g., `2024-03-05`) |
| App runs slowly | Delete old tasks; check available RAM; restart app |
| Special characters show as symbols | Use UTF-8 encoding; avoid non-ASCII characters |
| Accidentally deleted task | No recovery in current version; restore from backup if available |

---

## Advanced

**Q: Can I edit tasks.json directly?**  
A: Not recommended for beginners. If you do, maintain valid JSON format or risk corruption.

**Q: Can I import tasks from another app?**  
A: If it exports JSON, convert to TaskManagerProject format and replace `tasks.json`

**Q: Is my data encrypted?**  
A: No, plain text JSON. Keep computer secure; use passwords; encrypt hard drive for sensitive data.

**Q: Can I contribute to the project?**  
A: Yes! Report bugs, suggest features, write code, improve docs. See README for guidelines.

**Q: Where can I get help?**  
A: Check README.md, Task Creation Guide, error messages, or post on the project repository.

---

## Quick Commands Reference

| Command | What It Does |
|---------|-------------|
| `create` | Create a new task |
| `list` | View all tasks |
| `update` | Modify existing task |
| `delete` | Remove a task |
| `filter` | Find tasks by tag/priority |
| `exit` | Quit application |

---

**Still need help?**  
- Review main README.md
- Check Task Creation Guide
- Post questions on repository
- Check error messages for clues

**Last Updated**: 2024  
**Version**: 1.0