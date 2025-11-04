from random import randint

from sorting_algorithms.bubble_sort import bubble_sort


def test_easy():
    lst = [3, 1, 2]
    bubble_sort(lst)
    assert lst == [1, 2, 3]


def test_empty():
    lst = []
    bubble_sort(lst)
    assert lst == []


def test_random():
    lst = [randint(-1000, 1000) for _ in range(randint(1, 1000))]
    lst_copy = lst.copy()
    bubble_sort(lst)
    assert lst == sorted(lst_copy)
