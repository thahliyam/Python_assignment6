# Question 2: (5 Marks) Create a Python module named employee that contains a class Employee with attributes
# name, salary and methods get_name() and get_salary(). Write a program to use this module to create an object
# of the Employee class and display its name and salary.
class Employee:
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

        def get_name(self):
            print(f"Employee Name: {self.name}")

        def get_salary(self):
            print(f"Employee Salary: {self.salary}")

