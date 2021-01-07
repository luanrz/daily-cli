import curses


class View:
    def __init__(self):
        self.__data = []

    def load(self, data):
        self.__data = data
        return self

    def show(self):
        TaskWidget().load(self.__data).render()

    def success(self):
        print(self.__data)

    def error(self):
        print(self.__data)


class TaskWidget:
    def __init__(self):
        self.__tasks = []
        self.__begin_x_id = 0
        self.__begin_x_content = 0
        self.__begin_x_status = 0
        self.__begin_y = 0
        self.__stdscr = curses.initscr()

    def load(self, tasks):
        self.__tasks = tasks

        length_id_interval = 2
        length_content_interval = 2
        length_id = 1 + length_id_interval
        length_content = get_content_max_length(tasks) + length_content_interval
        length_status = 5

        task_size = get_task_size(tasks)
        task_interval_length = task_size - 1
        task_step_size = get_task_step_size(tasks)

        max_x = curses.COLS
        max_y = curses.LINES

        self.__begin_x_id = (max_x - length_id - length_content - length_status) // 2
        self.__begin_x_content = self.__begin_x_id + length_id
        self.__begin_x_status = self.__begin_x_content + length_content
        self.__begin_y = (max_y - task_size - task_interval_length - task_step_size) // 2

        return self

    def render(self):
        curses.curs_set(False)
        curses.noecho()
        curses.cbreak()
        self.__stdscr.keypad(True)

        y = self.__begin_y
        task_id_index = 1
        for task in self.__tasks:
            self.__stdscr.addstr(y, self.__begin_x_id, str(task_id_index), curses.A_BOLD)
            self.__stdscr.addstr(y, self.__begin_x_content, task.content, curses.A_BOLD)
            self.__stdscr.addstr(y, self.__begin_x_status, get_status_ico(task.status), curses.A_BOLD)
            y = y + 1
            task_step_id_index = 1
            for task_step in task.task_steps:
                self.__stdscr.addstr(y, self.__begin_x_id + task_step_padding, str(task_step_id_index), curses.A_DIM)
                self.__stdscr.addstr(y, self.__begin_x_content + task_step_padding, task_step.content, curses.A_DIM)
                self.__stdscr.addstr(y, self.__begin_x_status, get_status_ico(task_step.status), curses.A_DIM)
                y = y + 1
                task_step_id_index = task_step_id_index + 1
            task_id_index = task_id_index + 1
            y = y + 1

        self.__stdscr.getch()

        self.__stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()


def get_content_max_length(tasks):
    max_content_length = 0
    for task in tasks:
        current_content_length = len(task.content.encode('gbk'))
        if current_content_length > max_content_length:
            max_content_length = current_content_length
        for task_step in task.task_steps:
            current_content_length = len(task_step.content.encode('gbk')) + task_step_padding
            if current_content_length > max_content_length:
                max_content_length = current_content_length
    return max_content_length


def get_task_size(tasks):
    return tasks.__len__()


def get_task_step_size(tasks):
    task_step_size = 0
    for task in tasks:
        task_step_size = task_step_size + task.task_steps.__len__()
    return task_step_size


def get_status_ico(status):
    if status == '1':
        return '[ X ]'
    if status == '0':
        return '[   ]'
    return ''


task_step_padding = 4
