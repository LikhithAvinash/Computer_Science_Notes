class students:
    # constructor
    def __init__(self,name,cls,marks,age):
        self.name = name
        self.cls = cls
        self.__marks = marks
        self.age = age

    # getter method
    def get_marks(self):
        return self.__marks

    # setter method
    def set_marks(self,new_marks,passcode):

        if (passcode == '0000'):

            if 0 <= new_marks <= 100:
                self.__marks = new_marks
            else:
                print("Invalid marks. Marks should be between 0 and 100.")

        else:
            print(f'Wrong Passcode {passcode}')

    # Getter for public attribute 'age'
    def get_age(self):
        return self.age

    # Setter for public attribute 'age' with validation
    def set_age(self, new_age):
        if new_age > 0:
            self.age = new_age
        else:
            print("Invalid age. Age must be positive.")

    def Age(self):
        print(self.age)

    # instance method
    def study(self):
        print(f"I am studying in {self.clg} college")
    
    # instance method
    def play(self):
        print(f"I play a lot here")

s1 = students('Likhith',10,100,12)
s2 = students('rishik',10,90,14)

########################################################################################

# Getting the initial marks of s1
print("Initial marks for s1:", s1.get_marks())

# Setting new marks for s1
s1.set_marks(50,'0001')
print("Updated marks for s1:", s1.get_marks())

# Trying to set invalid marks
s1.set_marks(150,'0000')
print("Marks for s1 after trying to set to 150:", s1.get_marks())

# Setting valid marks again
s1.set_marks(30,'0000')
print("Final marks for s1:", s1.get_marks())

########################################################################################
print("\n--- Operations on Public Attribute 'age' ---")

# Getting the initial age of s1 (direct access)
print("Initial age for s1:", s1.age)

# Setting a new age for s1 (direct modification)
print("Setting age for s1 to 25")
s1.age = 25
print("Updated age for s1:", s1.age)

# Setting an invalid age - public attributes have no protection
print("Setting age for s1 to -5 (invalid, but allowed)")
s1.age = -5
print("Final age for s1:", s1.age)

########################################################################################
print("\n--- Operations on Public Attribute 'age' with Getters and Setters ---")
print()
# Resetting age to a valid value before starting
s1.age = 12 
print("Initial age for s1 (using get_age):", s1.get_age())

# Setting a new age for s1 using the setter
s1.set_age(30)
print("Updated age for s1 (using get_age):", s1.get_age())

# Trying to set an invalid age using the setter
s1.set_age(-10)
print("Age for s1 after trying to set to -10:", s1.get_age())



