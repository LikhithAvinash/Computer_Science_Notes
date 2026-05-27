## This only blueprint there is no object stored under __init__(self)


class students:
    def __init__(self): # creates obj

        name = 'Likhith' ## it is in class instant only so when the function ends
                         # it scopes end and also we defined name variable in a func
                         # but while printing if I a calling func it doesn't knoow it is calling
                         # variable
    
s1 = students()
print(s1) ## just address is stored of __init__ under student instance .. 
        # name is stored under class instance and then forgotted(has limitted scope as func)

## s1.name gives ERROR here


print('#########################################')

## This is blueprint and object is stored under __init__(self)

class Students:
    def __init__(self):
        self.name = 'Likhith'

s2 = Students()
print(s2.name) ## This is stored under student instance the name also