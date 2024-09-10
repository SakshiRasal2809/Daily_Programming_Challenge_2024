def Sort(arr):
    low = 0
    mid = 0 
    high = len(arr)-1
    
    while mid <= high :
        if arr[mid]== 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            mid+=1
            low+=1
            
        elif arr[mid]==1:
             mid+=1
            
        else:
            arr[mid], arr[high] = arr[high],arr[mid]
            high-=1
    return arr
            
arr=  [0, 1, 2, 1, 0, 2, 1, 0]
print('Sorted Array:',Sort(arr))

arr=  [2,2,2,2]
print('Sorted Array:',Sort(arr))

arr=  [0,0,0,0]
print('Sorted Array:',Sort(arr))

arr=  []
print('Sorted Array:',Sort(arr))
            