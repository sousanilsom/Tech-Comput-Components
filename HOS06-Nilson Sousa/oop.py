# # name of the class normally use CapWords convention
class Employee:
    emp_count = 0                # class variable

    def __init__(self, first, last, pay):
        self.first = first        # instance variable
        self.last  = last         # instance variable
        self.pay   = pay          # instance variable
        self.email = first + '.' + last + '@company.com'
        Employee.emp_count += 1   # <- focus here

    def showinfo(self):
        return '{} {}, {}'.format(self.first, self.last, self.email)


emp1 = Employee('Elliot', 'Alderson', 7000)
emp2 = Employee('Jean',   'Grey',     8000)

print(emp1.showinfo())
print("Total Employees:", Employee.emp_count)
