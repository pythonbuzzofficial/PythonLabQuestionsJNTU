'''
Write a class called Converter. The user will pass a length and a unit when 
declaring an object from the class— for example, c = Converter(9,'inches').
The possible units are inches, feet, yards, miles, kilometers, meters, centimeters, and millimeters. 
For each of these units there should be a method that returns the length converted into those units. 
For example, using the Converter object created above, the user could call c.feet() 
and should get 0.75 as the result.
'''

class Converter:
    
    conversion_factors = {
        "inches": 1,
        "feet": 12,
        "yards": 36,
        "miles": 63360,
        "millimeters": 25.4,  # 1 inch = 25.4 mm
        "centimeters": 2.54,  # 1 inch = 2.54 cm
        "meters": 0.0254,  # 1 inch = 0.0254 m
        "kilometers": 0.0000254  # 1 inch = 0.0000254 km
    }
    
    def __init__(self,length,unit):
        if unit not in self.conversion_factors:
            raise ValueError("Invalid Unit.Choose from inches,feet,yards,miles,millimeters,centimeters,meters,kilometers")
        
        self.length_in_inches = length
    
    def inches(self):
        return self.length_in_inches  
    def feet(self):
        return self.length_in_inches /self.conversion_factors['feet']
    def yards(self):
        return self.length_in_inches / self.conversion_factors["yards"]
 
    def miles(self):
        return self.length_in_inches / self.conversion_factors["miles"]
    def millimeters(self):
        return self.length_in_inches * 25.4
    
    def centimeters(self):
        return self.length_in_inches * 2.54
    
    def meters(self):
        return self.length_in_inches * 0.0254
    
    def kilometers(self):
        return self.length_in_inches * 0.0000254

c = Converter(9,'inches')

print(c.feet())
print(c.meters())
print(c.miles())