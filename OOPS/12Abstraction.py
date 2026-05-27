from abc import ABC, abstractmethod


# Abstract class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


# Child class
class Dog(Animal):

    def sound(self):
        print("Dog says: Bark")


# Child class
class Cat(Animal):

    def sound(self):
        print("Cat says: Meow")


# Normal function
def animal_sound(animal): ## just creating
    animal.sound() # calling is enough 

    #without knowing what the above 2 classes do
    # just know the class name and the function u want to call
    ## u don't need to know anything
    # --- THis is the details it is hiding


# Objects
d = Dog()
c = Cat()

# Function calls
animal_sound(d)
animal_sound(c)



'''
1) The parent abstract class defines what must be done
2) The child class defines how it is done
'''

from abc import ABC, abstractmethod

class AbstractShape(ABC):
    @abstractmethod
    def calculate_area(self):
        """
        This is an abstract method. Any class that inherits from
        AbstractShape MUST implement this method.
        """
        pass

    @abstractmethod
    def display(self):
        """Another abstract method."""
        pass

# Now, let's try to create subclasses.

class Circle2(AbstractShape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
    def display(self):
        print(f"This is a circle with radius {self.radius}")

class Rectangle2(AbstractShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
    # If we forget to implement display(), we will get an error.
    def display(self):
        print(f"This is a rectangle with width {self.width} and height {self.height}")

# If we try to instantiate a class that does not implement all abstract methods,
# Python will raise a TypeError.
# For example, if Rectangle2 did not implement display():
# rect = Rectangle2(4, 6)  # This would raise TypeError

# This enforces a common interface for all subclasses.
circle2 = Circle2(5)
rectangle2 = Rectangle2(4, 6)

print(f"Area of Circle2: {circle2.calculate_area()}")
circle2.display()

print(f"Area of Rectangle2: {rectangle2.calculate_area()}")
rectangle2.display()
