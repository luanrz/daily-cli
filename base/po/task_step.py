import uuid


class TaskStep:
    def __init__(self):
        self.task_step_id = uuid.uuid4().hex
        self.task_id = None
        self.status = None
        self.content = None
