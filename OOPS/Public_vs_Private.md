# Public vs. Private Attributes in Python

In Python, the concepts of "public" and "private" attributes are handled by convention rather than strict enforcement. This guide explains the differences, how to use them, and the role of getter and setter methods.

---

## 1. Public Attributes

Public attributes are the default in Python. They can be freely accessed and modified from anywhere—inside or outside the class.

**Convention**: Any attribute without a leading underscore (`_`) is considered public.

### Example:

```python
class Employee:
    def __init__(self, name, salary):
        # Both name and salary are public attributes
        self.name = name
        self.salary = salary

# Create an instance of the Employee class
emp = Employee("Alice", 80000)

# --- Accessing and Modifying Public Attributes ---

# 1. Direct Reading
print(f"Employee Name: {emp.name}")  # Output: Employee Name: Alice

# 2. Direct Writing/Modification
print(f"Initial Salary: {emp.salary}") # Output: Initial Salary: 80000
emp.salary = 90000  # Directly changing the value
print(f"Updated Salary: {emp.salary}") # Output: Updated Salary: 90000

# The problem: No control over the values
emp.salary = -500 # This is illogical, but Python allows it
print(f"Salary after invalid update: {emp.salary}") # Output: Salary after invalid update: -500
```

**Pros**:
*   Simple and straightforward to use.
*   Less code required (no need for methods to access them).

**Cons**:
*   **No Control**: You cannot control how the attribute is modified. This can lead to invalid or inconsistent data in your objects.
*   **Breaks Encapsulation**: It exposes the internal state of the object, making your code more fragile. If you later decide to change how the attribute is stored, you will have to update all the code that accesses it directly.

---

## 2. Private Attributes

Private attributes are intended to be accessible only from within the class. This is a way to hide the internal state and prevent direct, uncontrolled modification from outside.

**Convention**: An attribute with a double leading underscore (`__`) is considered private. Example: `self.__marks`.

This triggers **Name Mangling**. Python automatically changes the name of the attribute to `_ClassName__attributeName`. This makes it difficult (but not impossible) to access from outside the class.

### Example:

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.__gpa = gpa # __gpa is a private attribute

# Create an instance
stu = Student("Bob", 3.5)

# --- Attempting to Access Private Attributes ---

# This will fail with an AttributeError
try:
    print(stu.__gpa)
except AttributeError as e:
    print(f"Error: {e}") # Output: Error: 'Student' object has no attribute '__gpa'

# You can still access it if you know the mangled name (but you shouldn't!)
print(f"Accessing via name mangling: {stu._Student__gpa}") # Output: 3.5
```

**Pros**:
*   **Encapsulation**: Hides the internal implementation of the class.
*   **Control**: Prevents accidental modification from outside the class.

**Cons**:
*   Requires methods (getters and setters) to be accessed from the outside, which means more code.

---

## 3. Getters and Setters: Controlled Access

Getters and setters are methods that provide controlled read and write access to an attribute. They are the standard way to work with private attributes.

*   **Getter**: A method to retrieve the value of an attribute.
*   **Setter**: A method to modify the value of an attribute, often including validation logic.

### Detailed Example:

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.__gpa = gpa # Private attribute

    # Getter method for __gpa
    def get_gpa(self):
        """Returns the value of the private __gpa attribute."""
        return self.__gpa

    # Setter method for __gpa
    def set_gpa(self, new_gpa, admin_password):
        """Sets the value of __gpa only if the password is correct and the GPA is valid."""
        if admin_password != "admin123":
            print("Authentication failed. Cannot change GPA.")
            return

        if 0.0 <= new_gpa <= 4.0:
            self.__gpa = new_gpa
            print("GPA has been successfully updated.")
        else:
            print("Invalid GPA. Please provide a value between 0.0 and 4.0.")

# --- Using Getters and Setters ---
stu = Student("Charlie", 3.8)

# 1. Reading the GPA using the getter
print(f"Initial GPA: {stu.get_gpa()}") # Output: Initial GPA: 3.8

# 2. Trying to set a new GPA with the wrong password
stu.set_gpa(3.9, "wrong_password") # Output: Authentication failed...
print(f"GPA after failed attempt: {stu.get_gpa()}") # Output: 3.8

# 3. Trying to set an invalid GPA with the correct password
stu.set_gpa(5.0, "admin123") # Output: Invalid GPA...
print(f"GPA after invalid value: {stu.get_gpa()}") # Output: 3.8

# 4. Setting a valid GPA with the correct password
stu.set_gpa(3.7, "admin123") # Output: GPA has been successfully updated.
print(f"Final GPA: {stu.get_gpa()}") # Output: Final GPA: 3.7
```

This example shows the true power of setters: they act as a gatekeeper, ensuring that the object's state remains valid and consistent.

---

## Summary: Public vs. Private

| Feature             | Public Attribute (`self.age`)                               | Private Attribute (`self.__marks`)                          |
| ------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| **Access**          | Direct, from anywhere (`obj.age`)                           | Indirect, through methods (`obj.get_marks()`)               |
| **Modification**    | Direct, from anywhere (`obj.age = 25`)                      | Indirect, through methods (`obj.set_marks(95)`)             |
| **Control**         | None. Any value can be set.                                 | Full control. Setter methods can validate and reject changes. |
| **Encapsulation**   | Broken. Exposes internal state.                             | Preserved. Hides internal state.                            |
| **Use Case**        | For simple data that doesn't need validation or logic.      | For critical data that must be protected and validated.     |

This covers the fundamental differences and best practices for using public and private attributes in Python.
