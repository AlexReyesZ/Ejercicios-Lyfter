
#Class Car es el molde MOLDE
#Car_whels es el ATRIBUTO
#my_car_1 es el OBJETO
#my_first_method es un metodo se podria decir que son funciones dentro de las clases
#dentro de los metodos se pueden poner mas de un parametro
#LAS CLASES PUEDEN TENER CUANTOS ATRIBUTOS Y METODOS QUERAMOS
# El def __init__ hace referencia al conductor, los conductores se usan cuando no queremos que los atributos sean cambiantes 

class Car:
    car_whels=4

my_car_1=Car()
print(my_car_1.car_whels)

my_car_2=Car()
my_car_2.car_whels=6
print(my_car_2.car_whels)


my_car_3=Car()
my_car_3.car_whels=8
print(my_car_3.car_whels)
#---------------------------------------------------------------------
class CarPremiun:
    car_whels=4
    gas_type= 'Disel'

    def my_first_method(self):
        print('Hello world')

    def show_history(self, miles, crashes):
        print(f'This car has {miles} Miles, {crashes} Crashes and {self.car_whels} whels')

    def improve_engine(self):
        if self.gas_type=='Disel':
            print('Changin Disel motor to super gasoline motor')
            self.gas_type='Super'

        else:
            print('This car is already super gasoline motor')


my_car_4=CarPremiun()
my_car_4.my_first_method()
my_car_4.show_history(2000,0)


my_car_5=CarPremiun()
my_car_5.show_history(14000,2)

#------------------------------------------------------------------------

class CarPremiun:
    car_whels=4
    gas_type= 'Disel'

    def my_first_method(self):
        print('Hello world')

    def show_history(self, miles, crashes):
        print(f'This car has {miles} Miles and {crashes} Crashes')

    def improve_engine(self):
        if self.gas_type=='Disel':
            print('Changing Disel motor to super gasoline motor')
            self.gas_type='Super'

        else:
            print('This car is already super gasoline motor')

print('------------------')
print('My first Car')
my_car_6=CarPremiun()
print('Car fabricated')
print(my_car_6.gas_type)
my_car_6.improve_engine()
print('Car improved')
print(my_car_6.gas_type)
my_car_6.improve_engine()
print('-'*20)

#----------------------------------------------------------------

class Person():
    def __init__(self, name):
        print(f'Have borned a person called {name}!')
        self.name=name
        self.age=0 

person_1=Person('Alex')
person_1.age=28
print(person_1.age)
print(person_1.name)