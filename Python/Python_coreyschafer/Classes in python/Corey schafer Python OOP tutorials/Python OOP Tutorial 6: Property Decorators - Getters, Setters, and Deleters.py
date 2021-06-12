"""
Property decorators (getter, setter, deleter)
    => this allows us to give class attributes getter, setter, deleter functionalities
"""

class Employee:
 
    def __init__(self, first, last):

        self.first = first
        self.last = last
        #self.email = first +  "." + last + "@company.com"

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("!!!!!!!!!Deleting the full name")    
        self.first = None
        self.last = None

emp1 = Employee('Harsha', 'Vardhan')

print(emp1.first)       
print(emp1.last)           
print(emp1.fullname)  

# we defined email in the class like a method, but we are able to access it like an attribute
print(emp1.email)       

emp1.fullname = 'chandler bing'
print(emp1.fullname)

del emp1.fullname  
print(emp1.fullname)
