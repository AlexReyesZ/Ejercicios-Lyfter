class Rectangle:
    def __init__(self, width, height):

        if width < 0 or height <0:
            raise ValueError (' Error: The value can not be negative')
        

        self.width=width
        self.height=height


    def get_area(self):

        return self.width * self.height
    

    def get_perimeter(self):

        return 2 *(self.width * self.height)
    

try:
    user_width=float(input('Enter the width: '))
    user_hight=float(input('Enter the height:'))

    rectangle=Rectangle(user_width, user_hight)

    print(f'Area: {rectangle.get_area()}')
    print(f'Perimeter: {rectangle.get_perimeter()}')


except ValueError as e:
    print(e)