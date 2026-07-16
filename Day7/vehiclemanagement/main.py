from car import Car
from ev import EV
from polymorphism import Overloadingdemo


#create object for class
car1 = Car("Toyota", "Camry", 2020)
ev1 = EV("Tesla", "Model 3", 2022, 75)

car1.set_owner("Alice")
print(car1.get_owner())

#call methods on the objects
car1.start_engine()
car1.show_info()

ev1.show_info()
ev1.charge_battery()
ev1.start_engine()



