# ORM and Unix Introduction - Day 2

### Learning Objectives
***Students Will Be Able To***

* Wrap SQL queries inside Python objects to make an ORM

---
### Context

* When working with back end technologies many frameworks come with a short hand so there's no need to write out SQL code from scratch.

---
### Lesson

##### Part 1 - Syntax to create a Model with kwargs
* Let's say we want to pass a variable number of inputs to our class's `__init__` function. Here's some syntax to do that:
```
class Model:
    def __init__(self, **kwargs):
        for i in kwargs.keys():
            setattr(self, i, kwargs[i])
```
* Now, later on, we want to make a User model that inherits from the Model class. Something like this:
```
class Users(Model):
    pass
```
* We've used `pass` here so that our `Users` class will just inherit from the `Model` class.
* Now I can use my `Users` class to make a new object:
```
user = Users(name='Timmy', id=45, house='tree')
```
* The Model class' `__init__` method lets me pass any amount of keyword arguments.
* Now, I can use this syntax to create objects of the `Users` class.

##### Part 2 - sys.argv:
* We can pass Python programs command line arguments when we execute those programs in a terminal. An example here will make things much more clear:
```python
#argecho.py
import sys

for arg in sys.argv:
    print arg
```
* In the example above, I've created a Python file called argecho.py, I've import `sys`.
* My `for-loop` has some new syntax. Another set of examples will show how this syntax works:
```
[you@localhost py]$ python argecho.py
argecho.py
```
```
[you@localhost py]$ python argecho.py abc def
argecho.py
abc
def
```
```
[you@localhost py]$ python argecho.py --help
argecho.py
--help
```
```
[you@localhost py]$ python argecho.py -m kant.xml
argecho.py
-m
kant.xml
```
* What this example is meant to demonstrate is that sys.argv allows us to access the `command-line arguments` that a user passes to our program.
* `sys.argv` will contain a list of all the words that are typed after the name of the program.
##### Part 3 - Introduction to today's challenges:
* All of the instructions you'll need are included within the respective README file for each exercise.
* We recommend that that you do the exercises in the following chronological order:

    * baby-orm-save
    * todos-baby-orm
    * unix-ninja-two

* Notice that there is a directory today called `orm_example_solutions`. LOOK AT THIS FILE WITH CAUTION! This shows you ONE way to solve the baby_orm challenge. Only use this is you want to see how someone has solved the baby_orm challenge. Remembering that copying/pasting someone else's code teaches you nothing.
