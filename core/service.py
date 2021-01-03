from core.dao import Dao


class Service:
    def __init__(self):
        self.dao = Dao()

    def get_tasks(self):
        return self.dao.find_all_task()

    def add_tasks(self, tasks):
        for task in tasks:
            self.dao.insert_task(task)
