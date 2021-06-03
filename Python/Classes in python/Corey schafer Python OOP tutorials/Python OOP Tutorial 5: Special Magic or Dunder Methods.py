"""
Special methods also called as Magic methods,
    => These special methods emulates some built in behaviour within python
    => By defining our own special methods, we will be able to change the built in behaviour or operations
"""

# 3 Important special methods are, 
# __init__ (called as dunder init)
# __repr__(dunder reper) => is meant to be an unambigious representation of object & should be used for debugging, logging etc
    # => It's really meant to be seen by other developers.
# __str__ (dunder str) => is meant to be more of a readable representation of an object and is meant to be used as a display to the end user


class Employee:
    
    num_of_employes = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +  "." + last + "@company.com"
        Employee.num_of_employes +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp1 = Employee("Harsha", "Vardhan", 50000)
emp2 = Employee("test", "user", 60000)

print(emp1)
print(emp2)
print(repr(emp1))
print(emp2.__repr__())
print(str(emp1))
print(emp2.__str__())

print(emp1 + emp2)
print(len(emp1))

