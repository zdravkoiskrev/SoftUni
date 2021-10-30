from project.task import Task


class Section:

    def __init__(self, name,):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        counter = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                counter += 1
        return f"Cleared {counter} tasks."

    def view_section(self):
        result = f"Section {self.name}:"

        for task in self.tasks:
            result += "\n"
            result += task.details()

        return result

