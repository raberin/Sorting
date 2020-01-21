# Complete Insertion Sort
def insertion_sort(arr):
    return arr


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # Find the smallest element in the arr
        for j in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # Swap Elements
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


arr = [6, 5, 8, 3, 2, 12, 9, 10]
print(selection_sort(arr))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            # Compare adjacent values, swap if necessary
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = [6, 5, 8, 3, 2, 12, 9, 10]
print(bubble_sort(arr))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
