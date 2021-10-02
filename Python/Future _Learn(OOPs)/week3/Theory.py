
# Objectives
"""
-> Extend a class by adding your own functionality to existing code
-> Look at the concepts of inheritance and polymorphism
-> Use inheritance and polymorphism in the context of your text-based adventure game to create enemies for the player to encounter
"""

# Extending a class
"""
Extending a class takes advantage of a concept called inheritance; 
the new class can be said to inherit properties from its parent class. 
To extend a class, you can define new attributes or methods, and you can also change the behavior of existing methods.
"""

# Inheritence
"""
Inheritance is one of the key elements of OOP; 
it allows you to base a new class on an existing one. 
The new class automatically inherits all the methods and attributes of the existing class, 
removing the need to include the same methods and attributes in the new class.
"""




# Concepts
"""
When you create a subclass, that class will inherit all of the attributes and methods from the superclass. 
You used inheritance to extend a class written by somebody else, customising it and overriding its methods as necessary. 
Moreover, inheritance is also useful because it allows you to write code only once in a base class, and then extend that code with subclasses. 
It therefore helps you to avoid code duplication.

Polymorphism allows us to treat a subclass as if it were an object of the superclass, 
and yet still have the subclass behave differently. 
You saw this demonstrated where you wrote some code for a character object, and then successfully used the same code on an enemy object. 
This was possible because Enemy is a subclass of Character.

When an object contains another object, you can describe their relationship with ‘has a’, and you call this aggregation. 
For example, your room object now has a character inside it. 
In practice, the object might be of the Character class or the Enemy class: because of polymorphism, an enemy is a character, and therefore it doesn’t matter which type of object is used.

Next week, you will investigate class variables and finish writing the game. 
You will also look at ways of sharing your code and making it easy for other people to use.


"""




# key words
"""
Aggregation: when an object contains an instance of (or ‘has a’) another object

Extend: a class that uses the functionality of an existing class, but also adds to or overwrites some of it

Inherit: a class that inherits from another class is able to use all of the attributes and methods from that class

Polymorphism: if a class inherits from another class, it can also be considered to be (‘is a’) object of that class, but can behave differently

Subclass: inherits the properties of another class and adds some specialised methods of its own

Superclass: provides methods and attributes that are used by another class


"""