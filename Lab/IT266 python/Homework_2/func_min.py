def min(item_list):
    min = None
    for item in item_list:
        if min is None or float(item) < min:
            min = float(item)
    return min
