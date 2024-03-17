def selectionSort(array: list):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]


if __name__ == "__main__":
    arr = [4, 7, -1, -0.2, 0, 2, 9, 3, 6, 345, 0, 3, 3, 7, 7, 3]
    selectionSort(arr)
    print(arr)
