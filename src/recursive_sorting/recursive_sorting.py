# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # TO-DO
    merged_arr = []
    arrA_index, arrB_index = 0, 0

    # use While loop to go through both arrays until one is empty
    while arrA_index < len(arrA) and arrB_index < len(arrB):
        if arrA[arrA_index] < arrB[arrB_index]:
            merged_arr.append(arrA[arrA_index])
            arrA_index += 1
        else:
            merged_arr.append(arrB[arrB_index])
            arrB_index += 1

    if arrA_index == len(arrA):
        merged_arr.extend(arrB[arrB_index:])
    else:
         merged_arr.extend(arrA[arrA_index:])

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    #start with the base case, means there is only 1 or no elements in the array
    if len(arr) <= 1:
        return arr
    else:
    #split the array down the middle
        split_array = len(arr) // 2
        left_array = merge_sort(arr[:split_array])
        right_array = merge_sort(arr[split_array:])

    return merge(left_array, right_array)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DOO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
