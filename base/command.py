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
            pass
        if command1 == 'u' or command1 == 'update':
            pass
        if command1 == 'f' or command1 == 'finish':
            pass
        if command1 == 't' or command1 == 'task':
            return self.__handle_task()
        return BehaviorEnum.ERROR_COMMAND, '无效参数: [ ' + command1 + ' ] '

    def __handle_add_tasks(self):
        tasks = []
        for item in self.commands[1:]:
            task = Task()
            task.content = item
            tasks.append(task)
        return BehaviorEnum.ADD_TASKS, tasks

    def __handle_task(self):
        task = Task()
        task.task_id = self.commands[1]

        command3 = self.commands[2]
        if command3 == 'a' or command3 == 'add':
            return self.__handle_add_task_steps(task)
        if command3 == 'd' or command3 == 'delete':
            pass
        if command3 == 'u' or command3 == 'update':
            pass
        if command3 == 'f' or command3 == 'finish':
            pass

    def __handle_add_task_steps(self, task):
        for item in self.commands[3:]:
            task_step = TaskStep()
            task_step.content = item
            task.task_steps.append(task_step)
        return BehaviorEnum.ADD_TASK_STEPS, task


BehaviorEnum = Enum('BehaviorEnum', (
    'ERROR_COMMAND', 'ADD_TASKS', 'DELETE_TASKS', 'UPDATE_TASKS', 'FINISH_TASKS',
    'ADD_TASK_STEPS', 'DELETE_TASK_STEPS', 'UPDATE_TASK_STEPS', 'FINISH_TASK_STEPS'))
