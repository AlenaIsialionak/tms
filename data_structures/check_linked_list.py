from LinkedList import LinkedList


def check_linked_list_methods(my_list):

    # ADD
    my_list.add("ADD_1")
    print(my_list, "Size: {}".format(len(my_list)))

    my_list.add("ADD_2")

    # APPEND
    my_list.append(1)
    print(
        my_list,
        "Size: {}".format(len(my_list)),
        "Tail: {}".format(my_list.tail.get_item()),
    )
    my_list.append(2)
    print(
        my_list,
        "Size: {}".format(len(my_list)),
        "Tail: {}".format(my_list.tail.get_item()),
    )
    my_list.append(3)
    print(
        my_list,
        "Size: {}".format(len(my_list)),
        "Tail: {}".format(my_list.tail.get_item()),
    )
    my_list.append(4)
    print(
        my_list,
        "Size: {}".format(len(my_list)),
        "Tail: {}".format(my_list.tail.get_item()),
    )
    my_list.append(5)
    print(
        my_list,
        "Size: {}".format(len(my_list)),
        "Tail: {}".format(my_list.tail.get_item()),
    )
    print(my_list)

    assert [i for i in my_list] == ["ADD_2", "ADD_1", 1, 2, 3, 4, 5]
    #
    # ADD
    # """
    # Uncomment the lines bellow after the add() method will be implemented
    # """
    my_list.add("ADD_3")
    print(my_list, "Size: {}".format(len(my_list)))
    my_list.add("ADD_4")
    print(my_list, "Size: {}".format(len(my_list)))
    my_list.add("ADD_5")
    print(my_list, "Size: {}".format(len(my_list)))
    #
    # ASSERTIONS
    assert len(my_list) == 10
    assert [i for i in my_list] == [
        "ADD_5",
        "ADD_4",
        "ADD_3",
        "ADD_2",
        "ADD_1",
        1,
        2,
        3,
        4,
        5,
    ]
    print(f'index of the element "ADD_5": {my_list.index("ADD_5")}')
    assert my_list.index("ADD_5") == 0
    assert my_list.index(5) == len(my_list) - 1
    #
    # INSERT

    # Insert to TAIL
    my_list.insert("INSERT_1", 11)
    print(my_list, "Size: {}".format(len(my_list)))
    assert [i for i in my_list] == [
        "ADD_5",
        "ADD_4",
        "ADD_3",
        "ADD_2",
        "ADD_1",
        1,
        2,
        3,
        4,
        5,
        "INSERT_1",
    ]
    assert my_list.tail.item == "INSERT_1"
    assert len(my_list) == 11
    assert my_list.index("INSERT_1") == len(my_list) - 1

    # Insert to HEAD
    my_list.insert("INSERT_2", 0)
    # print(my_list, "Size: {}".format(len(my_list)))
    assert [i for i in my_list] == [
        "INSERT_2",
        "ADD_5",
        "ADD_4",
        "ADD_3",
        "ADD_2",
        "ADD_1",
        1,
        2,
        3,
        4,
        5,
        "INSERT_1",
    ]
    assert my_list.tail.item == "INSERT_1"
    assert len(my_list) == 12
    assert my_list.index("INSERT_1") == len(my_list) - 1
    assert my_list.index("INSERT_2") == 0

    # Insert to MIDDLE
    my_list.insert("INSERT_3", 5)
    # print(my_list, "Size: {}".format(len(my_list)))
    assert [i for i in my_list] == [
        "INSERT_2",
        "ADD_5",
        "ADD_4",
        "ADD_3",
        "ADD_2",
        "INSERT_3",
        "ADD_1",
        1,
        2,
        3,
        4,
        5,
        "INSERT_1",
    ]
    assert my_list.tail.item == "INSERT_1"
    assert my_list.head.item == "INSERT_2"
    assert len(my_list) == 13
    assert my_list.index("INSERT_1") == len(my_list) - 1
    assert my_list.index("INSERT_2") == 0
    assert my_list.index("INSERT_3") == 5
    assert my_list.index("ADD_1") == 6

    # POP

    # POP from TAIL
    res1 = my_list.pop()
    # print(my_list, "Size: {}".format(len(my_list)))
    assert res1 == "INSERT_1"
    assert my_list.head.item == "INSERT_2"
    assert my_list.tail.item == 5
    assert len(my_list) == 12
    assert [i for i in my_list] == [
        "INSERT_2",
        "ADD_5",
        "ADD_4",
        "ADD_3",
        "ADD_2",
        "INSERT_3",
        "ADD_1",
        1,
        2,
        3,
        4,
        5,
    ]
    assert my_list.index(5) == len(my_list) - 1

    # POP from HEAD
    res1 = my_list.pop(0)
    # print(my_list, "Size: {}".format(len(my_list)))
    assert res1 == "INSERT_2"
    assert my_list.head.item == "ADD_5"
    assert my_list.tail.item == 5
    assert len(my_list) == 11
    assert [i for i in my_list] == [
        "ADD_5",
        "ADD_4",
        "ADD_3",
        "ADD_2",
        "INSERT_3",
        "ADD_1",
        1,
        2,
        3,
        4,
        5,
    ]
    assert my_list.index(5) == len(my_list) - 1

    # POP from MIDDLE
    idx = 5
    res1 = my_list.pop(idx)
    # print(my_list, "Size: {}".format(len(my_list)))
    assert res1 == "ADD_1"
    assert my_list.head.item == "ADD_5"
    assert my_list.tail.item == 5
    assert len(my_list) == 10
    assert my_list.index(1) == idx
    assert [i for i in my_list] == [
        "ADD_5",
        "ADD_4",
        "ADD_3",
        "ADD_2",
        "INSERT_3",
        1,
        2,
        3,
        4,
        5,
    ]
    assert my_list.index(5) == len(my_list) - 1

    # REMOVE
    my_list.remove("INSERT_3")
    # print(my_list, "Size: {}".format(len(my_list)))
    assert my_list.head.item == "ADD_5"
    assert my_list.tail.item == 5
    assert len(my_list) == 9
    assert [i for i in my_list] == ["ADD_5", "ADD_4", "ADD_3", "ADD_2", 1, 2, 3, 4, 5]

    # ADD again!
    my_list.add("NEW_ADD")
    # print(my_list, "Size: {}".format(len(my_list)))
    assert my_list.head.item == "NEW_ADD"
    assert my_list.tail.item == 5
    assert len(my_list) == 10
    assert [i for i in my_list] == [
        "NEW_ADD",
        "ADD_5",
        "ADD_4",
        "ADD_3",
        "ADD_2",
        1,
        2,
        3,
        4,
        5,
    ]
    assert my_list.index("NEW_ADD") == 0

    # APPEND again!
    my_list.append("NEW_APPEND")
    # print(my_list, "Size: {}".format(len(my_list)))
    assert my_list.head.item == "NEW_ADD"
    assert my_list.tail.item == "NEW_APPEND"
    assert len(my_list) == 11
    assert [i for i in my_list] == [
        "NEW_ADD",
        "ADD_5",
        "ADD_4",
        "ADD_3",
        "ADD_2",
        1,
        2,
        3,
        4,
        5,
        "NEW_APPEND",
    ]
    assert my_list.index("NEW_APPEND") == len(my_list) - 1

    # REMOVE again!
    my_list.remove(5)
    # print(my_list, "Size: {}".format(len(my_list)))
    assert my_list.head.item == "NEW_ADD"
    assert my_list.tail.item == "NEW_APPEND"
    assert len(my_list) == 10
    assert [i for i in my_list] == [
        "NEW_ADD",
        "ADD_5",
        "ADD_4",
        "ADD_3",
        "ADD_2",
        1,
        2,
        3,
        4,
        "NEW_APPEND",
    ]
    assert my_list.index("NEW_APPEND") == len(my_list) - 1

    # POP again!
    res = my_list.pop(1)
    print(my_list, "Size: {}".format(len(my_list)))
    assert res == "ADD_5"
    assert my_list.head.item == "NEW_ADD"
    assert my_list.tail.item == "NEW_APPEND"
    assert len(my_list) == 9
    assert my_list.index("ADD_4") == 1
    assert [i for i in my_list] == [
        "NEW_ADD",
        "ADD_4",
        "ADD_3",
        "ADD_2",
        1,
        2,
        3,
        4,
        "NEW_APPEND",
    ]
    assert my_list.index("NEW_APPEND") == len(my_list) - 1

    # INSERT by NEGATIVE index!
    my_list.insert("NEGATIVE", -1)
    print(my_list, "Size: {}".format(len(my_list)))
    assert my_list.head.item == "NEGATIVE"
    assert my_list.tail.item == "NEW_APPEND"
    assert len(my_list) == 10
    assert [i for i in my_list] == [
        "NEGATIVE",
        "NEW_ADD",
        "ADD_4",
        "ADD_3",
        "ADD_2",
        1,
        2,
        3,
        4,
        "NEW_APPEND",
    ]
    assert my_list.index("NEW_APPEND") == len(my_list) - 1

    # Contains
    for i in (
        "NEGATIVE",
        "NEW_ADD",
        "ADD_4",
        "ADD_3",
        "ADD_2",
        1,
        2,
        3,
        4,
        "NEW_APPEND",
    ):
        assert i in my_list

    return my_list


def check_exceptions(my_list):
    print("\nCheck possible Exceptions:\n")

    try:
        LinkedList().pop()
    except IndexError:
        print("- IndexError on 'pop' from empty list is raised")

    try:
        my_list.pop(15)
    except IndexError:
        print("- IndexError on 'pop' by non-existing index is raised")

    try:
        my_list.remove("sdfsf3w590453045jjk")
    except ValueError:
        print("- ValueError upon 'remove' of non-existing field is raised")


linked_list = LinkedList()
linked_list = check_linked_list_methods(linked_list)
check_exceptions(linked_list)
