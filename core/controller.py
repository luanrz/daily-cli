from core.service import Service
from core.view import View
from base.command import Command, BehaviorEnum


class Controller:
    def __init__(self):
        self.service = Service()
        self.view = View()
        self.command = Command()

    def main(self, commands):
        if len(commands) == 0:
            self.__show_home()
        else:
            self.__handle_command(commands)

    def __show_home(self):
        data = self.service.get_tasks()
        self.view.load(data).show()

    def __handle_command(self, commands):
        behavior, data = self.command.load(commands).handle()
        if behavior == BehaviorEnum.ADD_TASKS:
            self.service.add_tasks(data)
        if behavior == BehaviorEnum.DELETE_TASKS:
            self.service.delete_tasks(data)
        if behavior == BehaviorEnum.UPDATE_TASKS:
            self.service.update_tasks(data)
        if behavior == BehaviorEnum.FINISH_TASKS:
            self.service.finish_tasks(data)
        if behavior == BehaviorEnum.ADD_TASK_STEPS:
            self.service.add_task_steps(data)
        if behavior == BehaviorEnum.DELETE_TASK_STEPS:
            self.service.delete_task_steps(data)
        if behavior == BehaviorEnum.UPDATE_TASK_STEPS:
            self.service.update_task_steps(data)
        if behavior == BehaviorEnum.FINISH_TASK_STEPS:
            self.service.finish_task_steps(data)
        if behavior == BehaviorEnum.SYNC:
            pass
        if behavior == BehaviorEnum.EXPORT:
            pass
        if behavior == BehaviorEnum.HELP:
            self.view.load(self.service.get_help_doc()).print_info()
        if behavior == BehaviorEnum.ERROR_COMMAND:
            self.view.load(data).print_info()
