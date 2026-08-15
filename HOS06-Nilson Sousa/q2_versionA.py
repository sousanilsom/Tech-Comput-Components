# Version A - using self.emp_count
class Employee:
    emp_count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first + '.' + last + '@company.com'
        self.emp_count += 1   # Version A


emp1 = Employee('Elliot', 'Alderson', 7000)
emp2 = Employee('Jean',   'Grey',     8000)

print(Employee.emp_count)
print(emp1.emp_count)
print(emp2.emp_count)
