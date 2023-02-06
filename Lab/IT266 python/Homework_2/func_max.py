def max(item_list):
    max = None
    for item in item_list:
        if max is None or float(item) > max:
            max = float(item)
    return max