class Employee:
    def __init__(self):
        self.name = input("Enter Employee name: ")
        self.emp_id = input("Enter Employee ID: ")
        self.dept = input("Enter Employee Dept: ")
        self.salary = int(input("Enter Employee Salary: "))
        
    def show_details(self):
        print("Employee Details")
        print(f"Name: {self.name}")
        print(f"ID: {self.emp_id}")
        print(f"Dept: {self.dept}")
        print(f"Salary: {self.salary}")

    def update_salary(self):
        self.salary = int(input("Enter new Salary: "))
        print(f"Updated Salary: {self.salary}")

e1 = Employee()
e1.show_details()
e1.update_salary()
