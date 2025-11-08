def _heapify(lst, index):
    while index > 0:
        if lst[index] > lst[(index - 1) // 2]:
            lst[index], lst[(index - 1) // 2] = lst[(index - 1) // 2], lst[index]
        else:
            break
        index = (index - 1) // 2


def _list_to_heap(lst, unsorted_size):
    for i in range(unsorted_size):
        if lst[i] > lst[(i - 1) // 2]:
            _heapify(lst, i)


def heap_sort(unsorted_lst: list) -> list:
    """Heap sort. Takes list. Returns sorted list."""
    lst = unsorted_lst.copy()
    size = len(lst)
    for i in range(size):
        _list_to_heap(lst, size - i)
        lst[0], lst[size - i - 1] = lst[size - i - 1], lst[0]
    return lst
