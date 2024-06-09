import pytest
from algorithms.Linked_list import LinkedList

@pytest.mark.parametrize(
    "list1, list2, expected",  # arguments names
    [
        ([], [], True),
        ([1, 2, 3], [1, 2, 3], True),
        ([], [1, 2, 3], False),
        ([1, 2, 3], [], False),
        ([1, 2, 3], [1, 2, 3, 4], False),
        ([1, 2, 3, 4], [1, 2, 3], False),
        ([3, 2, 1, 4], [1, 2, 3, 4], False)

    ]   # tests values
)



def test_eq_linked_list(list1:list, list2:list, expected:bool):

    assert (LinkedList.from_iterable(list1) == LinkedList.from_iterable(list2)) is expected
@pytest.mark.skip
def test_eq_type_linked_list():
    with pytest.raises(TypeError) as exc_info:
        LinkedList.from_iterable([1, 2, 3]) == [1, 2, 3]

    assert True
