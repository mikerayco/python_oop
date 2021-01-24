
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'



emp1 = Employee('steve', 'jobs', 50000)
emp2 = Employee('eric', 'barone', 60000)


emp1.greet = 'hello' #you can still add an adhoc variable
print(emp1.__dict__)

print(emp2.fullname())

# run a function from a class

fullname = Employee.fullname(emp1)
print(fullname)
