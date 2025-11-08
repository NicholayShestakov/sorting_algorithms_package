def _merge(lst_1, lst_2):
    merged = []

    while lst_1 != [] and lst_2 != []:
        if lst_1[0] < lst_2[0]:
            merged.append(lst_1.pop(0))
        else:
            merged.append(lst_2.pop(0))

    if lst_1 != []:
        merged.extend(lst_1)
    if lst_2 != []:
        merged.extend(lst_2)

    return merged


def merge_sort(lst: list) -> list:
    """Merge sort. Takes list. Returns sorted list."""
    length = len(lst)
    if length in (0, 1):
        return lst

    left_half = merge_sort(lst[: length // 2])
    right_half = merge_sort(lst[length // 2 :])

    return _merge(left_half, right_half)
