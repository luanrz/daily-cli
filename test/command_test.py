import unittest

from base.command import Command, BehaviorEnum


class CommandTest(unittest.TestCase):
    def setUp(self):
        self.command = Command()

    def test_insert_task_command(self):
        command_insert_tasks = 'a task1 task2'.split(' ')
        behavior, tasks = self.command.load(command_insert_tasks).handle()
        self.assertEqual(BehaviorEnum.ADD_TASKS, behavior)
        self.assertEqual(2, len(tasks))
        self.assertEqual('task1', tasks[0].content)
        self.assertEqual('task2', tasks[1].content)
        self.assertIsNotNone(tasks[0].create_time)
        self.assertIsNotNone(tasks[1].create_time)

    def test_delete_task_command(self):
        command_delete_tasks = 'd 1 2'.split(' ')
        behavior, tasks = self.command.load(command_delete_tasks).handle()
        self.assertEqual(BehaviorEnum.DELETE_TASKS, behavior)
        self.assertEqual(2, len(tasks))
        self.assertEqual('2', tasks[0].index)
        self.assertEqual('1', tasks[1].index)

    def test_update_task_command(self):
        command_update_tasks = 'u 1 task1_new 2 task2_new'.split(' ')
        behavior, tasks = self.command.load(command_update_tasks).handle()
        self.assertEqual(BehaviorEnum.UPDATE_TASKS, behavior)
        self.assertEqual(2, len(tasks))
        self.assertEqual('1', tasks[0].index)
        self.assertEqual('task1_new', tasks[0].content)
        self.assertEqual('2', tasks[1].index)
        self.assertEqual('task2_new', tasks[1].content)

    def test_update_task_command_when_param_not_match(self):
        command_update_tasks = 'u 1 task1_new 2 task2_new 3'.split(' ')
        behavior, msg = self.command.load(command_update_tasks).handle()
        self.assertEqual(BehaviorEnum.ERROR_COMMAND, behavior)
        self.assertEqual('Error Command: [ Update params error]', msg)

    def test_finish_task_command(self):
        command_finish_tasks = 'f 1 2'.split(' ')
        behavior, tasks = self.command.load(command_finish_tasks).handle()
        self.assertEqual(BehaviorEnum.FINISH_TASKS, behavior)
        self.assertEqual(2, len(tasks))
        self.assertEqual('1', tasks[0].index)
        self.assertEqual('2', tasks[1].index)
        self.assertIsNotNone(tasks[0].finish_time)
        self.assertIsNotNone(tasks[1].finish_time)

    def test_insert_task_step_command(self):
        command_insert_task_steps = 't 1 a task_step_1 task_step_2'.split(' ')
        behavior, task = self.command.load(command_insert_task_steps).handle()
        self.assertEqual(BehaviorEnum.ADD_TASK_STEPS, behavior)
        self.assertEqual('1', task.index)
        self.assertEqual(2, len(task.task_steps))
        self.assertEqual('task_step_1', task.task_steps[0].content)
        self.assertEqual('task_step_2', task.task_steps[1].content)
        self.assertIsNotNone(task.task_steps[0].create_time)
        self.assertIsNotNone(task.task_steps[1].create_time)

    def test_delete_task_step_command(self):
        command_insert_task_steps = 't 1 d 1 2'.split(' ')
        behavior, task = self.command.load(command_insert_task_steps).handle()
        self.assertEqual(BehaviorEnum.DELETE_TASK_STEPS, behavior)
        self.assertEqual('1', task.index)
        self.assertEqual(2, len(task.task_steps))
        self.assertEqual('2', task.task_steps[0].index)
        self.assertEqual('1', task.task_steps[1].index)

    def test_update_task_step_command(self):
        command_insert_task_steps = 't 1 u 1 task_step_1_new 2 task_step_2_new'.split(' ')
        behavior, task = self.command.load(command_insert_task_steps).handle()
        self.assertEqual(BehaviorEnum.UPDATE_TASK_STEPS, behavior)
        self.assertEqual('1', task.index)
        self.assertEqual(2, len(task.task_steps))
        self.assertEqual('1', task.task_steps[0].index)
        self.assertEqual('task_step_1_new', task.task_steps[0].content)
        self.assertEqual('2', task.task_steps[1].index)
        self.assertEqual('task_step_2_new', task.task_steps[1].content)

    def test_finish_task_step_command(self):
        command_insert_task_steps = 't 1 f 1 2'.split(' ')
        behavior, task = self.command.load(command_insert_task_steps).handle()
        self.assertEqual(BehaviorEnum.FINISH_TASK_STEPS, behavior)
        self.assertEqual('1', task.index)
        self.assertEqual(2, len(task.task_steps))
        self.assertEqual('1', task.task_steps[0].index)
        self.assertEqual('2', task.task_steps[1].index)
        self.assertIsNotNone(task.task_steps[0].finish_time)
        self.assertIsNotNone(task.task_steps[1].finish_time)
