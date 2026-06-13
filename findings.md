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



Excercise Part 3: Understanding Domain Model

1. Extract domain model:

* Identify the core entity cleases

    - The core entity classes in model.py are TaskPriority, TaskStatus and Task. Then in storage.py we find TaskStorage.

* Look for the business logic related to tasks

    - This is the business logic found in the app.py file which is TaskManager.

* Note any terminology or concepts that seem specific to this application

    - Task, Tags, TaskID, Status workflow, Priority scale and Overdue task.

2. Form initial understanding 

* Write a brief explanation of what you think each entity represent.

    - Task: this is the core item the app manages, it has the title, description, priority, status, due dates, timestamps, completion date and tags. 

    - TaskStatus: an enumiration that represents where a task is in workflow, TODO, IN_PROGRESS, REVIEW and DONE.

    - TaskPriority: an enumiration that determines the tasks importantance, LOW, MEDIUM, HIGH and URGENT.

    - TaskStorage: it handles saving and loading a collection of task from task.json.

* Note any questions or confusion you have about the business logic
    - I need a little clarity about the due_date_str if statement.

4. Test your knowledge:

* Create a glossary of domain terms used in the application.

    - Task: The main item of application can have title, description, stauts, due date, timestamp and tags.

    - TaskID: A unique number generated using UUID used to find a specific task.

    - Title: The short name of the task.

    - Description: This is the short summary about the task.

    - Status: This shows current stage of the task. Can be TODO, IN_PROGRESS, REVIEW and DONE.

    - Priority: The imprtance of the task. Can be LOW, MEDIUM, HIGH and URGENT.

    - Due date: This is the date in which the task need to be completed. Its optional.

    - Overdue task: This are the task that should have been done already.

    - Created at: The timestamp on when the task was created.

    - Updated at: The timestamp showig when its was last changed

    - Complited at: Timestamp showing on when it was complited.

    - Tag: A label used to group certain task.

    - Task manager: Is the aplication that manages task handling like list and updating.

    - Task Storage: This infrastructure is responsible for saving and loading task from task.json.

    - Statistics: A summary of total task, task by priority, overdue task and tasks completed in the last 7 days.

    - Persistance: Saving of task data so it still exist after the program closes. This is in tasks.json.



Exercise Part 4: Practical Application

2. Planning: Based on your understanding from the previous parts:

* Identify which files you would need to modify

    - This will include model.py, cli.py and the main logic app.py with storage not mmodified as it only verifies persistance.

* Outline the changes you would make to implement this rule

    - Firstly on the model.py file I would add a new status ABANDONED

    - Then add a function to check whether a task is over due by 7 days and not of high priority.

    - Then on main logic app.py add a logc that automatically marks old overdue task as abandoned. 

    - The cli.py also will be updated on its status list. This will allow it to filter by new status.

* Note any questions you would ask your team before implementing

    - Should the high priority mean high or also urgent. 

    - Should users be allowed to manually mark task as abandoned. 

    - Should the ovedue for more 7 days mean exactly on the same day or following day

3. Reflection: 

* How did the AI prompts help you understand where and how to implement this feature

    - It starts by explaining the concepts and the business relationship between the components. It validated my understanding before with the questioning. 

* What aspects of the codebase are you still unsure about

    - This would be the cli intergration with the main app.py and the data flow.

* What would be your next steps to deepen your understanding

    - Understanding more on the data flow functionality from the cli to the main app.py logic.


Final Discussion and Reflection

2. Personal Refletion

* Which prompt was most helpful for building your understanding?

    - That would be Prompt 3: Understanding Domain Models and Business Concept because it was the topic I didi not understand the most and I was able to grasp it in less time.

* What would you do differently next time you approach an unfamiliar codebase?

    - Diffenatly follow the steps I have learned above instead of using my old methods of understanding project structure. This would reduce the time it takes to undeerstand the project structure.

* What additional tools or resources would complement the AI prompting approach?

    - Use code  search tools t look for key words and readme files this would make it more easier to go through the structure of the project.