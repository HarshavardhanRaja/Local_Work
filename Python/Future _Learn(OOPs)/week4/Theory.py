

"""
There are different types of attributes: public, protected, and private attributes.
During this course, you have created public attributes that are available outside the class.
Most programming languages support the following attribute access levels:

Public: can be changed outside the class
Protected: can only be changed by the class or a subclass
Private: can only be changed by the class


Attributes within Python are always public, 
but there is a convention of using either no, single, or double underscores before an attribute name to denote its access level.


class MyClass():

    def __init__(self):
        # no underscore = public
        self.my_attribute = None

        # single underscore = protected
        self._my_attribute = None

        # double underscore = private
        self.__my_attribute = None
"""


# Class and instance variables
"""
The attributes in a class are just variables used to store data within an object of that class. 
Each time you create an object, that object has its own set of these variables.


A class variable is like having a shared notebook, with its contents available to all notebook owners, 
i.e. all objects of that class.


You can create a class variable in Python by adding it outside of the constructor.

class MyClass():

    # class variable outside the constructor
    my_class_variable = 0

    def __init__(self):
        # instance variable inside the constructor
        self.my_instance_variable = None


To use a class variable you use the name of the class, as opposed to the name of an object, for example:
Room.number_of_rooms = 1

"""


# Different types of methods
"""
During this course you have been using methods to interact with instances (objects) of classes. 
These methods are known as instance methods. 

There are two other types of method available in Python: static and class. 
In this step you will explore the different types of method and how they can be used.

    Instance methods
    Static methods
    Class methods


Static and class methods are different to instance methods in that you don’t have to create an object of the class before you can use them. 
Static and class methods belongs to a class, whereas an instance methods belongs to the object.
Static and class method are useful if you want to create a function that is the same for all objects within a class.




Review the code below, which includes a static method and a class method in addition to an instance method.



class MyClass():

    def instance_method(self):
        print(self)

    @staticmethod
    def static_method():
        print("nothing")

    @classmethod
    def class_method(cls):
        print(cls)

my_object = MyClass()
my_object.instance_method()
MyClass.static_method()
MyClass.class_method()




An instance method is passed self, a static method is passed nothing, and a class method is passed cls, which is the class the method belongs to.
To define a method as static or class, you use either the @staticmethod or @classmethod decorator.
You call a static or class method via the class (MyClass.staticmethod()), not its object.
"""


# Properties
"""
A property is a special type of function that allows you to get and set attributes without the use of getter and setter methods.

As you have previously learnt, 
it is good practice to set attributes through the use of getter and setter methods, as demonstrated in this class:

class MyClass():
    def __init__(self):
        self.my_attribute = 0

    def get_my_attribute(self):
        return self.my_attribute

    def set_my_attribute(self, value):
        self.my_attribute = value    

my_object = MyClass()

my_object.set_my_attribute(1)
print(my_object.get_my_attribute())



As the attributes are public, it is possible in Python to access them directly using my_object.my_attribute, for example:

my_object = MyClass()

my_object.my_attribute = 2
print(my_object.my_attribute)

This approach would simplify the code, 
but with the downside that without wrapping the get and set into functions, 
you cannot control how attributes in your class are updated. 
There would be nothing stopping someone setting the attribute to an invalid value, for example:

my_object.my_attribute = "some invalid value"




Properties get around this problem by allowing you to define a function that is called when the value of an attribute is changed directly.
A property is a special type of attribute that is defined using the @property decorator.

class MyClass():
    def __init__(self):
        self._my_attribute = 0

    @property
    def my_attribute(self):
        return self._my_attribute

    @my_attribute.setter
    def my_attribute(self, value):
        self._my_attribute = value

my_object = MyClass()


I have used an underscore _ to denote that the my_attribute attribute is protected. By doing so I am stating that this attribute should not be changed directly.

There are two new methods, both called my_attribute.

The my_attribute method that has the @property decorator before it is the getter and, when called, it will return the value stored in _my_attribute.

The second my_attribute method that has the @my_attribute.setter decorator is the setter. It accepts a single parameter which, when called, will set _my_attribute to the value passed.




"""





