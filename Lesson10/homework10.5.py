import time


class MyStack:

    time1 = 0

    def __init__(self, new_collection=[ ]):
        self.new_collection = new_collection
        self.inner_collection = [a for a in new_collection]

    def time_decorator(func):
        def wrapper(self, *args, **kwargs):
            start_time = time.time()
            func(self, *args, **kwargs)
            self.time1 = (time.time()-start_time)*1000
            return self.time1
        return wrapper

    @time_decorator
    def push(self, elem):
        return self.inner_collection.insert(0, elem)
    @time_decorator
    def pop(self):
        return self.inner_collection.pop(0)

    def is_empty(self):
        if self.inner_collection:
            return True
        return False


p = MyStack([1, 1, 2, 3])
p.push(4)
print(p.__dict__)
p.pop()
print(p.__dict__)
