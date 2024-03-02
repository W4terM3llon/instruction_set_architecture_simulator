def mergeSort(array: list) -> list:
    if len(array) <= 1:
        return array

    mid = int(len(array) / 2)
    leftArray = mergeSort(array[0:mid:])
    rightArray = mergeSort(array[mid::])

    sortedArray = []

    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(leftArray) and rightIndex < len(rightArray):
        if leftArray[leftIndex] <= rightArray[rightIndex]:
            sortedArray.append(leftArray[leftIndex])
            leftIndex += 1
        else:
            sortedArray.append(rightArray[rightIndex])
            rightIndex += 1

    # add remaining left array elements if any
    while leftIndex < len(leftArray):
        sortedArray.append(leftArray[leftIndex])
        leftIndex += 1

    # add remaining right array elements if any
    while rightIndex < len(rightArray):
        sortedArray.append(rightArray[rightIndex])
        rightIndex += 1

    return sortedArray


if __name__ == "__main__":
    print(mergeSort([4, 7, -1, -0.2, 0, 2, 9, 3, 6, 345, 0, 3, 3, 7, 7, 3]))
