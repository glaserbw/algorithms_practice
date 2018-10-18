arr = [6, 2, 4, 5, 7]
target = 7

def closest_target(arr, target):
  results = []
  closest = max(arr)*3
  for i in range(0, len(arr)-2):
    for j in range(i+1, len(arr)-1):
      for x in range(i+2, len(arr)):
        add = arr[i]+arr[j]+arr[x]
        compare = add - target
        if compare < closest:
          closest = compare 
          results = [arr[i],arr[j],arr[x]]
  return results
  
print(closest_target(arr, target))