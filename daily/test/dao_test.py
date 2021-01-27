import unittest

from daily.model import Task, TaskStep, User
from daily.dao import TaskDao, TaskStepDao, UserDao


class DaoTest(unittest.TestCase):
    def setUp(self):
        self.task_dao = TaskDao()
        self.task_step_dao = TaskStepDao()
        self.user_dao = UserDao()

    def test_manage_task(self):
        task = Task()
        task.task_id = task.get_random_task_id()
        task.create_time = task.get_current_time()

        task.content = 'This is a task'
        self.task_dao.insert_task(task)
        new_task = self.task_dao.find_task_by_task_id(task.task_id)
        self.assertEqual(task.content, new_task.content)
        self.assertIsNotNone(new_task.create_time)

        task.content = 'This is a new task'
        self.task_dao.update_task_content(task)
        new_task = self.task_dao.find_task_by_task_id(task.task_id)
        self.assertEqual(task.content, new_task.content)

        task.status = Task.Status.FINISH.value
        task.finish_time = task.get_current_time()
        self.task_dao.update_task_status_and_finish_time(task)
        new_task = self.task_dao.find_task_by_task_id(task.task_id)
        self.assertEqual(task.status, new_task.status)
        self.assertIsNotNone(new_task.finish_time)

        self.task_dao.delete_task(task.task_id)
        new_task = self.task_dao.find_task_by_task_id(task.task_id)
        self.assertIsNone(new_task)

    def test_manage_task_step(self):
        task_step = TaskStep()
        task_step.task_step_id = TaskStep.get_random_task_step_id()
        task_step.task_id = Task.get_random_task_id()
        task_step.create_time = TaskStep.get_current_time()

        task_step.content = 'This is a task step'
        self.task_step_dao.insert_task_step(task_step)
        new_task_step = self.task_step_dao.find_task_step_by_task_step_id(task_step.task_step_id)
        self.assertEqual(task_step.content, new_task_step.content)
        self.assertIsNotNone(new_task_step.create_time)

        task_step.content = 'This is a new task step'
        self.task_step_dao.update_task_step_content(task_step)
        new_task_step = self.task_step_dao.find_task_step_by_task_step_id(task_step.task_step_id)
        self.assertEqual(task_step.content, new_task_step.content)

        task_step.status = TaskStep.Status.FINISH.value
        task_step.finish_time = task_step.get_current_time()
        self.task_step_dao.update_task_step_status_and_finish_time(task_step)
        new_task_step = self.task_step_dao.find_task_step_by_task_step_id(task_step.task_step_id)
        self.assertEqual(task_step.status, new_task_step.status)
        self.assertIsNotNone(new_task_step.finish_time)

        self.task_step_dao.delete_task_step(task_step)
        new_task_step = self.task_step_dao.find_task_step_by_task_step_id(task_step.task_step_id)
        self.assertIsNone(new_task_step)

    def test_user(self):
        user = User()
        user.user_id = 'user_id'
        user.username = 'username'
        user.jwt = 'jwt'

        self.user_dao.insert_user(user)
        new_user = self.user_dao.find_user()
        self.assertIsNotNone(new_user)
        self.assertEqual(new_user.user_id, user.user_id)
        self.assertEqual(new_user.username, user.username)
        self.assertEqual(new_user.jwt, user.jwt)

        self.user_dao.delete_user()
        new_user = self.user_dao.find_user()
        self.assertIsNone(new_user)
