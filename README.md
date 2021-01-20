## How to use

### Manage task data

| operation   | command                                        | example                       |
| ----------- | ---------------------------------------------- | ----------------------------- |
| add task    | `{ a , add } <TASK_CONTENT>...`                | `a 'do housework' 'exercise'` |
| update task | `{ u , update } {<TASK_ID> <TASK_CONTENT>}...` | `u 1 'do homework' `          |
| finish task | `{ f , finish } <TASK_ID>...`                  | `f 1 2`                       |
| delete task | `{ d , delete } <TASK_ID>...`                  | `d 1 2`                       |

### Manage task step data

| operation        | command                                                      | example                         |
| ---------------- | ------------------------------------------------------------ | ------------------------------- |
| add task step    | `{ t , task } <TASK_ID> { a , add } <STEP_CONTENT>...`       | `t 1 a 'do math homework'`      |
| update task step | `{ t , task } <TASK_ID> { u , update } {<STEP_ID> <STEP_CONTENT>}...` | `t 1 u 1 'do physics homework'` |
| finish task step | `{ t , task } <TASK_ID> { f , finish } <STEP_ID>...`         | `t 1 f 1`                       |
| delete task step | `{ t , task } <TASK_ID> { d , delete } <STEP_ID>...`         | `t 1 d 1`                       |

### Extend functionality

| operation | command          | example  |
| --------- | ---------------- | -------- |
| sync      | `{ s , sync }`   | `sync`   |
| export    | `{ e , export }` | `export` |
| help      | `{ h , help }`   | `help`   |
