from enum import Enum

class Status(Enum):
    new = 1
    in_progress = 2
    closed = 3

class Task:
    def __init__(self, id, name, description):
        self.__id = id
        self.__name = name
        self.__description = description
        self.status = Status.new

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class Subtask(Task):
    # have comlex task id
    def __init__(self, id, name, description, parent_id):
        super().__init__(id, name, description)
        self.parent_id = parent_id


class ComplexTask(Task):
    # contains list of subtasks
    def __init__(self, id, name, description):
        super().__init__(id, name, description)
        self.subtasks = []




class TaskManager:

    id_series = 0

    def __init__(self):
        self.tasks = {}
        self.subtasks = {}
        self.complex_tasks = {}


    def __get_and_increment_id(self):
        next_id_value = TaskManager.id_series
        TaskManager.id_series += 1
        return next_id_value


    def create_task(self, name, description):
        current_id = self.__get_and_increment_id()
        new_task = Task(current_id, name, description)
        self.tasks[current_id] = new_task
        return new_task


    def create_subtask(self, task, name, description):
        current_id = self.__get_and_increment_id()
        parent_id = task.get_id()
        new_task = Subtask(current_id, name, description, parent_id)
        self.subtasks[current_id] = new_task
        task.subtasks.append(current_id)
        return new_task

    def create_complex_task(self, complex_task, description):
        current_id = self.__get_and_increment_id()
        new_task = ComplexTask(current_id, complex_task, description)
        self.complex_tasks[current_id] = new_task
        return new_task


    def get_tasks(self):
        ans = []
        for task in self.tasks:
            t_name = self.tasks[task]
            ans.append(t_name)
        return ans

    def get_subtasks(self):
        ans = []
        for task in self.subtasks:
            t_name = self.subtasks[task]
            ans.append(t_name)
        return ans

    def get_complex_tasks(self):
        ans = []
        for task in self.complex_tasks:
            t_name = self.complex_tasks[task]
            ans.append(t_name)
        return ans

    def get_tasks_by_id(self, id):
        return self.tasks.get(id, None)

    def get_subtasks_by_id(self, id):
        return self.subtasks.get(id, None)

    def get_complex_tasks_by_id(self, id):
        return self.complex_tasks.get(id, None)

    def remove_tasks(self):
        self.tasks.clear()

    def remove_subtasks(self):
        self.subtasks.clear()

    def remove_complex_tasks(self):
        self.complex_tasks.clear()
        self.remove_subtasks()

    def remove_task_by_id(self, id):
        self.tasks.pop(id, None)

    def remove_subtask_by_id(self, id):
        subtask = self.get_subtasks_by_id(id)
        parent_task = self.get_complex_tasks_by_id(subtask.parent_id)
        parent_task.subtasks.remove(id)
        self.subtasks.pop(id, None)

    def remove_complex_task_by_id(self, id):
        complex_task = self.get_complex_tasks_by_id(id)
        subtasks = complex_task.subtasks
        for task_id in subtasks:
            self.remove_subtask_by_id(task_id)
        self.complex_tasks.pop(id, None)

    def update_status(self, task):
        if task.get_id() in self.tasks or task.get_id() in self.subtasks:
            new_val = task.status.value + 1
            task.status = Status(new_val)
        elif task.get_id() in self.complex_tasks:
            if len(task.subtasks) == 0:
                new_val = task.status.value + 1
                task.status = Status(new_val)
            else:
                not_started = False
                for sub_id in task.subtasks:
                    subtask = self.get_subtasks_by_id(sub_id)
                    # print(subtask.status)
                    if subtask.status.value != 3:
                        # print(subtask.status.value)
                        if subtask.status.value == 2:
                            task.status = subtask.status
                            break
                        else:
                            not_started = True
                else:
                    if not_started:
                        task.status = Status.new
                    else:
                        task.status = Status.closed

        return task.status


def assertEqual(actual, expected):
    assert actual == expected

def create():
    manager = TaskManager()
    big_task = manager.create_complex_task("do hw", "description")
    subtask1 = manager.create_subtask(big_task, "open copybook", "smth")
    subtask2 = manager.create_subtask(big_task, "write in date", "today is ...")
    stat1 = manager.update_status(big_task)
    manager.update_status(subtask1)
    manager.update_status(subtask2)
    print(subtask1.status, subtask2.status)
    stat2 = manager.update_status(big_task)
    print(stat2)
    manager.update_status(subtask1)
    manager.update_status(subtask2)
    stat3 = manager.update_status(big_task)


create()