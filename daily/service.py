import functools

from daily.dao import TaskDao, TaskStepDao, OperationDao
from daily.model import Task, TaskStep, Operation
from daily.config import help_doc


class Aspect:
    @staticmethod
    def record_operation(operation_type):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                operation_dao = OperationDao()
                operation = Operation()
                operation.operation_id = Operation.get_random_operation_id()
                operation.status = Operation.Status.NOT_SYNCHRONIZED.value
                operation.type = operation_type
                operation.content = str(args[1])
                operation.operate_time = Operation.get_current_time()
                operation_dao.insert_operation(operation)
                return func(*args, **kw)
            return wrapper
        return decorator


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
            self.add_task(task)

    def delete_tasks(self, tasks):
        self.__fill_tasks_by_index(tasks)
        for task in tasks:
            self.delete_task(task)

    def update_tasks(self, tasks):
        self.__fill_tasks_by_index(tasks)
        for task in tasks:
            self.update_task_content(task)

    def finish_tasks(self, tasks):
        self.__fill_tasks_by_index(tasks)
        self.__reverse_task_status(tasks)
        for task in tasks:
            if task.status == Task.Status.CREATE.value:
                task.finish_time = None
            self.finish_task(task)

    def add_task_steps(self, task):
        self.__fill_task_by_index(task)
        for task_step in task.task_steps:
            task_step.task_id = task.task_id
            self.add_task_step(task_step)

    def delete_task_steps(self, task):
        self.__fill_task_by_index(task)
        for task_step in task.task_steps:
            self.delete_task_step(task_step)

    def update_task_steps(self, task):
        self.__fill_task_by_index(task)
        for task_step in task.task_steps:
            self.update_task_step(task_step)

    def finish_task_steps(self, task):
        self.__fill_task_by_index(task)
        self.__reverse_task_step_status(task)
        for task_step in task.task_steps:
            if task_step.status == TaskStep.Status.CREATE.value:
                task_step.finish_time = None
            self.finish_task_step(task_step)

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

    @staticmethod
    def get_help_doc():
        return help_doc

    @Aspect.record_operation(Operation.Type.ADD_TASK.value)
    def add_task(self, task):
        self.task_dao.insert_task(task)

    @Aspect.record_operation(Operation.Type.DELETE_TASK.value)
    def delete_task(self, task):
        self.task_dao.delete_task(task.task_id)

    @Aspect.record_operation(Operation.Type.UPDATE_TASK.value)
    def update_task_content(self, task):
        self.task_dao.update_task_content(task)

    @Aspect.record_operation(Operation.Type.UPDATE_TASK.value)
    def finish_task(self, task):
        self.task_dao.update_task_status_and_finish_time(task)

    @Aspect.record_operation(Operation.Type.ADD_TASK_STEP.value)
    def add_task_step(self, task_step):
        self.task_step_dao.insert_task_step(task_step)

    @Aspect.record_operation(Operation.Type.DELETE_TASK_STEP.value)
    def delete_task_step(self, task_step):
        self.task_step_dao.delete_task_step(task_step)

    @Aspect.record_operation(Operation.Type.UPDATE_TASK_STEP.value)
    def update_task_step(self, task_step):
        self.task_step_dao.update_task_step_content(task_step)

    @Aspect.record_operation(Operation.Type.UPDATE_TASK_STEP.value)
    def finish_task_step(self, task_step):
        self.task_step_dao.update_task_step_status_and_finish_time(task_step)
