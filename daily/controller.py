from daily.service import TaskService, ConfigService, ServerService
from daily.view import View
from daily.command import Command, BehaviorEnum


class Controller:
    def __init__(self):
        self.task_service = TaskService()
        self.config_service = ConfigService()
        self.server_service = ServerService()
        self.view = View()
        self.command = Command()

    def main(self, commands):
        if len(commands) == 0:
            self.__show_home()
        else:
            self.__handle_command(commands)

    def __show_home(self):
        data = self.task_service.get_tasks()
        self.view.load(data).show()

    def __handle_command(self, commands):
        behavior, data = self.command.load(commands).handle()
        if behavior == BehaviorEnum.ADD_TASKS:
            self.task_service.add_tasks(data)
        if behavior == BehaviorEnum.DELETE_TASKS:
            self.task_service.delete_tasks(data)
        if behavior == BehaviorEnum.UPDATE_TASKS:
            self.task_service.update_tasks(data)
        if behavior == BehaviorEnum.FINISH_TASKS:
            self.task_service.finish_tasks(data)
        if behavior == BehaviorEnum.ADD_TASK_STEPS:
            self.task_service.add_task_steps(data)
        if behavior == BehaviorEnum.DELETE_TASK_STEPS:
            self.task_service.delete_task_steps(data)
        if behavior == BehaviorEnum.UPDATE_TASK_STEPS:
            self.task_service.update_task_steps(data)
        if behavior == BehaviorEnum.FINISH_TASK_STEPS:
            self.task_service.finish_task_steps(data)
        if behavior == BehaviorEnum.HELP:
            result = self.config_service.get_help_doc()
            self.view.load(result).print_info()
        if behavior == BehaviorEnum.SET_CONFIG:
            result = self.config_service.set_config(data)
            self.view.load(result).print_info()
        if behavior == BehaviorEnum.GET_CONFIG:
            result = self.config_service.get_config(data)
            self.view.load(result).print_info()
        if behavior == BehaviorEnum.DELETE_CONFIG:
            result = self.config_service.delete_config(data)
            self.view.load(result).print_info()
        if behavior == BehaviorEnum.LIST_CONFIG:
            result = self.config_service.list_config()
            self.view.load(result).print_info()
        if behavior == BehaviorEnum.LOGIN:
            result = self.server_service.login(data)
            self.view.load(result).print_info()
        if behavior == BehaviorEnum.SYNC:
            pass
        if behavior == BehaviorEnum.EXPORT:
            pass
        if behavior == BehaviorEnum.ERROR_COMMAND:
            self.view.load(data).print_info()
