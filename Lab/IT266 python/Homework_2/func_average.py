def average(list_items):
    count = 0
    sum = 0
    average = 0 
    for item in list_items:
        sum += float(item)
        count += 1
    average = sum / count
    return average