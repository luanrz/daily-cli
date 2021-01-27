import os
from configparser import ConfigParser


class DefaultConfig:
    DEFAULT_WORK_DIR_PATH = os.path.join(os.path.expanduser('~'), '.daily')
    DEFAULT_DATA_FILE_PATH = os.path.join(DEFAULT_WORK_DIR_PATH, 'daily.db')
    DEFAULT_CONFIG_FILE_PATH = os.path.join(DEFAULT_WORK_DIR_PATH, 'daily.ini')
    DEFAULT_SERVER_URL = 'https://api.daily.luanrz.cn'

    @staticmethod
    def make_default_work_dir_if_not_exist():
        is_exist = os.path.exists(DefaultConfig.DEFAULT_WORK_DIR_PATH)
        if not is_exist:
            os.makedirs(DefaultConfig.DEFAULT_WORK_DIR_PATH)


class DataConfig:
    def __init__(self):
        DefaultConfig.make_default_work_dir_if_not_exist()
        self.__data_file_path = DefaultConfig.DEFAULT_DATA_FILE_PATH

    def get_data_file_path(self):
        return self.__data_file_path


class CustomConfig:
    def __init__(self):
        DefaultConfig.make_default_work_dir_if_not_exist()
        self.__config_file_path = DefaultConfig.DEFAULT_CONFIG_FILE_PATH
        self.__default_config = {
            'server_url': DefaultConfig.DEFAULT_SERVER_URL
        }

    def set(self, key, value):
        parser = ConfigParser()
        section = parser.default_section
        parser.read(self.__config_file_path)
        parser[section][key] = value
        with open(self.__config_file_path, 'w') as configfile:
            parser.write(configfile)

    def get(self, key):
        parser = ConfigParser()
        section = parser.default_section
        parser.read(self.__config_file_path)
        if key in parser[section]:
            return parser[section][key]
        if key in self.__default_config:
            return self.__default_config[key]
        return None

    def delete(self, key):
        parser = ConfigParser()
        section = parser.default_section
        parser.read(self.__config_file_path)
        parser.remove_option(section, key)
        with open(self.__config_file_path, 'w') as configfile:
            parser.write(configfile)

    def list(self):
        config_dict = self.__default_config
        parser = ConfigParser()
        section = parser.default_section
        parser.read(self.__config_file_path)
        for key, value in parser[section].items():
            config_dict[key] = value
        return config_dict


help_doc = '''
Manage base data of the task and step:
{a|add} <TASK>...                                    add tasks
{u|update} {<TASK_ID> <TASK>}...                     update tasks
{f|finish} <TASK_ID>...                              finish tasks
{d|delete} <TASK_ID>...                              delete tasks
{t|task} <TASK_ID> {a|add} <STEP>...                 add task steps
{t|task} <TASK_ID> {u|update} {<STEP_ID> <STEP>}...  update tasks steps
{t|task} <TASK_ID> {f|finish} <STEP_ID>...           finish tasks steps
{t|task} <TASK_ID> {d|delete} <STEP_ID>...           delete task steps

Extend functionality:
{h|help}                                             show this help info
{c|config} {s|set} <KEY> <VALUE>                     set a config
{c|config} {g|get} <KEY>                             get a config
{c|config} {d|delete} <KEY>                          delete a config
{c|config} {l|list}                                  list all config
{l|login} <USERNAME> <PASSWORD>                      login (if need sync)
{s|sync}                                             synchronize with server
{e|export}                                           export data to markdown
'''
