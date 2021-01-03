import uuid
import time


class Task:
    def __init__(self, content):
        self.task_id = uuid.uuid4().hex
        self.create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.content = content
