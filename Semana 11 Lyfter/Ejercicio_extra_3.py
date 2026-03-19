class Vehicle:
    def __init__(self, brand, year):
        self._brand=brand
        self._year=year

    def get_info(self):
        return f"{self._brand} ({self._year})"
    


class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def get_info(self):
        return f"{super().get_info()} - {self.doors} Doors"


class Motorcycle(Vehicle):
    def __init__(self, brand, year, bike_type):
        super().__init__(brand, year)
        self.bike_type = bike_type

    def get_info(self):
        return f"{super().get_info()} - Tipo: {self.bike_type}"
    

# - TESTING AREA -

vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")

print(vehicle1.get_info())  
print(vehicle2.get_info())
