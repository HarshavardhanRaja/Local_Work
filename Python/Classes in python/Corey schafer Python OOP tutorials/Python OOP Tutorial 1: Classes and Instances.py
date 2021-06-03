"""
                                Basics of creating and instanciating simple classes
Why should we even use classes?
=> Classes are being used in most modern programming languages
=> They allow us to logically froup our data & Functions in a way that is easy to reuse and to build upon if need being
            data ===> attributes
            Functions ==> Methods (A function theat is assosiated with a class)
"""


#Class ==> Basically a blue print for creating instances
#Instances ==> objects made using class, Instance variables contains data that is unique to each instance


#creating class defination i.e, blue print to creat instances
class Employee:

    """
    If we create methods within a class they receive instance as the first argument automatically.
    By convention we call it as 'self' but we can call it whatever we want.
    After the first argument we can specify what other arguments we wan to take.
    """
    def __init__(self, first, last, pay):
        #Special initialize method also called as constructor in other languages
        #used to create instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +  "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


#creating instance from the class and reading their values
emp1 = Employee("Harsha", "Vardhan", "50000")
emp2 = Employee("test", "user", "60000")

print(emp1)             #<__main__.Employee object at 0x104929fd0>
print(emp1.first)       #Harsha
print(emp2.last)        #user
print(emp1.email)       #Harsha.Vardhan@company.com
print(emp1.fullname())  #Harsha Vardhan
print(Employee.fullname(emp2))  #test user


# the __dict__ method is a very useful method in Python to display all attributes of an instance of a class or other data type such as a class itself.
print(emp1.__dict__)        #{'first': 'Harsha', 'last': 'Vardhan', 'pay': '50000', 'email': 'Harsha.Vardhan@company.com'}
print(Employee.__dict__)    #{'__module__': '__main__', '__doc__': "\n    If we create methods within a class they receive instance as the first argument automatically.\n    By convention we call it as 'self' but we can call it whatever we want.\n    After the first argument we can specify what other arguments we wan to take.\n    ", '__init__': <function Employee.__init__ at 0x100c2f310>, 'fullname': <function Employee.fullname at 0x100c2f280>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>}
