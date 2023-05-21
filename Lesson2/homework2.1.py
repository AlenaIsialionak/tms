list1, list2, list3 = '123', '123', '123'
list4, list5 = [1,2], [1,2]
print(id(list1), id(list2), id(list3), sep = '\n')
print(id(list4), id(list5) , sep = '\n')
list1, list1, list3 = int(list1), list(list2), float(list3)
list4, list5 = bool(list4), bool(list5)
print()
print(id(list1), id(list2), id(list3), sep = '\n')
print(id(list4), id(list5) , sep = '\n')