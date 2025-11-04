def bubble_sort(lst):
    """Bubble sort. Takes list and sorts it."""
    size = len(lst)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(size - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                is_sorted = False
