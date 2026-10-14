def bubble_sort(data_list):
    # Type validation to raise TypeError for non-list inputs
    if not isinstance(data_list, list):
        raise TypeError("Input parameter must be a list")

    n = len(data_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
                swapped = True
        if not swapped:
            break

    return data_list