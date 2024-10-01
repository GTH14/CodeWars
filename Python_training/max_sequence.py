## The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
##  max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
##  should be 6: [4, -1, 2, 1]
## Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is
## made up of only negative numbers, return 0 instead.
## Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

# Idea: it verify which is then it verifies if the sum of
import numpy as np

def max_sequence(arr):
    arr_np = np.array(arr)
    if len(arr_np) == 0 or len(arr_np)+np.sum(np.sign(arr_np)) == 0:
        return 0
    else:
        
        return 1

        
def main():
    # array_test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    neg_array = [-1,-2,-1,-5,-3,-4]
    res = max_sequence(neg_array)
    print(res)
main()