class Circule:
    def __init__(self, radius):
        self.radius=radius
    
    def get_area(self):

        area=3.14 *(self.radius * self.radius)
        return area
    
my_circule=Circule(5)
result=my_circule.get_area()

print(f'The radius is:{my_circule.radius}')
print(f'The area is: {result}')        

