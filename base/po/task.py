import uuid
import time


class Task:
    def __init__(self):
        self.task_id = uuid.uuid4().hex
        self.status = None
        self.content = None
        self.create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.deadline_time = None
        self.task_steps = []
