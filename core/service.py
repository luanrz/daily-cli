from core.dao import TaskDao, TaskStepDao


class Service:
    def __init__(self):
        self.task_dao = TaskDao()
        self.task_step_dao = TaskStepDao()

    def get_tasks(self):
        all_task = self.task_dao.find_all_task()
        for task in all_task:
            task.task_steps = self.task_step_dao.find_all_task_step_by_task_id(task.task_id)
        return all_task

    def add_tasks(self, tasks):
        for task in tasks:
            self.task_dao.insert_task(task)

    def delete_tasks(self, tasks):
        self.__fill_tasks_by_index(tasks)
        for task in tasks:
            self.task_dao.delete_task(task.task_id)

    def update_tasks(self, tasks):
        self.__fill_tasks_by_index(tasks)
        for task in tasks:
            self.task_dao.update_task_content(task)

    def finish_tasks(self, tasks):
        self.__fill_tasks_by_index(tasks)
        self.__reverse_task_status(tasks)
        for task in tasks:
            self.task_dao.update_task_status(task)

    def add_task_steps(self, task):
        self.__fill_task_by_index(task)
        for task_step in task.task_steps:
            task_step.task_id = task.task_id
            self.task_step_dao.insert_task_step(task_step)

    def delete_task_steps(self, task):
        self.__fill_task_by_index(task)
        for task_step in task.task_steps:
            self.task_step_dao.delete_task_step(task_step)
        pass

    def update_task_steps(self, task):
        self.__fill_task_by_index(task)
        for task_step in task.task_steps:
            self.task_step_dao.update_task_step_content(task_step)

    def finish_task_steps(self, task):
        self.__fill_task_by_index(task)
        self.__reverse_task_step_status(task)
        for task_step in task.task_steps:
            self.task_step_dao.update_task_step_status(task_step)

    def __fill_tasks_by_index(self, tasks):
        full_all_task = self.get_tasks()
        for task in tasks:
            full_task = full_all_task[int(task.index) - 1]
            task.task_id = full_task.task_id
        return tasks

    def __fill_task_by_index(self, task):
        full_task = self.get_tasks()[int(task.index) - 1]
        task.task_id = full_task.task_id
        for task_step in task.task_steps:
            if task_step.index is None:
                return task
            task_step.task_step_id = full_task.task_steps[int(task_step.index) - 1].task_step_id
            task_step.task_id = task.task_id
        return task

    def __reverse_task_status(self, tasks):
        full_all_task = self.get_tasks()
        for task in tasks:
            full_task = full_all_task[int(task.index) - 1]
            if full_task.status == '0':
                task.status = '1'
            if full_task.status == '1':
                task.status = '0'
        return tasks

    def __reverse_task_step_status(self, task):
        full_task = self.get_tasks()[int(task.index) - 1]
        for task_step in task.task_steps:
            full_task_step = full_task.task_steps[int(task_step.index) - 1]
            if full_task_step.status == '0':
                task_step.status = '1'
            if full_task_step.status == '1':
                task_step.status = '0'
        return task
