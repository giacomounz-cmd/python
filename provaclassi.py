
from car import Car

car1=Car("panda",2009,"arancione","sarria")

car2=Car("chiron","2025","blu","jack")

print(car1.color,car1.proprietario)

print(car2.color,car2.proprietario)

car1.guida()

print(car1.car_general)

print(Car.car_general)#varibile della classe

print(Car.car_numb)

for og in Car.ordine:
    print(f"\t{og}")


        