import os


class DefaultConstant:
    DEFAULT_WORK_DIR = os.path.join(os.path.expanduser('~'), '.daily')
    DEFAULT_DATA_FILE = os.path.join(DEFAULT_WORK_DIR, 'daily.db')
    DEFAULT_CONFIG_FILE = os.path.join(DEFAULT_WORK_DIR, 'daily.conf')


class GlobalConfig:
    def __init__(self):
        self.__data_file_path = DefaultConstant.DEFAULT_DATA_FILE
        self.__data_config_path = DefaultConstant.DEFAULT_CONFIG_FILE

    def get_data_file_path(self):
        return self.__data_file_path

    def get_config_file_path(self):
        return self.__data_config_path


