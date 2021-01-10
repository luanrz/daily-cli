from base.config import GlobalConfig
from base.po.task import Task
from base.po.task_step import TaskStep
import sqlite3


class DaoBase:
    def __init__(self):
        data_file = GlobalConfig().get_data_file_path()
        self.connect = sqlite3.connect(data_file)
        self.cursor = self.connect.cursor()
        self._init_table()

    def close(self):
        self.cursor.close()
        self.connect.close()

    def _init_table(self):
        pass


class TaskDao(DaoBase):
    __SQL_CREATE_TASK = "CREATE TABLE `TASK` (\
      `TASK_ID` varchar(32) NOT NULL,\
      `STATUS` varchar(10) NOT NULL DEFAULT 0,\
      `CONTENT` varchar(512) NOT NULL,\
      `CREATE_TIME` datetime NOT NULL,\
      `DEADLINE_TIME` datetime DEFAULT NULL,\
      PRIMARY KEY(TASK_ID)\
    )"
    __SQL_SELECT_TABLE_TASK_COUNT = "SELECT COUNT(*) FROM `sqlite_master` WHERE type='table' AND name='TASK'"
    __SQL_SELECT_TASK_ALL = "SELECT * FROM `TASK`"
    __SQL_SELECT_TASK_BY_TASK_ID = "SELECT * FROM `TASK` WHERE TASK_ID = ?"
    __SQL_INSERT_TASK = "INSERT INTO `TASK` (TASK_ID, CONTENT, CREATE_TIME) VALUES (?, ?, ?)"
    __SQL_DELETE_TASK = "DELETE FROM TASK WHERE TASK_ID = ?"
    __SQL_UPDATE_TASK_CONTENT = "UPDATE TASK SET CONTENT = ? WHERE TASK_ID = ?"
    __SQL_UPDATE_TASK_STATUS = "UPDATE TASK SET STATUS = ? WHERE TASK_ID = ?"

    def _init_table(self):
        if not self.__is_table_task_exist():
            self.cursor.execute(self.__SQL_CREATE_TASK)

    def __is_table_task_exist(self):
        table_task_count = self.cursor.execute(self.__SQL_SELECT_TABLE_TASK_COUNT).fetchall()[0][0]
        return table_task_count == 1

    def find_all_task(self):
        task_tuple_list = self.cursor.execute(self.__SQL_SELECT_TASK_ALL).fetchall()
        return self.__trans_to_task_list(task_tuple_list)

    def find_task_by_task_id(self, task_id):
        task_tuple = self.cursor.execute(self.__SQL_SELECT_TASK_BY_TASK_ID, (task_id,)).fetchone()
        return self.__trans_to_task(task_tuple)

    def insert_task(self, task):
        self.cursor.execute(self.__SQL_INSERT_TASK, (task.task_id, task.content, task.create_time))
        self.connect.commit()

    def delete_task(self, task_id):
        self.cursor.execute(self.__SQL_DELETE_TASK, (task_id,))
        self.connect.commit()

    def update_task_content(self, task):
        self.cursor.execute(self.__SQL_UPDATE_TASK_CONTENT, (task.content, task.task_id))
        self.connect.commit()

    def update_task_status(self, task):
        self.cursor.execute(self.__SQL_UPDATE_TASK_STATUS, (task.status, task.task_id))
        self.connect.commit()

    @staticmethod
    def __trans_to_task_list(task_tuple_list):
        return list(map(TaskDao.__trans_to_task, task_tuple_list))

    @staticmethod
    def __trans_to_task(task_tuple):
        if task_tuple is None:
            return None

        task = Task()
        task.task_id = task_tuple[0]
        task.status = task_tuple[1]
        task.content = task_tuple[2]
        task.create_time = task_tuple[3]
        task.deadline_time = task_tuple[4]
        return task


