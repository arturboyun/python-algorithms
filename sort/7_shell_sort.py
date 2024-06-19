def shell_sort(arr: list[int]) -> list[int]:
    gap = len(arr) // 2
    while gap > 0:
        for value in range(gap, len(arr)):
            current_value = arr[value]
            position = value
            
            while position >= gap and arr[position - gap] > current_value:
                arr[position] = arr[position - gap]
                position -= gap

            arr[position] = current_value
        gap //= 2
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array is: {arr}")
print(f"Sorted array is: {shell_sort(arr)}")
