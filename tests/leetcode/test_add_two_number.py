from solutions.common.dto import from_list, to_list
from solutions.leetcode.add_two_number import add_two_number

def test_add_two_number_example1():
    l1 = from_list([2, 4, 3])
    l2 = from_list([5, 6, 4])
    expected = from_list([7, 0, 8])
    actual = add_two_number(l1, l2)
    assert to_list(expected) == to_list(actual)

def test_add_two_number_example2():
    l1 = from_list([0])
    l2 = from_list([0])
    expected = from_list([0])
    actual = add_two_number(l1, l2)
    assert to_list(expected) == to_list(actual)

def test_add_two_number_example3():
    l1 = from_list([9, 9, 9, 9, 9, 9, 9])
    l2 = from_list([9, 9, 9, 9])
    expected = from_list([8, 9, 9, 9, 0, 0, 0, 1])
    actual = add_two_number(l1, l2)
    assert to_list(expected) == to_list(actual)
