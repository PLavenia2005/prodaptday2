#define a class

class Car:
    def __init__(carmodel, brand, model, year):
        carmodel.brand=brand
        carmodel.model=model
        carmodel.year=year
        carmodel.__owner=None #private attribute


    def start_engine(carmodel):
        print(f"The engine of {carmodel.brand} {carmodel.model} is starting.")

    def show_info(carmodel):
        print(f"Car Info: {carmodel.brand} {carmodel.model}, Year: {carmodel.year}")


    def set_owner(carmodel, owner):
        if not carmodel.__owner:
            carmodel.__owner= owner
        else:
            print(f"The car already has an owner: {carmodel.__owner}. Cannot change owner.")
            # print(f"Owner of {carmodel.brand} {carmodel.model} is set to {carmodel.owner}.")

    def get_owner(carmodel):
        return carmodel.__owner
#create an object of the class

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)
print(car1.brand) #output: Toyota
#print( car1.__owner)
car1.set_owner("Alice")
print(car1.get_owner())

car1.set_owner("Bob")
print(car1.get_owner())

#call methods on the objects
car1.start_engine()
car1.show_info()

car2.start_engine()
car2.show_info()

#another way to call methods on the objects using a list of objects
cars = [car1, car2]

for car in cars:
    car.start_engine()
    car.show_info()

