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
            return 'The car has started moving'
        else:
            return 'The car is already moving'

    @classmethod
    def stop(cls):
        if not cls.CONDITION:
            cls.CONDITION = True
            return 'The car has been stopped'

        else:
            return 'The car had already been stopped'

    def birthday(self):
        self.age += 1
        return self.age


my_car = Auto('audi', 5, ' black','5533', 1745)

print(my_car.birthday())
print(my_car.birthday())
print(my_car.birthday())
print(my_car.move())
print(my_car.move())
print(my_car.stop())
print(my_car.stop())