# Recap
"""
My biggest criticism of object-oriented programming (OOP) is the language used to describe the principles, as the terms are difficult to remember and understand.

In this step you will review the terms and join a conversation about the concept you found most difficult to understand, so that you can provide an alternative description.

You have learnt the following terms during this course:

Object: the data and functions required to model something in code
Class: a blueprint for making an object
Instance: a specific example of an object
Attribute: a named piece of data stored within an object
Method: a function which performs a task on an object i.e. tells the object what to do
Inheritance: a class is able to use all of the attributes and methods from a superclass
Polymorphism: when a method behaves differently depending on which object it belongs too
Aggregation: when an object contains an instance of another object
I have provided some brief descriptions for each. I am sure you can do better, though.

Pick a term from the list above and comment on how you would describe it to someone else.

"""




# challenge 1
"""
Add the Item class you wrote in week two to your game. 
Follow the same process as for the Character class: 
add an attribute to Room so that it can store an Item, 
and then create the Item and assign it to the Room. 
Inside the game loop, check whether there is an Item in the room, and if so, describe it.
"""

"""
Example solution
I added an item attribute to the Room class in room.py.

class Room():
    def __init__(self, room_name):
        ...
        self.item = None

def get_item(self):
    return self.item
    
def set_item(self, item_name):
    self.item = item_name
I added a describe() method to the Item class so that I could display what the item was.

def describe(self):
    print("The [" + self.name + "] is here - " + self.description)
I created some items and added them to rooms when setting up the game.

cheese = Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = Item("book")
book.set_description("A really good book entitled 'Knitting for Everyone'")
dining_hall.set_item(book)
In the main game loop, I got the item from the room and used the describe method to display it:

while dead == False:
    ...

    item = current_room.get_item()
    if item is not None:
        item.describe()
"""



# Challenge 2
"""
Add a backpack to allow the player to store items. This could be a list in the main part of the program, or a separate class:

backpack = []
When a player enters a room that contains an Item, 
the command ‘take’ should put the name of the current room’s Item into the backpack, 
and also set the Item attribute of the Room to None.

"""

"""
I created a list to hold the items in my backpack.

backpack = []
I added a new command, take, to the game, which would remove the item from the room and add it to my backpack list.

elif command == "take":
    if item is not None:
      print("You put the " + item.get_name() + " in your backpack")
      backpack.append(item.get_name())
      current_room.set_item(None)
"""



# Challenge 3
"""
Change your game so that when the player chooses an item to use in a fight,
 the game checks whether the player actually has an item with that name in their backpack.
"""

"""
I added an if statement to check that I had the item in the backpack list before using it to fight with:

    elif command == "fight":
        ...    
            # Do I have this item?
            if fight_with in backpack:
                ...
            else:
                print("You don't have a " + fight_with)

"""


# Challenge 4
"""
If you want your game to last a bit longer, 
you can use a class variable to allow the player to win the game only after they have defeated a specific number of enemies, 
rather than winning it the instant they defeat a single enemy.
"""
"""
I added an enemies_to_defeat class variable to the Enemy class, and increment the value each time an Enemy object was created:

class Enemy(Character):
    enemies_to_defeat = 0

    def __init__(self, char_name, char_description):
        ...
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1
If an enemy was defeated, I reduced the value of enemies_to_defeat by 1:

class Enemy(Character):
    ...
    def fight(self, combat_item):
        if combat_item == self.weakness:
            ...
            Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1
            return True


In the main game loop, I checked to see if I had defeated all the enemies before ending the game:

    elif command == "fight":
        ...
            if inhabitant.fight(fight_with) == True:
                ...
                if Enemy.enemies_to_defeat == 0:
                    print("Congratulations, you have vanquished the enemy horde!")
                    dead = True
When dead is set to True, the while loop exits and the game finishes.


"""