class Person:
    def __init__(self, name):
        self.name = name

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = [] 

    def add_passenger(self, person):
        
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} hopped on the bus.")
        else:
            print("The bus is full! Cannot add more passengers.")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} got off the bus.")
        else:
            print(f"{person.name} is not on this bus.")


school_bus = Bus(max_passengers=4)


person_1 = Person("Alex")
person_2= Person("Bob")
person_3= Person("Marilyn")
person_4= Person("Oscar")
person_5= Person("Vanesa")

# 3. Operations
school_bus.add_passenger(person_1)
school_bus.add_passenger(person_2)
school_bus.add_passenger(person_3)
school_bus.add_passenger(person_4) 
school_bus.add_passenger(person_5) 

school_bus.remove_passenger(person_1) 
school_bus.remove_passenger(person_2)