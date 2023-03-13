import random

# Exchange sort function
def exchange_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# Interpolation search function
def interpolation_search(arr, x):
    n = len(arr)
    lo = 0
    hi = n - 1
    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        pos = lo + ((x - arr[lo]) * (hi - lo)) // (arr[hi] - arr[lo])
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1

# Generate a random array of integers
arr = [random.randint(1, 100) for i in range(10)]
print("Random array:", arr)

# Sort the array using Exchange sort
sorted_arr = exchange_sort(arr)
print("Sorted array:", sorted_arr)

# Search for a random number in the array using Interpolation search
search_num = int(input("Search Number: "))
print("Searching for number:", search_num)
result = interpolation_search(sorted_arr, search_num)
if result == -1:
    print("Number not found.")
else:
    print("Number found at index:", result)
