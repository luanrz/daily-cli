import uuid
import time


class TaskStep:
    def __init__(self, task_id, content):
        self.task_step_id = uuid.uuid4().hex
        self.create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.task_id = task_id
        self.content = content
