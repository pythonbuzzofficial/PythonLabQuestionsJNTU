'''
Write a Python class to implement pow(x, n) 
'''

class power:
    def calculate(self,x,n):
        return x**n
    
p = power()

print(p.calculate(10,3))
print(p.calculate(3,-3))
print(p.calculate(10,0))


