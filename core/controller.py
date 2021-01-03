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
        if behavior == BehaviorEnum.ERROR_COMMAND:
            self.view.load(data).error()

