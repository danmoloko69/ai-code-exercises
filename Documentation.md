Exercise Part 1: Understanding Project Structure

2. Form initial understanding:

* Write best guess aboout how the codebase is orginised.

- I think the Task Manager project is a application that crates, list and prioritises task base on their due date. After the stats function gathered information on task completed in the 7 day, status and priority.

* List the technologies and frameworks you think it uses.

- The are standard python libraries used which is datetime and timedelta for time management and argparse for CLI argument parsing.

* Identify what you think are the main components.

- I think it would be the TaskManager with its components like models.py to define the data structure, storage.py for loading task, cli.py dtermines the command line interface.

3. Apply the Project Structure Prompt:

* Compare the AI's analysis with your own observation.

- The AI clerified that Task Manager project is a command-line task management app, not only a creating task and list and due-date prioritization. It also update, tag, delete, and inspect tasks. Tasks can have a title and description, priority: LOW, MEDIUM, HIGH, URGENT, a status: todo, in_progress, review, done and an optional due date. With tags created/updated/completed timestamps.

- The liabrary I stated are correct but it uses even more like json fro saving and loading task, os to check whether the storage files axist, uuid to generate unique task IDs and enum for task priority and staus values.

- It also explains the main components models.py, storage.py, cli.py and app.py.

4. Documnet your findings:

* Record any misconceptions you had.

- I did not fully explain the logic of the application. Also did not list all the tools used.

* Note important entry points and architectural patterns identified.

- AI stated the main user entry point is cli.py specifically main function. The main apllication logic entry point is task manager.

* List the key components and their responsibility.

- cli.py this handles user input from the command line. Like defines create, list, status, delete and stats using argparse.

- app.py contains the main logic in TaskManager class. Coordinates creating, updating, tagging and calculating statistics for task.

- models.py defines the core data structure: Task, TaskPriority, TaskStatus. This is where task fields and task behaviour like mark_as_done() and is_overdue() live.

- storage.py this handles persistance. Laod task from tasks.json, save task back to json, and provides methods to add, update, delete and retrieve tasks.


Exercise Part 2: Finding Feature Implementation

2. Form a hypothesis:

* Based on your initial search, write down where you think task data export functionality might belong

- I think it would belong to the cli.py, app.py, storage.py and model.py components as they depend on each other. 

* Note which existing comoponents might need to be modified.

- I think cli.py will have to add export command and app.py in the logic we will also have to add export to CSV. 

* List search  terms used and files you found.

- I use the CSV extention files name which I expected to be completely inaccurate.

4. Document your findings:

* Map out where in the codebase you would implement this new feature.

- Firstly in the CLI entry point I will add export command maybe near the list and the stats commands.

- The main export logic would belong to the app.py the TaskManager class. This would be in a form of method that decide which task to export

- From the storage.py, data will be pulled but it will not be responsible for formating the CSV files as it used for persistance and loading task.

- Models.py file that defines what current task actually contain will be important for the exporting feature.

* Note related components that would be affected.

- This are the componets mentioned above cli.py, app.py, storage.py, models.py

*  Outline a plan for how you would approach implimenting the export feature.

- I will look at how the cli calls TaskManager from the app.py file and how app.py retrieves information from the storage.py file. 

- Determine the best location for the for the export command in the cli.py and add it.

- After look in app.py logic and where to add the exprt logic method. It can reuse the list_task().

- Then convert task objects into CSV rows. This will convert into a readable string. Use the CSV module csv.DictWriter instead of manually joining.

- Then from the cli.py call the new TaskManager.export_task_to_csv() method. Then test I will then test method if works.



