import random


class RandomValue:

    def __init__(self, limit):
        self.random = range(1, 101)
        self.limit = limit

    def generator_function(self):
        for _ in range(self.limit):
            yield random.choice(self.random)


my_limit = int(input("Enter a limit: "))
my_random = RandomValue(my_limit)

results = [elem for elem in my_random.generator_function()]
print(results)

assert len(results) == my_limit
for i in results:
    assert i is not None
