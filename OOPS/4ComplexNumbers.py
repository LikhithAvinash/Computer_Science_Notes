''''
For Complex Numbers add,sub,mult,div through OOPS between 2 numbers
'''

class ComplexNumbers:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __str__(self):
        if self.real == 0:
            return f'{self.img}j'
        
        elif self.img < 0:
            return f'{self.real} {self.img}j'

        else:
            return f'{self.real} + {self.img}j'
    
    def __add__(self,other): ## (arg1,arg2) can be written but this is more pythonic way
        resultReal,resultImg = 0,0

        resultReal, resultImg = self.real + other.real,self.img + other.img

        res = ComplexNumbers(resultReal,resultImg)

        return res

    def __sub__(self,other): 
        resultReal,resultImg = 0,0

        resultReal, resultImg = self.real - other.real,self.img - other.img

        res = ComplexNumbers(resultReal,resultImg)

        return res
    
    def __mul__(self,other): 
        resultReal,resultImg = 0,0

        resultReal = ((self.real * other.real) - (self.img * other.img))
        resultImg = ((self.real * other.img) + (self.img * other.real))

        res = ComplexNumbers(resultReal,resultImg)

        return res
    
    def __truediv__(self, other):
        denominator = other.real**2 + other.img**2
        if denominator == 0:
            raise ZeroDivisionError("division by zero")
        
        resultReal = (self.real * other.real + self.img * other.img) / denominator
        resultImg = (self.img * other.real - self.real * other.img) / denominator

        res = ComplexNumbers(resultReal, resultImg)
        return res
    
    def __eq__(self,other):
        return self.real == other.real and self.img == other.img 

cn1 = ComplexNumbers(5,10)
cn2 = ComplexNumbers(6,12)

print(cn1+cn2)
print(cn1-cn2)
print(cn1*cn2)
print(cn1/cn2)
print(cn1==cn2)

print("I've used Magic Methods")
