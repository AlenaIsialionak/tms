from dataclasses import dataclass


@dataclass(frozen=True)
class MyDataClass1:
    a: str
    b: str
    c: list

@dataclass
class MyDataClass2:
    # a: str
    # b: str
    # c: list

    @classmethod
    def build(cls, a, b, c):
        try:
            if isinstance(a, str) and isinstance(b, int) and isinstance(c, list):
                return MyDataClass1(a, b, c)
            else:
                raise TypeError('Parameters were entered incorrectly')
        except TypeError as err:
            print(err)


person1 = MyDataClass2.build("TEST", 34, [1, 2, 3])
print(person1)

person2 = MyDataClass2.build(100, 33, [1, 2, 3])