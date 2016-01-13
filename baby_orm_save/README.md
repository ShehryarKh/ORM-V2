# ORM Extended (Save)

* Today well be extending our Baby ORM to include save functionality. 

##### Objective 1 

* Pseudocode everything!
* Do not write any real code. Read this entire markdown and pseudo code what you intend on doing to complete the prompts

##### Objective 2

* You want to be able to take any number or arguments from whatever table is supplied, and either create the row, if it doesn't exist, or update the row, if it does exist. The save method should not take parameters, and is an instance method.

```
user = Users(name="Cassie") # new instance
user.save() # creates new row in table, stores id, returns True on success

cassie = Users.get(name="Cassie") # existing row instance
cassie.hair = "purple"
cassie.save() # updates row, returns True
```

#### The Create Method

* The create function is a class method, that creates a new row and returns the instance.

```
user = Users.create(name="Greg") # returns newly created instance of User class
```
* Think about the simplest way you can accomplish this.


***HINT***

* We studied some of these in class but familiarize yourself with the following

```
setattr()
hasattr()
__name__
type(self)
__dict__
**kwargs
```
