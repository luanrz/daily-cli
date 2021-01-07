from core.dao import Dao


class Service:
    def __init__(self):
        self.dao = Dao()

    def get_tasks(self):
        all_task = self.dao.find_all_task()
        for task in all_task:
            task.task_steps = self.dao.find_all_task_step_by_task_id(task.task_id)
        return all_task

    def add_tasks(self, tasks):
        for task in tasks:
            self.dao.insert_task(task)

    def add_task_steps(self, task):
        index = int(task.task_id) - 1
        all_task = self.dao.find_all_task()
        full_task = all_task[index]
        for task_step in task.task_steps:
            task_step.task_id = full_task.task_id
            self.dao.insert_task_step(task_step)
