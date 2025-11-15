# Implement binary search to find the position of a target value in a sorted array.

def binary_search(arr, target):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

arr = sorted(list(map(int, input().split())))
target = int(input("Target: "))

pos = binary_search(arr, target)
print("Found at index", pos if pos != -1 else "Not Found")
