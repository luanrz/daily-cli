from core.dao import TaskDao, TaskStepDao
from base.po.task import Task
from base.po.task_step import TaskStep


class Service:
    def __init__(self):
        self.task_dao = TaskDao()
        self.task_step_dao = TaskStepDao()

    def get_tasks(self):
        all_task = self.task_dao.find_all_task()
        for task in all_task:
            task.task_steps = self.task_step_dao.find_all_task_step_by_task_id(task.task_id)
        return self.__filter_today_tasks(all_task)

    def __filter_today_tasks(self, all_tasks):
        filtered_tasks = list(filter(self.__should_task_shown, all_tasks))
        return filtered_tasks

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
            if task.status == Task.Status.FINISH.value:
                self.task_dao.update_task_finish_time(task)
            if task.status == Task.Status.CREATE.value:
                task.finish_time = None
                self.task_dao.update_task_finish_time(task)

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
            if task_step.status == TaskStep.Status.FINISH.value:
                self.task_step_dao.update_task_step_finish_time(task_step)
            if task_step.status == TaskStep.Status.CREATE.value:
                task_step.finish_time = None
                self.task_step_dao.update_task_step_finish_time(task_step)

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
            if full_task.status == Task.Status.CREATE.value:
                task.status = Task.Status.FINISH.value
            if full_task.status == Task.Status.FINISH.value:
                task.status = Task.Status.CREATE.value
        return tasks

    def __reverse_task_step_status(self, task):
        full_task = self.get_tasks()[int(task.index) - 1]
        for task_step in task.task_steps:
            full_task_step = full_task.task_steps[int(task_step.index) - 1]
            if full_task_step.status == TaskStep.Status.CREATE.value:
                task_step.status = TaskStep.Status.FINISH.value
            if full_task_step.status == TaskStep.Status.FINISH.value:
                task_step.status = TaskStep.Status.CREATE.value
        return task

    @staticmethod
    def __should_task_shown(task):
        is_toddy = Service.__is_today(task.create_time)
        is_undone = task.status == Task.Status.CREATE.value
        return is_toddy or is_undone

    @staticmethod
    def __is_today(create_time):
        today_time = Task.get_current_time()
        today_date_list = today_time.split(" ")[0].split("-")
        create_date_list = create_time.split(" ")[0].split("-")
        is_year_equal = int(today_date_list[0]) == int(create_date_list[0])
        is_month_equal = int(today_date_list[1]) == int(create_date_list[1])
        is_day_equal = int(today_date_list[2]) == int(create_date_list[2])
        return is_year_equal and is_month_equal and is_day_equal
