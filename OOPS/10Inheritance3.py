# 10Inheritance.py

class Company:
    def __init__(self, name):
        self.public_name = name
        # Protected attribute: Should only be accessed by this class or its children.
        self._project = "Project Phoenix"

    def _get_project_details(self):
        # Protected method.
        return f"Confidential details for {self._project}"

    # --- Public "getter" methods to safely expose protected info ---
    def get_project_name(self):
        """Good Practice: A public method to get the protected project name."""
        return self._project

    def show_project_details(self):
        """Good Practice: A public method that calls the protected method."""
        return self._get_project_details()

    def set_project(self, new_project_name):
        """Good Practice: A public method to safely change the protected project name."""
        if new_project_name and len(new_project_name) > 3:
            self._project = new_project_name
            print(f"(Project updated to: {self._project})")
        else:
            print("(Invalid project name. No change made.)")

class Department(Company):
    def __init__(self, name, department_name):
        super().__init__(name)
        self.department_name = department_name

    def show_department_project(self):
        """
        Case 1: Accessing a protected member from within a subclass.
        This is the correct and intended use.
        """
        print(f"--- Accessing from within the '{self.department_name}' Department (Correct) ---")
        # The child class 'Department' can access the parent's protected attribute.
        print(f"The current project is: {self._project}")
        # It can also call the parent's protected method.
        print(f"Details: {self._get_project_details()}")


# --- Setup ---
# Create an instance of the child class
dev_department = Department("TechCorp", "Development")


# --- Case 1: Good Practice - Correct access from within the child class ---
# This method is part of the child class and correctly accesses the protected member.
dev_department.show_department_project()


print("\n" + "="*50 + "\n")


# --- Case 2: Demonstrating Good vs. Bad Practice for external access ---

print("--- Accessing from outside the class ---")

# Bad Practice: Accessing protected members directly.
print("\n[Bad Practice] Direct, uncontrolled access:")
print(f"Direct access to _project: {dev_department._project}")
print(f"Direct call to _get_project_details(): {dev_department._get_project_details()}")
print("This is discouraged as it breaks encapsulation.")

# Good Practice: Using public methods to access the data.
print("\n[Good Practice] Controlled access via public methods:")
print(f"Access via get_project_name(): {dev_department.get_project_name()}")
print(f"Access via show_project_details(): {dev_department.show_project_details()}")
print("This is the correct way to expose internal data.")




'''
Summary:
If you are a child class (like Department): You can directly access and 
modify protected members (like self._project) from within your own methods. 
This is considered "good practice" because you are inside the class family.

If you are outside the class (in the main script): You cannot directly write 
to a protected member. This is "bad practice."
'''
