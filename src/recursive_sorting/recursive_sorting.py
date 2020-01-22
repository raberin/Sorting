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

# def quick_sort(arr):

#     # STRETCH: implement an in-place merge sort algorithm


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
