def quickSort(array: list, left_index: int, right_index: int):
    if left_index > right_index:
        return

    pivot = array[right_index]
    greater_number_index = left_index - 1

    for i in range(left_index, right_index):
        if array[i] < pivot:
            greater_number_index += 1
            (array[i], array[greater_number_index]) = (array[greater_number_index], array[i])

    greater_number_index += 1
    (array[right_index], array[greater_number_index]) = (array[greater_number_index], array[right_index])  # swap pivot into a middle

    quickSort(array, left_index, greater_number_index-1)
    quickSort(array, greater_number_index+1, right_index)


if __name__ == "__main__":
    arr = [4, 7, -1, -0.2, 0, 2, 9, 3, 6, 345, 0, 3, 3, 7, 7, 3]
    quickSort(arr, 0, len(arr) - 1)
    print(arr)
