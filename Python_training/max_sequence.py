## The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
##  max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
##  should be 6: [4, -1, 2, 1]
## Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is
## made up of only negative numbers, return 0 instead.
## Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

# Idea: it searches first for the minimum sum subarray going from the left to the right
import numpy as np
import time
def max_sequence(arr):
    arr_np = np.array(arr)
    len_arr = len(arr)
    if len_arr == 0 or len_arr+np.sum(np.sign(arr_np)) == 0:
        return 0
    elif len_arr-np.sum(np.sign(arr_np)) == 0:
        return sum(arr)
    else:
        sign_arr = 1*(arr_np>=0)
        arr_island = []
        
        for index in range(len_arr):
            if not(sum(arr_island)) and sign_arr[index]>0:
                arr_island.append(arr[index])
            elif sum(sign_arr[index::]) == 0:
                break
            elif sum(arr_island):
                if sign_arr[index] == sign_arr[index-1]:
                    arr_island[-1] += arr[index]
                else:
                    arr_island.append(arr[index]) 
        max_value = arr_island[0]
        max_index = 0
        if len(arr_island)>2:
            for index in range(1,len(arr_island), 2):
                inter_sum = sum(arr_island[max_index+1:index+1])
                if max_value > -inter_sum and arr_island[index+1] > -inter_sum :
                    max_value = max_value + inter_sum  + arr_island[index+1]
                elif max_value < -arr_island[index] and arr_island[index+1] > max_value:
                    max_value = arr_island[index+1]
                    max_index = index+1
        return max_value
                

def main():
    t_init = time.time_ns()
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
        print(max_sequence(seq))
    t_fin = time.time_ns()
    print(t_fin - t_init)
main()