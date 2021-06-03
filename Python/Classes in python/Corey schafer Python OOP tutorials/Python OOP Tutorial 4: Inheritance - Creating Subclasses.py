"""
Inheritance:
    => it allows us to inherit attributes and methods from a parent class.
    => these are useful because we can create subclass and get alll the functionalities of the parent class and then 
    we can override or add completely new functionalities without affecting the parent class in anyway.
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


class Developer(Employee):
    raise_amount = 1.08

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # used to initalize values inherited from parent class
        #Employee.__init__(self, first, last, pay) this can also be used
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay) # used to initalize values inherited from parent class
        #Employee.__init__(self, first, last, pay) this can also be used
        if employees is None: self.employees = []
        else: self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def del_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("==>", emp.fullname())



emp1 = Employee("Harsha", "Vardhan", 50000)
emp2 = Employee("test", "user", 60000)
dev1 = Developer("Blake", "navy_blue", 30000,  "thunder" )
dev2 = Developer("tori", "blue", 450000, "water")
dev3 = Developer("Dustin", "yellow", 22000, "Earth")
man1 = Manager("shane", "red", 90000, [dev2])
man2 = Manager("Hunter", "maroon", 85000, [dev1])

dev2.apply_raise()
print(dev2.pay)

man1.print_emps()
man1.add_employee(dev3)
man1.del_employee(dev2)
man1.print_emps()