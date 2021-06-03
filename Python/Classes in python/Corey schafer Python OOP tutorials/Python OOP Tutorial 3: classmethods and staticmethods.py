"""
Regular methods ==> automatically takes instance as the first argument ('self')
Class methods ==> automatically takes class as the first argument ('self')
Static methods ==> don't pass anything automatically
               ==> They behave just like regular functions except we include them in classes because they have some logical connection with the class
               ==> If you don't access the instance or class anywhere within the function then it is static function.

"""
# Decorators are used to create classmethods, static methods before the function.
# @classmethod => decorator for classmethod.
# @staticmethod => decorator for static method.

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
    
    @classmethod
    def set_raise_amount(cls, amount):
         cls.raise_amount = amount

    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6 :
            return False
        return True



emp1 = Employee("Harsha", "Vardhan", 50000)
emp2 = Employee("test", "user", 60000)

print(Employee.raise_amount)
Employee.set_raise_amount(1.06)
print(Employee.raise_amount)

emp3  = Employee.from_str("lala-babaa-34590")
print(emp3.__dict__)
import datetime
mydate = datetime.date(2021, 11, 5)
print(Employee.is_workday(mydate))
