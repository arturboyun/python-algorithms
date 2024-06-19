def merge_lists(arr1: list[int], arr2: list[int]) -> list[int]:
    merged_list = []
    i = j = 0

    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_list.append(arr1[i])
            i += 1
        else:
            merged_list.append(arr2[j])
            j += 1

    if i < len(arr1):
        merged_list.extend(arr1[i:])

    if j < len(arr2):
        merged_list.extend(arr2[j:])
    return merged_list


def merge_sort(items: list[int]) -> list[int]:
    if len(items) == 1:
        return items

    middle = len(items) // 2
    print(f"Items is: {items}")
    print(f"Middle is: {middle}")
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])
    return merge_lists(left, right)


arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array is: {arr}")
print(f"Sorted array is: {merge_sort(arr)}")
