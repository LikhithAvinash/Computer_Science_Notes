class something:
    val = 0

    def __init__(self,name,cls):
        self.res = 0
        self.name = name
        self.cls = cls
        something.val = something.val + 1
        self.val = something.val + 1
       
        self.res = self.res + 1

s = something('Likhith',3)
s1 = something('Avinash',4)

print(something.val)
print(s.res,s.val)
print(s1.res,s.val)
print(something.val)

print('vs')

class something:
    val = 0

    def __init__(self,name,cls):
        self.res = 0
        self.name = name
        self.cls = cls
        self.val = something.val + 1
        something.val = something.val + 1
        
        self.res = self.res + 1

s = something('Likhith',3)
s1 = something('Avinash',4)

print(something.val)
print(s.res,s.val)
print(s1.res,s.val)
print(something.val)

print('something.val is stored at class level but self.val stored such 2nd call it re-initiates')

print('Because of this it would start from 0...but when it is at class it doesnt happen in that way')
    
