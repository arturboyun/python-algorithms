def insert_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            print(f"i: {i}, j: {j}")
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array is: {arr}")
print(f"Sorted array is: {insert_sort(arr)}")
