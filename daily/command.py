from enum import Enum
from daily.model import Task, TaskStep, Config, UserAuth


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
        if command1 == 'c' or command1 == 'config':
            return self.__handle_config()
        if command1 == 'l' or command1 == 'login':
            return self.__handle_login()
        if command1 == 's' or command1 == 'sync':
            return BehaviorEnum.SYNC, None
        if command1 == 'e' or command1 == 'export':
            return BehaviorEnum.EXPORT, None
        if command1 == 'h' or command1 == 'help':
            return BehaviorEnum.HELP, None
        return BehaviorEnum.ERROR_COMMAND, 'Error Command: [ \'' + command1 + '\' ] '

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
        return BehaviorEnum.ERROR_COMMAND, 'Error Command: [ \'' + command3 + '\']'

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

    def __handle_config(self):
        params = self.commands[1:]
        command2 = params[0]
        if command2 == 's' or command2 == 'set':
            return self.__handle_set_config()
        if command2 == 'g' or command2 == 'get':
            return self.__handle_get_config()
        if command2 == 'd' or command2 == 'delete':
            return self.__handle_delete_config()
        if command2 == 'l' or command2 == 'list':
            return self.__handle_list_config()
        return BehaviorEnum.ERROR_COMMAND, 'Error Command: [ \'' + command2 + '\']'

    def __handle_set_config(self):
        params = self.commands[2:]
        if len(params) != 2:
            return BehaviorEnum.ERROR_COMMAND, 'Error Command: [ Need two extra param when setting config ]'
        config = Config()
        config.key = params[0]
        config.value = params[1]
        return BehaviorEnum.SET_CONFIG, config

    def __handle_get_config(self):
        params = self.commands[2:]
        if len(params) != 1:
            return BehaviorEnum.ERROR_COMMAND, 'Error Command: [ Need one extra param when getting config ]'
        config = Config()
        config.key = params[0]
        return BehaviorEnum.GET_CONFIG, config

    def __handle_delete_config(self):
        params = self.commands[2:]
        if len(params) != 1:
            return BehaviorEnum.ERROR_COMMAND, 'Error Command: [ Need one extra param when deleting config ]'
        config = Config()
        config.key = params[0]
        return BehaviorEnum.DELETE_CONFIG, config

    def __handle_list_config(self):
        params = self.commands[2:]
        if len(params) != 0:
            return BehaviorEnum.ERROR_COMMAND, 'Error Command: [ Dont need extra param when listing config ]'
        return BehaviorEnum.LIST_CONFIG, None

    def __handle_login(self):
        params = self.commands[1:]
        if len(params) != 2:
            return BehaviorEnum.ERROR_COMMAND, 'Error Command: [ Need two param when login ]'
        user_auth = UserAuth()
        user_auth.username = params[0]
        user_auth.password = params[1]
        return BehaviorEnum.LOGIN, user_auth


class BehaviorEnum(Enum):
    ERROR_COMMAND = 'ERROR_COMMAND'
    ADD_TASKS = 'ADD_TASKS'
    DELETE_TASKS = 'DELETE_TASKS'
    UPDATE_TASKS = 'UPDATE_TASKS'
    FINISH_TASKS = 'FINISH_TASKS'
    ADD_TASK_STEPS = 'ADD_TASK_STEPS'
    DELETE_TASK_STEPS = 'DELETE_TASK_STEPS'
    UPDATE_TASK_STEPS = 'UPDATE_TASK_STEPS'
    FINISH_TASK_STEPS = 'FINISH_TASK_STEPS'
    SET_CONFIG = 'SET_CONFIG'
    GET_CONFIG = 'GET_CONFIG'
    DELETE_CONFIG = 'DELETE_CONFIG'
    LIST_CONFIG = 'LIST_CONFIG'
    LOGIN = 'LOGIN'
    SYNC = 'SYNC'
    EXPORT = 'EXPORT'
    HELP = 'HELP'
