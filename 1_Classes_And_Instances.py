#https://www.youtube.com/watch?v=ZDa-Z5JzLYM

class ClassEmpty:
    # You can use pass to stop python throwing errors for empty classes
    pass
    
class Employee:
    #Constructor for Employee class
    def __init__(self, firstname,lastname, age):
        #Define attributes for class
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = firstname + '.' + lastname + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

#Don't need to pass the instance "self" as an arg as it's done automatically
emp_1 = Employee('Jordan', 'McDougall', 25)

emp_2 = Employee('Employee', 'Two', 26)

print('Printing Employee Email using class attribute')
print(emp_1.email)
print(emp_2.email)

print('\nPrinting Employee full name using class method')
print(emp_1.fullname())
print(emp_2.fullname())

### 
# Notes
# * Every method in a class automatically takes the instance as the 1st arguement (i.e.self)
# * When invoking attributes you don't need parenthesis, for methods you do.
###