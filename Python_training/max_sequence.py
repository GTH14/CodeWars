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
    len_arr = len(arr)
    if len_arr == 0 or len_arr+np.sum(np.sign(arr_np)) == 0:
        return 0
    elif len_arr-np.sum(np.sign(arr_np)) == 0:
        return sum(arr)
    else:
        sign_arr = np.sign(arr_np)
        pos_index = []
        pos_island = np.array([])
        arr_island = np.array([])
        for index in range(len_arr):
            if sign_arr[index] > 0:                        
                if np.any(pos_index):
                    if index - pos_index[-1] -1 == 0:
                        pos_island[-1] += arr[index]
                        arr_island[-1] += arr[index]
                    else:
                        np.append(pos_island, arr[index])
                else: 
                    np.append(pos_island, arr[index])
                pos_index.append(index)
                np.append(arr_island, arr[index])
        

def main():
    array_test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sequence(array_test))
    np.random.seed(1)
    for length_var in range(10,20):
        seq = np.random.randint(low=-20, high=20, size=length_var)
        print(seq)
        print(max_sequence(seq))
    for length_var in range(20,50):
        seq = np.random.randint(low=-40, high=40, size=length_var)
        print(seq)
        print(max_sequence(seq.tolist()))
main()