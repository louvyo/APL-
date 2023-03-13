def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high and x >= arr[low] and x <= arr[high]:
        pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        if arr[pos] == x:
            return pos
        
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1

arr = [2,4,5,6,7,8,9,13,31]
print ("array:",arr)
x = int(input("Search Number: "))
result = interpolation_search(arr, x)

if result != -1:
    print(f"Elemen {x} ditemukan pada indeks {result}.")
else:
    print(f"Elemen {x} tidak ditemukan dalam array.")



