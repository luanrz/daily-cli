from base.config import GlobalConfig
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

SQL_INSERT_TASK = "INSERT INTO `TASK` (TASK_ID, CONTENT, CREATE_TIME) VALUES (?, ?, ?)"


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
        data = self.__cursor.execute(SQL_SELECT_TASK_ALL).fetchall()
        self.__close()
        return data

    def insert_task(self, task):
        self.__cursor.execute(SQL_INSERT_TASK, (task.task_id, task.content, task.create_time))
        self.__connect.commit()

