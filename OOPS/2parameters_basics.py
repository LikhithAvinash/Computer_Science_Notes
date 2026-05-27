class Students:
    def __init__(self,name,cls,id): # Initializes the object's attributes
        self.name = 'something' # This is called instance attribute assignment
        self.cls = '5'
        self.id = 10
    
s1 = Students('Likhith','Avinash',101) # obj created here 


##################################################
print('The Hardcoded will always be same no matter the parameter we pass')
##################################################

class students:
    def __init__(self, name, cls, id):
        self.name = name
        self.cls = cls
        self.id = id
    
s2 = students('Likhith', 'Avinash', 101)

print(s1.name)
print(s1.cls)
print(s1.id)
print('#######################################')
print(s2.name)
print(s2.cls)
print(s2.id)

print('Parameter changes Based on the value we pass')