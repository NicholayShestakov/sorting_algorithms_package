from random import randint

from sorting_algorithms.heap_sort import heap_sort


def test_easy():
    lst = [3, 1, 2]
    assert heap_sort(lst) == [1, 2, 3]


def test_empty():
    lst = []
    assert heap_sort(lst) == []


def test_random():
    lst = [randint(-1000, 1000) for _ in range(randint(1, 1000))]
    assert heap_sort(lst) == sorted(lst)
