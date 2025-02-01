'''
28.	Write a class called Time whose only field is a time in seconds. 
It should have a method called convert_to_minutes that returns a string of minutes
and seconds formatted as in the following example: if seconds is 230, 
the method should return '3:50'. It should also have a method called convert_to_hours
that returns a string of hours, minutes, and seconds formatted analogously to the previous method.
'''

class Time:
    def __init__(self,seconds):
        self.seconds = seconds
    
    def convert_to_minutes(self):
        minutes= self.seconds//60
        remaining_seconds = self.seconds % 60
        return f"{minutes}:{remaining_seconds}"
    def convert_to_hours(self):
        minutes= self.seconds//60
        hours = minutes//60
        remaining_minutes = minutes%60
        remaining_seconds = self.seconds % 60
        return f"{hours}:{remaining_minutes}:{remaining_seconds}"
               
t = Time(3666)
print(t.convert_to_minutes())  
print(t.convert_to_hours())
    
    
    
    
