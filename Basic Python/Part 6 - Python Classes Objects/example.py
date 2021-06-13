class Employee:
    total_employee = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employee += 1

    def show_total_employee(self):
        print("Total employee: ", Employee.total_employee)

    def show_profile_employee(self):
        print("Nama: ", self.name)
        print("Salary: ", self.salary)

employee_one = Employee("Hari", 13000000)
employee_two = Employee("Farhan", 10000000)
employee_three = Employee("Aang", 7000000)

employee_one.show_total_employee()
employee_one.show_profile_employee()
employee_two.show_total_employee()
employee_two.show_profile_employee()
employee_three.show_total_employee()
employee_three.show_profile_employee()