class TaskStepDao(DaoBase):
    __SQL_CREATE_TASK_STEP = "CREATE TABLE `TASK_STEP` (\
      `TASK_STEP_ID` varchar(32) NOT NULL,\
      `TASK_ID` varchar(32) NOT NULL,\
      `STATUS` varchar(10) NOT NULL DEFAULT 0,\
      `CONTENT` varchar(512) NOT NULL,\
      PRIMARY KEY(TASK_STEP_ID),\
      FOREIGN KEY(TASK_ID) REFERENCES `TASK`(TASK_ID)\
    )"
    __SQL_SELECT_TABLE_TASK_STEP_COUNT = "SELECT COUNT(*) FROM `sqlite_master` WHERE type='table' AND name='TASK_STEP'"
    __SQL_SELECT_TASK_STEP_ALL = "SELECT * FROM `TASK_STEP`"
    __SQL_SELECT_TASK_STEP_BY_TASK_ID = "SELECT * FROM `TASK_STEP` WHERE TASK_ID = ?"
    __SQL_SELECT_TASK_STEP_BY_TASK_STEP_ID = "SELECT * FROM `TASK_STEP` WHERE TASK_STEP_ID = ?"
    __SQL_INSERT_TASK_STEP = "INSERT INTO 'TASK_STEP' (TASK_STEP_ID, TASK_ID, CONTENT) VALUES (?, ?, ?)"
    __SQL_DELETE_TASK_STEP = "DELETE FROM TASK_STEP WHERE TASK_STEP_ID = ?"
    __SQL_UPDATE_TASK_STEP_CONTENT = "UPDATE TASK_STEP SET CONTENT = ? WHERE TASK_STEP_ID = ?"
    __SQL_UPDATE_TASK_STEP_STATUS = "UPDATE TASK_STEP SET STATUS = ? WHERE TASK_STEP_ID = ?"

    def _init_table(self):
        if not self.__is_table_task_step_exist():
            self.cursor.execute(self.__SQL_CREATE_TASK_STEP)

    def __is_table_task_step_exist(self):
        table_task_step_count = self.cursor.execute(self.__SQL_SELECT_TABLE_TASK_STEP_COUNT).fetchall()[0][0]
        return table_task_step_count == 1

    def find_all_task_step(self):
        task_step_tuple_list = self.cursor.execute(self.__SQL_SELECT_TASK_STEP_ALL).fetchall()
        return self.__trans_to_task_step_list(task_step_tuple_list)

    def find_all_task_step_by_task_id(self, task_id):
        task_step_tuple_list = self.cursor.execute(self.__SQL_SELECT_TASK_STEP_BY_TASK_ID, (task_id,)).fetchall()
        return self.__trans_to_task_step_list(task_step_tuple_list)

    def find_task_step_by_task_step_id(self, task_step_id):
        task_step_tuple = self.cursor.execute(self.__SQL_SELECT_TASK_STEP_BY_TASK_STEP_ID, (task_step_id,)).fetchone()
        return self.__trans_to_task_step(task_step_tuple)

    def insert_task_step(self, task_step):
        self.cursor.execute(self.__SQL_INSERT_TASK_STEP, (task_step.task_step_id, task_step.task_id, task_step.content))
        self.connect.commit()

    def delete_task_step(self, task_step):
        self.cursor.execute(self.__SQL_DELETE_TASK_STEP, (task_step.task_step_id,))
        self.connect.commit()

    def update_task_step_content(self, task_step):
        self.cursor.execute(self.__SQL_UPDATE_TASK_STEP_CONTENT, (task_step.content, task_step.task_step_id))
        self.connect.commit()

    def update_task_step_status(self, task_step):
        self.cursor.execute(self.__SQL_UPDATE_TASK_STEP_STATUS, (task_step.status, task_step.task_step_id))
        self.connect.commit()

    @staticmethod
    def __trans_to_task_step_list(task_step_tuple_list):
        return list(map(TaskStepDao.__trans_to_task_step, task_step_tuple_list))

    @staticmethod
    def __trans_to_task_step(task_step_tuple):
        if task_step_tuple is None:
            return None

        task_step = TaskStep()
        task_step.task_step_id = task_step_tuple[0]
        task_step.task_id = task_step_tuple[1]
        task_step.status = task_step_tuple[2]
        task_step.content = task_step_tuple[3]
        return task_step
