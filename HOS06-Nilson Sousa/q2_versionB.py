# Version B - using Employee.emp_count
class Employee:
    emp_count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first + '.' + last + '@company.com'
        Employee.emp_count += 1   # Version B


emp1 = Employee('Elliot', 'Alderson', 7000)
emp2 = Employee('Jean',   'Grey',     8000)

print(Employee.emp_count)
print(emp1.emp_count)
print(emp2.emp_count)
