import os


class DefaultConstant:
    DEFAULT_WORK_DIR = os.path.join(os.path.expanduser('~'), '.daily')
    DEFAULT_DATA_FILE = os.path.join(DEFAULT_WORK_DIR, 'daily.db')
    DEFAULT_CONFIG_FILE = os.path.join(DEFAULT_WORK_DIR, 'daily.conf')


class GlobalConfig:
    def __init__(self):
        self.__mkdir_if_not_exist(DefaultConstant.DEFAULT_WORK_DIR)
        self.__data_file_path = DefaultConstant.DEFAULT_DATA_FILE
        self.__data_config_path = DefaultConstant.DEFAULT_CONFIG_FILE

    def get_data_file_path(self):
        return self.__data_file_path

    def get_config_file_path(self):
        return self.__data_config_path

    @staticmethod
    def __mkdir_if_not_exist(path):
        is_exist = os.path.exists(path)
        if not is_exist:
            os.makedirs(path)


help_doc = '''
Manage base data of task:
{a|add} <TASK>...                                    add tasks
{u|update} {<TASK_ID> <TASK>}...                     update tasks
{f|finish} <TASK_ID>...                              finish tasks
{d|delete} <TASK_ID>...                              delete tasks

Manage base data of task step :
{t|task} <TASK_ID> {a|add} <STEP>...                 add task steps
{t|task} <TASK_ID> {u|update} {<STEP_ID> <STEP>}...  update tasks steps
{t|task} <TASK_ID> {f|finish} <STEP_ID>...           finish tasks steps
{t|task} <TASK_ID> {d|delete} <STEP_ID>...           delete task steps

Extend functionality:
{s|sync}                                             synchronize with server
{e|export}                                           export data to markdown
{h|help}                                             show this help info
'''
