from enum import Enum
from base.po.task import Task
from base.po.task_step import TaskStep


class Command:
    def __init__(self):
        self.commands = []

    def load(self, commands):
        self.commands = commands
        return self

    def handle(self):
        command1 = self.commands[0]
        if command1 == 'a' or command1 == 'add':
            return self.__handle_add_tasks()
        if command1 == 'd' or command1 == 'delete':
            return self.__handle_delete_tasks()
        if command1 == 'u' or command1 == 'update':
            return self.__handle_update_tasks()
        if command1 == 'f' or command1 == 'finish':
            return self.__handle_finish_tasks()
        if command1 == 't' or command1 == 'task':
            return self.__handle_task()
        return BehaviorEnum.ERROR_COMMAND, 'Error Command: [ ' + command1 + ' ] '

    def __handle_add_tasks(self):
        tasks = []
        for item in self.commands[1:]:
            task = Task()
            task.task_id = task.get_random_task_id()
            task.create_time = task.get_current_time()
            task.content = item
            tasks.append(task)
        return BehaviorEnum.ADD_TASKS, tasks

    def __handle_delete_tasks(self):
        params = sorted(self.commands[1:], reverse=True)
        tasks = []
        for item in params:
            task = Task()
            task.index = item
            tasks.append(task)
        return BehaviorEnum.DELETE_TASKS, tasks

    def __handle_update_tasks(self):
        params = self.commands[1:]
        ids = params[::2]
        contents = params[1::2]
        if len(ids) != len(contents):
            return BehaviorEnum.ERROR_COMMAND, 'Error Command: [ Update params error]'
        tasks = []
        for i in range(len(ids)):
            task = Task()
            task.index = ids[i]
            task.content = contents[i]
            tasks.append(task)
        return BehaviorEnum.UPDATE_TASKS, tasks

    def __handle_finish_tasks(self):
        tasks = []
        for item in self.commands[1:]:
            task = Task()
            task.index = item
            task.finish_time = task.get_current_time()
            tasks.append(task)
        return BehaviorEnum.FINISH_TASKS, tasks

    def __handle_task(self):
        task = Task()
        task.index = self.commands[1]

        command3 = self.commands[2]
        if command3 == 'a' or command3 == 'add':
            return self.__handle_add_task_steps(task)
        if command3 == 'd' or command3 == 'delete':
            return self.__handle_delete_task_steps(task)
        if command3 == 'u' or command3 == 'update':
            return self.__handle_update_task_steps(task)
        if command3 == 'f' or command3 == 'finish':
            return self.__handle_finish_task_steps(task)

    def __handle_add_task_steps(self, task):
        for item in self.commands[3:]:
            task_step = TaskStep()
            task_step.task_step_id = task_step.get_random_task_step_id()
            task_step.content = item
            task_step.create_time = task_step.get_current_time()
            task.task_steps.append(task_step)
        return BehaviorEnum.ADD_TASK_STEPS, task

    def __handle_delete_task_steps(self, task):
        params = sorted(self.commands[3:], reverse=True)
        for item in params:
            task_step = TaskStep()
            task_step.index = item
            task.task_steps.append(task_step)
        return BehaviorEnum.DELETE_TASK_STEPS, task

    def __handle_update_task_steps(self, task):
        params = self.commands[3:]
        ids = params[::2]
        contents = params[1::2]
        if len(ids) != len(contents):
            return BehaviorEnum.ERROR_COMMAND, 'Error Command: [ Update params error]'
        for i in range(len(ids)):
            task_step = TaskStep()
            task_step.index = ids[i]
            task_step.content = contents[i]
            task.task_steps.append(task_step)
        return BehaviorEnum.UPDATE_TASK_STEPS, task

    def __handle_finish_task_steps(self, task):
        for item in self.commands[3:]:
            task_step = TaskStep()
            task_step.index = item
            task_step.finish_time = task_step.get_current_time()
            task.task_steps.append(task_step)
        return BehaviorEnum.FINISH_TASK_STEPS, task


BehaviorEnum = Enum('BehaviorEnum', (
    'ERROR_COMMAND', 'ADD_TASKS', 'DELETE_TASKS', 'UPDATE_TASKS', 'FINISH_TASKS',
    'ADD_TASK_STEPS', 'DELETE_TASK_STEPS', 'UPDATE_TASK_STEPS', 'FINISH_TASK_STEPS'))
