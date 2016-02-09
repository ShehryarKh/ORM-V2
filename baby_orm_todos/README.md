# Final ORM Test

* We will now test your ORM.
* Create a terminal application that creates a todo list using ARGV and saves the lists using your baby ORM

For example:

```
python3 todolist.py add do laundry
python3 todolist.py add buy groceries
python3 todolist.py list
python3 todolist.py complete <task id>
python3 todolist.py delete <task id>
```

##### Your ORM

* The ORM you built should be universal and allow you to search through any class/table name

##### Design and create your database

* You will make a createdb.py file
* Design your schema.
* Create your database and seed it with some dummy data

##### Todo.py

* You will make another file with a Todo model inside of it
* This will talk to the orm_class
* We will need methods for `add`, `complete`, `delete`, and `list`
* These aren't just for the user - these are actual backend functionality in your code. Create a skeleton of methods for any db classes you might need.
* add() should append an item to the list.
* list() should display the list of tasks and their id. If it is completed, it should be noted as such.

```
python3 todolist.py list
$ My Todo List
$ 1. do laundry
$ 2. buy groceries
```
* delete() should take the id of the task and remove it from the database.
* complete() should take the id of the task and mark it complete.
