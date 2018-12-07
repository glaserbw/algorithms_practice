def is_ascending(items):
    ascending = descending = True
    for i in range(len(items) - 1): 
        if items[i] > items[i+1] :
            ascending = False
        elif items[i] < items[i+1] :
            descending = False
    return ascending or descending


items = [2, 3, 3, 2, 1]


# [4, 5, 6, 7, 3, 7, 9]c.ea

# def is_ascending(items):
#     all(items[i] <= items[i+1] for i in range(len(items)-1))


print(is_ascending(items))