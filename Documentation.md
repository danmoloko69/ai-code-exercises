Exercise Part 1: Understanding Project Structure

2.Form initial understanding:

*Write best guess aboout how the codebase is orginised.

-I think the Task Manager project is a application that crates, list and prioritises task base on their due date. After the stats function gathered information on task completed in the 7 day, status and priority.

*List the technologies and frameworks you think it uses.

-The are standard python libraries used which is datetime and timedelta for time management and argparse for CLI argument parsing.

*Identify what you think are the main components.

-I think it would be the TaskManager with its components like models.py to define the data structure, storage.py for loading task, cli.py dtermines the command line interface.

3.Apply the Project Structure Prompt:

*Compare the AI's analysis with your own observation

-The AI clerified that Task Manager project is a command-line task management app, not only a creating task and list and due-date prioritization. It also update, tag, delete, and inspect tasks. Tasks can have a title and description, priority: LOW, MEDIUM, HIGH, URGENT, a status: todo, in_progress, review, done and an optional due date. With tags created/updated/completed timestamps.

-The liabrary I stated are correct but it uses even more like json fro saving and loading task, os to check whether the storage files axist, uuid to generate unique task IDs and enum for task priority and staus values.

-It also explains the main components models.py, storage.py, cli.py and app.py.

4.Documnet your findings:

*Record any misconceptions you had
-I did not fully explain the logic of the application. Also did not list all the tools used.

*Note important entry points and architectural patterns identified.
-AI stated the main user entry point is cli.py specifically main function. The main apllication logic entry point is task manager.

*List the key components and their responsibility
-cli.py this handles user input from the command line. Like defines create, list, status, delete and stats using argparse.
-app.py contains the main logic in TaskManager class. Coordinates creating, updating, tagging and calculating statistics for task.
-models.py defines the core data structure: Task, TaskPriority, TaskStatus. This is where task fields and task behaviour like mark_as_done() and is_overdue() live.
-storage.py this handles persistance. Laod task from tasks.json, save task back to json, and provides methods to add, update, delete and retrieve tasks.


Exercise Part 2: Finding Feature Implementation

2.Form a hypothesis

*Based on your initial search, write down where you think task data export functionality might belong
-I think it would belong to the cli.py, app.py, storage.py and model.py components as they depend on each other. 

*Note which existing comoponents might need to be modified.
-As each component change other components will also need to be modified for example cli.py 

*List search  terms used and files you found
