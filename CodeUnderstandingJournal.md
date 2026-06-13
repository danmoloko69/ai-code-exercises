Exercise Part 1: Understanding a Specific Feature

1. Recording in your journal:

* The main components involved in task creation/updates

    - The main components are cli user input, app acts as main coordination layer, the models that defines the task status and priority, storage that saves and loads task.

* The execution flow when a task is created/updates
    
    - Starting at the cli.py where the user put in their input to create or update task. The ist calls TaskManager method in app.py.

    - Then the app.py applies the logic by either creating the task trhough the create_task function or updates the status through update_task_status.

    - The the models.py file will provide the Task object for taask creation and status enum for updating the statuses.

    - In the last step the storage.py will save or updates task in task.json.

* How data is stored and retrieved

    - Task are stored using json file which is task.json. When a task is created the TaskManager passes the Task to task storage which is keeps it in an in memory dictionary. Using task ID as the key it can call save() to write all task to json file. Because task has python objects like enum and dates TaskEncoder converts them into a string, number and formatted dates.

    - Then when the ap start again TaskStorage.load() checks weather json exist, read it and ues TaskDecoder to rebuild the save back into TAsk object. Retrieval method then reads into in_memory dictionary.

* Any interesting design paatterns you discovered.

    - Repository like pattern TaskStorage behaves like a small repository that hides how tasks are saved, loaded and updated.


Exercise Part 2: Deepen Understaing Through Guided Questions

1. Recording in your journal:

* Your initial understanding vs. what you discovered.

    - My initial understanding was when a user creates a task and indicates as high priority then goes through to app.py gets dependencies from models.py afte the tasks is recorded to storage with that high priority. And when the get_stats is called by prioritization the task will be included.

    - The I discovered that this code stores and filter priority but does not automatically decide what should be done first.

* The key insights the guided questions helped you uncover.
    
    - The questions helped me uncover why enum are used instead of plain numbers. What would happen if the priority value=99 instead of the enum. Also learned that the priority filter does not sort task returns all of them for that specific priority.

* Any misconceptions you had that were clarified.

    - I initialy thought that any inputs out of the four enum will be ignored but it was clarified that they are prevented by the cli ot rejected with an error.



Exercise Part 3: Mapping Data Flow

1. Recording in your journal:

* 
