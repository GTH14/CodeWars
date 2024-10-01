## The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
##  max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
##  should be 6: [4, -1, 2, 1]
## Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is
## made up of only negative numbers, return 0 instead.
## Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

# Idea: it searches first for the minimum sum subarray going from the left to the right
import numpy as np

def max_sequence(arr):
    arr_np = np.array(arr)
    if len(arr_np) == 0 or len(arr_np)+np.sum(np.sign(arr_np)) == 0:
        return 0
    elif len(arr_np)-np.sum(np.sign(arr_np)) == 0:
        return sum(arr)
    else:
        min_sum_left, min_index_left = min_sequence(arr)
        new_arr = arr[min_index_left:len(arr)]
        min_sum_right, min_index_right = min_sequence(new_arr[::-1])
        min_index_right = len(arr) - min_index_right

        min_sum_right1, min_index_right1 = min_sequence(arr[::-1])
        min_index_right1 = len(arr) - min_index_right1
        new_arr1 = arr[0:min_index_right1]
        min_sum_left1, min_index_left1 = min_sequence(new_arr1)
        
        if min_sum_left+min_sum_right < min_sum_left1+min_sum_right1:
            return sum(arr) - min_sum_left - min_sum_right
        else:
            return sum(arr) - min_sum_left1 - min_sum_right1

def min_sequence(arr):
    min_sum = 0
    min_index = 0
    current_sum = 0
    for index in range(len(arr)):
        current_sum += arr[index]
        if current_sum < min_sum:
            min_sum = current_sum
            min_index = index+1
    return min_sum, min_index

def main():
    array_test = [-1,1,-5, 2, -1]
    neg_array = [-1,-2,-1,-5,-3,-4]
    res = max_sequence(neg_array)
    print(max_sequence(neg_array))
    pos_array = [1,2,1,5,3,4]
    print(max_sequence(pos_array))
    print(sum(array_test))
    print(max_sequence(array_test))
main()