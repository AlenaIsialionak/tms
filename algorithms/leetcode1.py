class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_begin(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
    def inser_at_the_end(self,val):
        if self.head is None:
            self.insert_begin(val)
        else:
            prev = None
            current = self.head
            while current:
                prev = current
                current = current.next
            node = Node(val)
            prev.next = node

    def print(self, sp=None):
        linked_list = []
        if sp:
            current = sp
        else:
            current = self.head

        while current:
            linked_list.append(current.val)
            current = current.next

        return linked_list
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_elem = current.next
            current.next = prev
            prev = current
            current = next_elem
        return prev
    def isPalindrom(self):
        l1 = self.print()
        l2 = []
        prev = None
        current = self.head
        while current:
            next_elem = current.next
            current.next = prev
            prev = current
            current = next_elem
        l2 = self.print(prev)
        return l1 == l2


    def size_list(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next
        return size

    def pairSum(self):
        size = self.size_list()
        current = self.head
        l1, l2 = [], []
        for _ in range(size//2):
            l1.append(current.val)
            current = current.next
        while current:
            l2.append(current.val)
            current = current.next
        max_sum = l1[0] + l2.pop()
        for i in l1[1:]:
            m = i + l2.pop()
            if m > max_sum:
                max_sum = m
        return max_sum
    def remove_elements(self, val: int):
        if not self.head:
            return
        while self.head.val == val:
            self.head = self.head.next
            if not self.head:
                return
        current = self.head
        prev = None
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next


    # def insert(self, elem):
    #     if self.head is None:
    #         self.insert_begin(elem)
    #     else:
    #         current = self.head
    #         node = Node(elem)
    #         prev = None
    #         while current:
    #             if current.val >= elem:
    #                 if prev is None:
    #                     self.insert_begin(elem)
    #                     break
    #                 prev.next = node
    #                 node.next = current
    #                 break
    #             prev = current
    #             current = current.next

    def merge_k_sorted_list(self, lists):
        def merge_two_sorted_lists(self, l1, l2):
            l1, l2 = l1.head, l2.head
            current = self.head
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            if l1 or l2:
                current.next = l1 or l2


        if not lists:
            return None

        left, right = 0, len(lists)-1
        while right > 0:
            if left >= right:
                left = 0
            else:
                lists[left] = merge_two_sorted_lists(self, lists[left], lists[right])
                left += 1
                right -= 1
                lists = lists[0].next
            return lists


    def make_a_cycle_linked_list(self):

        atbegin = self.head.next.next
        print(atbegin.val)
        prev = None
        current = self.head
        while current:
            prev = current
            current = current.next

        prev.next = atbegin


    def find_cycle_in_linked_list(self):
        real, fast = self.head, self.head
        while fast and fast.next:
            real = real.next
            fast = fast.next.next
            if real == fast:
                return True
        return False

    def find_index_of_cycle_in_linked_list1(self):
        real = self.head
        links = []
        while real and real.next:
            links.append(real)
            real = real.next
            if real in links:
                ind = links.index(real)
                return ind

    def find_index_of_cycle_in_linked_list2(self):
        real, fast = self.head, self.head
        while fast and fast.next:
            real = real.next
            fast = fast.next.next
            if real == fast:
                real = self.head
                while real != fast:
                    real = real.next
                    fast = fast.next
                return real.val
        return False


    def middle_linked_list(self):
        if self.head is None:
            return
        real, fast = self.head, self.head
        while fast and fast.next:
            fast = fast.next.next
            real = real.next

        return real.val








new_list1 = Linked_list()
for i in [1, 4, 7, 8, 10, 11]:
    new_list1.inser_at_the_end(i)
print(new_list1.print())
# new_list2 = Linked_list()
# for i in [1, 2, 3, 21]:
#     new_list2.inser_at_the_end(i)
# sorted_list = Linked_list()
# sorted_list.insert_begin(0)
# print(sorted_list.merge_k_sorted_list([new_list1, new_list2]))
# print(sorted_list.print())


# print(new_list1.find_cycle_in_linked_list())
new_list1.make_a_cycle_linked_list()
# print(new_list1.find_cycle_in_linked_list())
# print(new_list1.find_index_of_cycle_in_linked_list())
print(new_list1.find_index_of_cycle_in_linked_list2())
# print(new_list1.middle_linked_list())



# new_list.remove_elements(7)
# print(new_list.print())






# def removeElement(nums, val: int) -> int:
#     new_list = nums.copy()
#     for i in new_list:
#         if i == val:
#             nums.remove(i)
#     return len(nums)
#
# print(removeElement([0,1,2,2,3,0,4,2], 2))
