def bubble_sort(items: list[int]):
    length = len(items)
    for i in range(0, length):
        swapped = False
        for j in range(0, length - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True

                print(f"Sorted array is: {arr}")
        if not swapped:
            return items
    return items


arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array is: {arr}")

bubble_sort(arr)

print(f"Sorted array is: {arr}")
