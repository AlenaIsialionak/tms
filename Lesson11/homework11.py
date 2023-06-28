import random


class RandomValue:

    def __init__(self, limit):
        self.random = range(1, 101)
        self.limit = limit

    def __iter__(self):
        return RandomValueIterator(self.random, self.limit)


class RandomValueIterator:

    def __init__(self, my_random, my_limit):
        self._my_random = my_random
        self.my_limit = my_limit
        self._curr_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curr_index < self.my_limit:
            result = random.choice(self._my_random)
            self._curr_index += 1
            return result
        else:
            raise StopIteration


my_limit = int(input("Enter a limit: "))
my_random = RandomValue(my_limit)

results = [elem for elem in my_random]
print(results)

assert len(results) == my_limit
for i in results:
    assert i is not None
