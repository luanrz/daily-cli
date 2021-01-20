usage='''
Manage task data:
{ a | add } <TASK_CONTENT>...                                          add tasks
{ u | update } {<TASK_ID> <TASK_CONTENT>}...                           update tasks
{ f | finish } <TASK_ID>...                                            finish tasks
{ d | delete } <TASK_ID>...                                            delete tasks

Manage task step data:
{ t | task } <TASK_ID> { a | add } <STEP_CONTENT>...                   add task steps
{ t | task } <TASK_ID> { u | update } {<STEP_ID> <STEP_CONTENT>}...    update tasks steps
{ t | task } <TASK_ID> { f | finish } <STEP_ID>...                     finish tasks steps
{ t | task } <TASK_ID> { d | delete } <STEP_ID>...                     delete task steps

Extend functionality:
{ s | sync }                                                           synchronize with the server
{ e | export }                                                         export data to markdown
{ h | help }                                                           show this help info
'''
