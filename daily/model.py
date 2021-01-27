import time
import uuid
import json
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

    def __str__(self) -> str:
        obj = {}
        if self.task_id:
            obj['task_id'] = self.task_id
        if self.status:
            obj['status'] = self.status
        if self.content:
            obj['content'] = self.content
        if self.create_time:
            obj['create_time'] = self.create_time
        if self.deadline_time:
            obj['deadline_time'] = self.deadline_time
        if self.finish_time:
            obj['finish_time'] = self.finish_time
        return json.dumps(obj)


class TaskStep:
    def __init__(self):
        self.task_step_id = None
        self.task_id = None
        self.status = None
        self.content = None
        self.create_time = None
        self.deadline_time = None
        self.finish_time = None
        self.index = None

    @staticmethod
    def get_random_task_step_id():
        return uuid.uuid4().hex

    @staticmethod
    def get_current_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    class Status(Enum):
        CREATE = '0'
        FINISH = '1'

    def __str__(self) -> str:
        obj = {}
        if self.task_step_id:
            obj['task_step_id'] = self.task_step_id
        if self.task_id:
            obj['task_id'] = self.task_id
        if self.status:
            obj['status'] = self.status
        if self.content:
            obj['content'] = self.content
        if self.create_time:
            obj['create_time'] = self.create_time
        if self.deadline_time:
            obj['deadline_time'] = self.deadline_time
        if self.finish_time:
            obj['finish_time'] = self.finish_time
        return json.dumps(obj)


class Operation:
    def __init__(self):
        self.operation_id = None
        self.status = None
        self.type = None
        self.content = None
        self.operate_time = None

    class Status(Enum):
        NOT_SYNCHRONIZED = '0'
        SYNCHRONIZED = '1'

    class Type(Enum):
        ADD_TASK = 'ADD_TASK'
        UPDATE_TASK = 'UPDATE_TASK'
        DELETE_TASK = 'DELETE_TASK'
        ADD_TASK_STEP = 'ADD_TASK_STEP'
        UPDATE_TASK_STEP = 'UPDATE_TASK_STEP'
        DELETE_TASK_STEP = 'DELETE_TASK_STEP'

    @staticmethod
    def get_random_operation_id():
        return uuid.uuid4().hex

    @staticmethod
    def get_current_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


class Config:
    def __init__(self):
        self.key = None
        self.value = None


class UserAuth:
    def __init__(self):
        self.username = None
        self.password = None


class User:
    def __init__(self):
        self.username = None
        self.user_id = None
        self.jwt = None
