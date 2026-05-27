class parents:
    def __init__(self,name,id,cllg):
        self.name = name
        self.id = id
        self.cllg = cllg
    
    def login(self):
        print('User Logged in')

    def logout(self):
        print('User logged out')
    

class child(parents):
    def __init__(self,intrest : str):
        self.intrest = intrest

    def studInt(self):
        print(f'Student has Intrest on : {self.intrest}')

c1 = child('Coding')
c2 = child('Drawing')

c1.studInt()
c1.login()

'''
HERE you might see there is no issue because it is just a print statment
But if an attribute is given then it throws an ERROR

That is why u need super key
'''

class parents:
    def __init__(self,name,id,cllg):
        self.name = name
        self.id = id
        self.cllg = cllg
    
    def login(self):
        print(f'User :{self.name} has Logged in')

    def logout(self):
        print('User logged out')
    

class child(parents):
    def __init__(self,intrest : str):
        self.intrest = intrest

    def studInt(self):
        print(f'Student has Intrest on : {self.intrest}')

c1 = child('Coding')
c2 = child('Drawing')

c1.studInt()
c1.login()

'''
Here in our child class there is no name attribute that is defined 
so we are getting ERROR

So Super key can RESOLVE this

See that code in /9Inheritance2.py file
'''
