from abc import ABC, abstractmethod
import math



class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# POR QUÉ: El decorador @abstractmethod obliga a que Circle, 
# Square, etc., tengan su propia versión de este método.
# Si no lo incluyen, Python dará un error.

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius

    def calculate_area(self):
        return math.pi * (self.radius **2)  # Fórmula: π * r²
    
    def calculate_perimeter(self):
        return 2*math.pi *self.radius    # Fórmula: 2 * π * r
    

class Square(Shape):
    def __init__(self, side):
        self.side=side

    def calculate_area(self):
        return self.side ** 2
    
    def calculate_perimeter(self):
        return 4 * self.side
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width=width
        self.height=height   

    def calculate_area(self):
        return self.width * self.height
    

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)    


# --- TESTING AREA ---
shapes = [
    Circle(5),
    Square(4),
    Rectangle(3, 6)
]

for s in shapes:
    
    print(f"Shape: {type(s).__name__}")
    print(f"Area: {s.calculate_area():.2f}")
    print(f"Perimeter: {s.calculate_perimeter():.2f}")
    print("-" * 20)
# No importa si es círculo o cuadrado, todos tienen los mismos métodos.
# Esto es POLIMORFISMO.