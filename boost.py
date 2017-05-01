import os, sys
import numpy as np

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                           #
#   Python module for counting inversions in an array.      #
#   Created by Nilesh PS                                    #
#   Created On 18-04-2017                                   #
#                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #   


def __merge(arr, left, mid, right):
    # Create an auxiliary array of same size.
    aux = np.zeros((right - left + 1, ), dtype=np.int64)
    # Initialise inversion count and other pointers.
    ic, k = 0, 0
    i, j = left, mid + 1
    # Following procedure is very similar to the merge procedure from merge sort. 
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
        	aux[k] = arr[i]
        	k += 1
        	i += 1
        else:
            ic += mid - i + 1
            aux[k] = arr[j]
            k += 1
            j += 1

    while i <= mid:
    	aux[k] = arr[i]
    	k += 1
    	i += 1

    while j <= right:
    	aux[k] = arr[j]
    	k += 1
    	j += 1
    # Copy auxiliary array to original array
    for i in range(0, right - left + 1):
        arr[i + left] = aux[i]
    # Return no of inversions found.
    return ic

def __inversion_count_impl(arr, left, right):
    if left >= right:
        return 0

    ic, mid = 0, int((left + right)/2)
    ic += __inversion_count_impl(arr, left, mid)
    ic += __inversion_count_impl(arr, mid + 1, right)
    ic += __merge(arr, left, mid, right);
    return ic

def inversion_count_optimized(arr, n = None):
    if n is None:
        n = arr.size if id(arr) == id(np.array) else len(arr)
    return __inversion_count_impl(arr, 0, n - 1)


def inversion_count_native(arr, n = None):
    if n is None:
        n = arr.size if id(arr) == id(np.array) else len(arr)
    ic = 0
    for i in range(0, n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                ic += 1

    return ic
