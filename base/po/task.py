import uuid
import time
from enum import Enum


class Task:
    def __init__(self):
        self.task_id = None
        self.status = None
        self.content = None
        self.create_time = None
        self.deadline_time = None
        self.finish_time = None
        self.task_steps = []
        self.index = None

    @staticmethod
    def get_random_task_id():
        return uuid.uuid4().hex

    @staticmethod
    def get_current_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    class Status(Enum):
        CREATE = '0'
        FINISH = '1'
