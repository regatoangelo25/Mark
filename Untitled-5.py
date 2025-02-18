class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"{self.name} received a raise of ${amount:.2f}. New salary: ${self.salary:.2f}")
        else:
            print("Raise amount must be positive.")

    def display_employee(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary:.2f}")
        print("-" * 30)

employee = Employee("Jhon Lyod", "Security", 12500)

employee.display_employee()

employee.give_raise(200)

employee.display_employee()