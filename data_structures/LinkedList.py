class Node:
    __slots__ = ("item", "next_item", "prev_item")
    # def __init__(self, item):
    #     self.item = item
    #     self.next_item = None
    #     self.prev_item = None
    
    def __init__(self, item, next_item=None):
        self.item = item
        self.next_item = next_item
        self.prev_item = None

    def get_item(self):
        return self.item

    def set_item(self, new_item):
        self.item = new_item

    def get_next(self):
        return self.next_item

    def set_next(self, new_next):
        self.next_item = new_next


class LinkedList:
    __slots__ = ("head", "tail", "_name", "_size")

    def __init__(self):
        self.head = self.tail = None
        self._name = self.__class__.__name__
        self._size = 0

    def __iter__(self):
        # Additional class for Iterator is not needed
        # Just move the code from __str__ method to here
        # (with appropriate updates which I specified, of course)
        return Iter(self.head)

    def __str__(self):
        # The logic you have here
        # should be implemented within
        # the __iter__ method, __str__
        # method should be simplified,
        # it should just call the __iter__
        # and return str result
        if self.head is None:
            return 'List is empty'

        elem = self.head
        my_list = []  # don't need list here
        while elem:
            # instead of appending element.item
            # to the new list - just 'yield' it :)
            my_list.append(elem.item)

            elem = elem.get_next()
        return f'Linked List: {my_list}'

    def __contains__(self, item):
        for element in self:
            if element == item:
                return True
        return False

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def index(self, item):
        current, counter = self.head, 0

        while counter < self._size:
            if current.get_item() == item:
                return counter
            current = current.get_next()
            counter += 1

        if counter == self._size - 1:
            raise ValueError

    def add(self, item):
        node = Node(item, self.head)
        self.head = node

        # here You forgot to add some check,
        # therefore my version of 'append'
        # doesn't work as expected

        self._size += 1

    def append(self, item):
        """
        Item is added to the Tail of the List
        """
        if self.head is None:
            self.head = Node(item, None)
            return
        elem = self.head
        while elem.get_next():
            # you iterate over the List elements here, this means that
            # for appending new element to the Tail of List you need
            # to go through the whole List starting from the Head
            # to the Tail. And this means that Complexity of this algorithm is
            # O(N) (where N - count of List elements), but expected Complexity
            # is O(1) (constant time, doesn't depend on count of Elements)
            # as it was implemented in my example of 'append'
            elem = self.tail = elem.get_next()
        elem.next_item = self.tail = Node(item, None)
        self._size += 1
        # node = Node(item)
        # if self._size == 0:
        #     node.set_next(self.head)
        #     self.head = self.tail = node
        # else:
        #     self.tail.set_next(node)
        #     self.tail = node
        #
        # self._size += 1

    def insert(self, item, position):
        if self._size == 0 or position <= 0:
            self.add(item)
        elif position > self._size - 1:
            self.append(item)
        else:
            node = Node(item)
            current, counter = self.head, 0
            previous = None

            while counter < self._size:
                if counter == position:
                    break
                previous = current
                current = current.get_next()
                counter += 1

            if previous is None:
                node.set_next(self.head)
                self.head = node
            else:
                node.set_next(current)
                previous.set_next(node)

            self._size += 1

    def __update_prev_and_next(self, prev, curr):
        if prev is None:
            self.head = curr.get_next()
        else:
            next_ = curr.get_next()
            if next_ is None:
                self.tail = prev
            prev.set_next(next_)

    def pop(self, position=None):
        if self._size == 0:
            raise IndexError(f"pop from empty list {self._name}")

        if position is not None and (position < 0 or position >= self._size):
            raise IndexError(f"pop index {position} is out of range")
        elif position is None:
            position = self._size - 1

        current, counter = self.head, 0
        previous = None

        while counter < self._size:
            if counter == position:
                break
            previous = current
            current = current.get_next()
            counter += 1

        self.__update_prev_and_next(previous, current)
        self._size -= 1

        return current.get_item()

    def remove(self, item):
        current = self.head
        previous, found = None, False
        counter = 0

        while counter < self._size:
            if current.get_item() == item:
                found = True
                break
            previous = current
            current = current.get_next()
            counter += 1

        if not found:
            raise ValueError(f"remove error: {item} not in {self._name}")
        else:
            self.__update_prev_and_next(previous, current)
            self._size -= 1


class Iter:
    def __init__(self, elem):
        self.elem = elem

    def __iter__(self):
        return self

    def __next__(self):
        if self.elem:
            result = self.elem.item
            self.elem = self.elem.next_item
            return result
        else:
            raise StopIteration






