"""
Class Variables:
    => Variables that are shared amoung all the instances of a class.
    => Whereas instance variables are unique for each instance.

When we try to access an attribute from an instance,
it will first checks if the instance contains that attribute and if it doesn't. 
it will see if class or any class that it inherits from contains that attribute.
"""
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

print(Employee.num_of_employes)
emp1 = Employee("Harsha", "Vardhan", 50000)
emp2 = Employee("test", "user", 60000)
print(Employee.num_of_employes)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

print(emp1.raise_amount)
print(Employee.raise_amount)

Employee.raise_amount = 1.05
emp1.raise_amount = 1.06

emp1.apply_raise()
emp2.apply_raise()
print(emp1.pay, emp1.raise_amount)
print(emp2.pay, emp2.raise_amount)
print(Employee.raise_amount)
