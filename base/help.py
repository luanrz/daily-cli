usage = '''
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
