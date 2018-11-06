arr = [1, 100, 50, -51, 1, 1]

def find_pivot(arr):
    arrLeft = 0
    arrRight = 0
    for i in range(len(arr)):
        arrLeft = 0
        arrRight = 0
        for j in range(i):
            arrLeft += arr[j]
        for j in range(i+1, len(arr)):
            arrRight += arr[j]
        if arrRight == arrLeft:
            return i
    return -1  
    # return -1 
 
print(find_pivot(arr))

# def find_pivotnew(arr):
#     newArr = sum(arr)
#     print(newArr)
#     for i in range(len(arr)):
#         test = newArr - arr[i]
#         if test = 


# # find_pivotnew(arr)