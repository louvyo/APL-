def exchange_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)

# Sort the array using Exchange sort
sorted_arr = exchange_sort(arr)
print("Array yang sudah diurutkan:",sorted_arr)
