def bubble_sort(lst: list) -> list:
    """Bubble sort. Takes list. Returns sorted list."""
    sorted_lst = lst.copy()
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(len(sorted_lst) - 1):
            if sorted_lst[i] > sorted_lst[i + 1]:
                sorted_lst[i], sorted_lst[i + 1] = sorted_lst[i + 1], sorted_lst[i]
                is_sorted = False

    return sorted_lst
