def select_sort(arr: list[int]) -> list[int]:
    i = 0
    while i < len(arr) - 1:
        m = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[m]:
                m = j
            j += 1
        arr[i], arr[m] = arr[m], arr[i]
        i += 1
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array is: {arr}")
print(f"Sorted array is: {select_sort(arr)}")
