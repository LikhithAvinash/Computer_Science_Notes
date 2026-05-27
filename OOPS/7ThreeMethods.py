class Employee:

    company = "Google"   # class attribute (shared by all employees)

    def __init__(self, name, salary):
        self.name = name         # instance attribute
        self.salary = salary     # instance attribute

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @staticmethod
    def is_valid_salary(amount):
        return amount > 0


# Creating objects
e1 = Employee("Likith", 50000)
e2 = Employee("Rahul", 70000)

# Instance attributes
print(e1.name)
print(e2.salary)

# Class attribute
print(e1.company)
print(e2.company)

# Class method changes shared class attribute
Employee.change_company("Microsoft")

print(e1.company)
print(e2.company)

# Static method
print(Employee.is_valid_salary(5000))
print(Employee.is_valid_salary(-100))