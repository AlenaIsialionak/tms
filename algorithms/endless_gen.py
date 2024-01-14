from typing import Iterable, Collection, Generator
def endless_gen(some_range: Iterable):
    while True:
        if isinstance(some_range, Generator):
            yield from some_range
        else:
            for item in some_range:
                yield item


base_collection_tipe = (str, list, tuple, set, dict)
value = 'HelloWorld'


str_gen = (c for c in value)

gen1 = list(range(1, 10))
print(gen1)
# for i in endless_gen(gen1):
#     print(i)