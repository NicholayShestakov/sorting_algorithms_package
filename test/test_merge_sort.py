from random import randint

from sorting_algorithms.merge_sort import merge_sort


def test_easy():
    lst = [3, 1, 2]
    assert merge_sort(lst) == [1, 2, 3]


def test_empty():
    lst = []
    assert merge_sort(lst) == []


def test_random():
    lst = [randint(-1000, 1000) for _ in range(randint(1, 1000))]
    assert merge_sort(lst) == sorted(lst)
