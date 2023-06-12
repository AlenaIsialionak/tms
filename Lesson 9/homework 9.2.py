from time import sleep


class Auto:

    CONDITION = True

    def __init__(self, brande, age, color, mark, weight):
        self.brande = brande
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    @classmethod
    def move(cls):
        if cls.CONDITION:
            cls.CONDITION = False
            print('The car has started moving')
        else:
            print('The car is already moving')

    @classmethod
    def stop(cls):
        if not cls.CONDITION:
            cls.CONDITION = True
            print('The car has been stopped')

        else:
            print('The car had already been stopped')

    def birthday(self):
        self.age += 1
        return self.age


class Truck(Auto):

    def __init__(self, brande, age, color, mark, weight, max_load=None):
        super().__init__(brande, age, color, mark, weight)
        self.max_load = max_load

    @classmethod
    def move(cls):
        if cls.CONDITION:
            print('Attention')
        super().move()

    def load(self):
        sleep(1)
        print('load')
        sleep(1)


class Car(Auto):

    def __init__(self, brande, age, color, mark, weight, max_speed=None):
        super().__init__(brande, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max_speed is {self.max_speed} km/h')


my_truck = Truck('ford', 5, ' black', '5593', 18000)

print(my_truck.birthday())
print(my_truck.birthday())
my_truck.move()
my_truck.move()
my_truck.load()
my_truck.stop()
print()
my_car = Car('audi', 5, ' black','5533', 1745, 237)
my_car.move()
my_car.move()
my_car.stop()
my_car.stop()






