# # STRETCH: implement Linear Search
def linear_search(arr, target):
    # TO-DO: add missing code
    for i in range(len(arr)):
        if(arr[i] == target):
            return i
    return -1


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Setting low and high indices to modify depending on midpoint
    lowIndex = 0
    highIndex = len(arr)-1

    while lowIndex < highIndex:
        # Set middleIndex // syntax estimates to nearest number
        middleIndex = (lowIndex + highIndex) // 2
        print(
            f"middleIndex = {middleIndex}, arr[middleIndex] = {arr[middleIndex]}")
        if target == arr[middleIndex]:
            return middleIndex
        else:
            if target < arr[middleIndex]:
                highIndex = middleIndex
            else:
                lowIndex = middleIndex
    return -1


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr1, -8))

# # STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, lowIndex, highIndex):
    # Base Case
    if len(arr) == 0:
        return -1

    middleIndex = (lowIndex + highIndex) // 2

    if arr[middleIndex] == target:
        return middleIndex
    else:
        if arr[middleIndex] < target:
            return binary_search_recursive(arr, target, middleIndex, highIndex)
        else:
            return binary_search_recursive(arr, target, lowIndex, middleIndex)


myArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search_recursive(myArr, 7, 0, len(myArr)))
