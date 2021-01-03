from enum import Enum
from base.po.task import Task

class Command:
    def __init__(self):
        self.commands = []

    def load(self, commands):
        self.commands = commands
        return self

    def handle(self):
        first_command = self.commands[0]
        if first_command == 'a' or first_command == 'add':
            return self.__handle_add_tasks()
        if first_command == 'd' or first_command == 'delete':
            pass
        if first_command == 'u' or first_command == 'update':
            pass
        if first_command == 'f' or first_command == 'finish':
            pass
        if first_command == 't' or first_command == 'task':
            pass
        return BehaviorEnum.ERROR_COMMAND, '无效参数: [ ' + first_command + ' ] '

    def __handle_add_tasks(self):
        tasks = []
        for item in self.commands[1:]:
            tasks.append(Task(item))
        return BehaviorEnum.ADD_TASKS, tasks


BehaviorEnum = Enum('BehaviorEnum', ('ERROR_COMMAND', 'ADD_TASKS', 'DELETE_TASKS', 'UPDATE_TASKS', 'FINISH_TASKS'))
