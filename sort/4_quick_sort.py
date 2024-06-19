def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array is: {arr}")
print(f"Sorted array is: {quick_sort(arr)}")
