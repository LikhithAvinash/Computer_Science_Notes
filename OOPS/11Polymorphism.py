# Polymorphism in Python

class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Creating instances of the classes
animal = Animal()
dog = Dog()
cat = Cat()

print(animal.speak())  # Output: Animal speaks
print(dog.speak())     # Output: Dog barks
print(cat.speak())     # Output: Cat meows

# Method Overloading

'''
if:
    if the function inside the child class is not written and when the client is 
    asking for it then it returns the answer which is written from the parent class

else: 
    if the child class has the same function and also something that is printed
    or returned with or without using attributes then that is been used

so the child checks whether he has an answer if he don't then goes to the parent
and provide the answer
'''

class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

# Creating an instance of the class
math_op = MathOperations()

# Calling the add method with different numbers of arguments
print(math_op.add(2, 3))       # Output: 5
print(math_op.add(2, 3, 4))    # Output: 9

# Operator Overloading

'''
It is about the function that can handle different parameters given
without going through error and return answer for the particular parameters
'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Creating instances of the Vector class
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Using the + operator on Vector objects
v3 = v1 + v2

print(v3)  # Output: Vector(6, 8)

'''
we load the function for different obj once the objects loading is done
then do the math and return it based on the operator we choose
'''
