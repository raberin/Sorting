# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    arrA_index = 0
    arrB_index = 0
    # Until the merged_arr is as big as both arrays combined
    while len(merged_arr) < len(arrA) + len(arrB):
        print(
            f"arrA_index = {arrA_index}, arrB_index = {arrB_index}\n {merged_arr}")
        # If arrB is empty add arrA elements and vice versa
        if len(arrB) <= arrB_index:
            merged_arr.append(arrA[arrA_index])
            arrA_index += 1
        elif len(arrA) <= arrA_index:
            merged_arr.append(arrB[arrB_index])
            arrB_index += 1
        # Compare which element is smaller and push to merged
        elif arrA[arrA_index] <= arrB[arrB_index]:
            merged_arr.append(arrA[arrA_index])
            arrA_index += 1
        else:
            merged_arr.append(arrB[arrB_index])
            arrB_index += 1
    return merged_arr


# arr1 = [1, 3, 5, 6, 7]
# arr2 = [2, 4, 8, 9]
# print(merge(arr1, arr2))


# # TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Base Case
    if len(arr) < 2:
        return arr
    # Make midpt variable
    middlePoint = len(arr) // 2
    # Recurse the left and right sides of the array
    sortLeft = merge_sort(arr[0:middlePoint])
    sortRight = merge_sort(arr[middlePoint:len(arr)])
    # Merge the arrays
    return merge(sortLeft, sortRight)


arr1 = [1, 3, 5, 6, 7, 2, 4, 8, 9]

print(merge_sort(arr1))


def quick_sort(arr):
    # Base case
    if len(arr) == 0:
        return arr
    # Set pivot point last number in arr
    pivot = arr[len(arr) - 1]
    # Create left and right arrays
    left_arr = []
    right_arr = []
    # Loop until right before last element
    for i in range(len(arr) - 1):
       # if pivot < arr[i] push to rightArr
        if pivot < arr[i]:
            right_arr.append(arr[i])
        # if pivot > arr[i] push to leftArr
        else:
            left_arr.append(arr[i])
    # recurse left + right
    left_arr_sorted = quick_sort(left_arr)
    right_arr_sorted = quick_sort(right_arr)
    print(
        f"left_arr_sorted {left_arr_sorted} + right_arr_sorted {right_arr_sorted}")
    # return left + pivot + right
    return left_arr_sorted + [pivot] + right_arr_sorted


arr1 = [1, 3, 5, 6, 7, 2, 4, 8, 9]

print(quick_sort(arr1))


# STRETCH: implement an in-place merge sort algorithm


# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr


# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):

#     return arr
