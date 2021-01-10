import uuid


class TaskStep:
    def __init__(self):
        self.task_step_id = None
        self.task_id = None
        self.status = None
        self.content = None
        self.index = None

    @staticmethod
    def get_random_task_step_id():
        return uuid.uuid4().hex

