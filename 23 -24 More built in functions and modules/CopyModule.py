print('''python program #23
Hashir - May 30 2018
This program is an introduction to the copy module
''')

import copy

class Car:
    pass
car1 = Car()
car1.wheels = 4
print(car1.wheels)
print("The initial object has a certain value of 4")

car2 = car1
car2.wheels = 3
print(car1.wheels)
print("The shallow copied object has the same memory address, both have the same value")

car3 = copy.copy(car1)
car3.wheels = 6
print(car1.wheels)
print("The deep copied object contains its own value and memory address")
