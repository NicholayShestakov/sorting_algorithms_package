def quick_sort(lst: list) -> list:
    """Quick sort. Takes list. Returns sorted list."""
    if len(lst) in (0, 1):
        return lst

    middle_index = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[0]:
            middle_index += 1
            lst[middle_index], lst[i] = lst[i], lst[middle_index]
    lst[middle_index], lst[0] = lst[0], lst[middle_index]

    return (
        quick_sort(lst[:middle_index])
        + [lst[middle_index]]
        + quick_sort(lst[middle_index + 1 :])
    )
