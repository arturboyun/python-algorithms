def list_merge(arr1: list[int], arr2: list[int]) -> list[int]:
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


arr1 = [1, 1]
arr2 = [2, 3, 4, 3, 6]

print(f"Original arrays are:\n{arr1}\n{arr2}")
print(f"Merged array is: {list_merge(arr1, arr2)}")
