from base.config import GlobalConfig
from base.po.task import Task
from base.po.task_step import TaskStep
import sqlite3


SQL_CREATE_TASK = "CREATE TABLE `TASK` (\
  `TASK_ID` varchar(32) NOT NULL,\
  `STATUS` varchar(10) NOT NULL DEFAULT 0,\
  `CONTENT` varchar(512) NOT NULL,\
  `CREATE_TIME` datetime NOT NULL,\
  `DEADLINE_TIME` datetime DEFAULT NULL,\
  PRIMARY KEY(TASK_ID)\
)"
SQL_CREATE_TASK_STEP = "CREATE TABLE `TASK_STEP` (\
  `TASK_STEP_ID` varchar(32) NOT NULL,\
  `TASK_ID` varchar(32) NOT NULL,\
  `STATUS` varchar(10) NOT NULL DEFAULT 0,\
  `CONTENT` varchar(512) NOT NULL,\
  PRIMARY KEY(TASK_STEP_ID),\
  FOREIGN KEY(TASK_ID) REFERENCES `TASK`(TASK_ID)\
)"
SQL_SELECT_TABLE_TASK_COUNT = "SELECT COUNT(*) FROM `sqlite_master` WHERE type='table' AND name='TASK'"
SQL_SELECT_TABLE_TASK_STEP_COUNT = "SELECT COUNT(*) FROM `sqlite_master` WHERE type='table' AND name='TASK_STEP'"
SQL_SELECT_TASK_ALL = 'SELECT * FROM `TASK`'
SQL_SELECT_TASK_STEP_ALL = "SELECT * FROM `TASK_STEP`"
SQL_SELECT_TASK_STEP_BY_TASK_ID = "SELECT * FROM `TASK_STEP` WHERE TASK_ID = ?"

SQL_INSERT_TASK = "INSERT INTO `TASK` (TASK_ID, CONTENT, CREATE_TIME) VALUES (?, ?, ?)"
SQL_INSERT_TASK_STEP = "INSERT INTO 'TASK_STEP' (TASK_STEP_ID, TASK_ID, CONTENT) VALUES (?, ?, ?)"


def trans_to_task(task_tuple):
    task = Task()
    task.task_id = task_tuple[0]
    task.status = task_tuple[1]
    task.content = task_tuple[2]
    task.create_time = task_tuple[3]
    task.deadline_time = task_tuple[4]
    return task


def trans_to_task_step(task_step_tuple):
    task_step = TaskStep()
    task_step.task_step_id = task_step_tuple[0]
    task_step.task_id = task_step_tuple[1]
    task_step.status = task_step_tuple[2]
    task_step.content = task_step_tuple[3]
    return task_step


def trans_to_task_list(task_tuple_list):
    return list(map(trans_to_task, task_tuple_list))


def trans_to_task_step_list(task_step_tuple_list):
    return list(map(trans_to_task_step, task_step_tuple_list))


class Dao:
    def __init__(self):
        self.__data_file = GlobalConfig().get_data_file_path()
        self.__connect = sqlite3.connect(self.__data_file)
        self.__cursor = self.__connect.cursor()
        self.__init_table()

    def __close(self):
        self.__cursor.close()
        self.__connect.close()

    def __init_table(self):
        if not self.__is_table_task_exist():
            self.__cursor.execute(SQL_CREATE_TASK)
        if not self.__is_table_task_step_exist():
            self.__cursor.execute(SQL_CREATE_TASK_STEP)

    def __is_table_task_exist(self):
        table_task_count = self.__cursor.execute(SQL_SELECT_TABLE_TASK_COUNT).fetchall()[0][0]
        return table_task_count == 1

    def __is_table_task_step_exist(self):
        table_task_step_count = self.__cursor.execute(SQL_SELECT_TABLE_TASK_STEP_COUNT).fetchall()[0][0]
        return table_task_step_count == 1

    def find_all_task(self):
        task_tuple_list = self.__cursor.execute(SQL_SELECT_TASK_ALL).fetchall()
        return trans_to_task_list(task_tuple_list)

    def insert_task(self, task):
        self.__cursor.execute(SQL_INSERT_TASK, (task.task_id, task.content, task.create_time))
        self.__connect.commit()

    def find_all_task_step(self):
        task_step_tuple_list = self.__cursor.execute(SQL_SELECT_TASK_STEP_ALL).fetchall()
        return trans_to_task_step_list(task_step_tuple_list)

    def find_all_task_step_by_task_id(self, task_id):
        task_step_tuple_list = self.__cursor.execute(SQL_SELECT_TASK_STEP_BY_TASK_ID, (task_id,)).fetchall()
        return trans_to_task_step_list(task_step_tuple_list)

    def insert_task_step(self, task_step):
        self.__cursor.execute(SQL_INSERT_TASK_STEP, (task_step.task_step_id, task_step.task_id, task_step.content))
        self.__connect.commit()

