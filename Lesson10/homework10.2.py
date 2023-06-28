from datetime import datetime


class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self._year = None

    def __iter__(self):
        for attr in self.__dict__.values():
            yield attr

    @property
    def birth(self):
        print('getter')
        return self._year

    @birth.setter
    def birth(self, now):
        print('setter')
        self._year = now - self.age

    @classmethod
    def verify(cls,other):
        if not isinstance(other, Person):
            raise TypeError('The objects being compared must be instances')

    def __eq__(self, other):
        print('equal')
        self.verify(other)
        return self.name.lower() == other.name.lower() and self.age == other.age

    def __ge__(self, other):
        print('greater than or equal to')
        self.verify(other)
        return self.age >= other.age

    def __lt__(self, other):
        print('less than')
        self.verify(other)
        return self.age < other.age


person1 = Person('asdfg', 91)

print(person1.__dict__)
print('*************')
person1.birth = datetime.now().year
print('*************')
print(f'year: {person1.birth}')
print(person1.birth)
print('*************')
print(person1.__dict__)
person2 = Person('Adfg', 101

print(person1 == person2)
print(person1 != person2)
print(person1 >= person2)
print(person1 <= person2)
print(person1 > person2)
print(person1 < person2)


