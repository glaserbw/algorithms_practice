arr = [1, 100, 50, -51, 1, 1]

def find_pivot(arr):
    for i in range(len(arr)):
        arrLeft = sum(arr[0:i])
        # print(arrLeft)
        arrRight = sum(arr[i:len(arr)])
        if arrRight == arrLeft:
            return i
            
    # return -1 


print(find_pivot(arr))
