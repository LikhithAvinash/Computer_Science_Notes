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
    def __init__(self,intrest : str,name,id,cllg):
        super().__init__(name,id,cllg)
        self.intrest = intrest
        
    def studInt(self):
        print(f'Student has Intrest on : {self.intrest}')
        print(f'Student cllg is {self.cllg}')

c1 = child('coding','Liki',101,'Woxsen')
# c2 = child('Drawing','Rishi')

c1.studInt()
c1.login()


'''
LEARNING
1) When using super class I need to give all attributes not just the one we are using
'''