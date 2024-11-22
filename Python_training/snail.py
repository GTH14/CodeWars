# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
def snail(snail_map):
    len_n = len(snail_map)
    snail_res = []
    counter = 0
    counter_col = 0
    counter_row = 0
    col_min = row_min = 0
    col_max = row_max = len_n - 1
    dir = 0
    if len_n == 1 and len(snail_map[0]) == 0:
        return []
    else: 
        while counter < len_n**2:
            if counter != 0:
                if counter_row >= row_max and dir == 0:
                    dir = 1
                    col_min += 1
                elif counter_col >= col_max and dir == 1:
                    dir = 2
                    row_max -= 1
                elif counter_row <= row_min and dir == 2:
                    dir = 3
                    col_max -= 1
                elif counter_col <= col_min and dir == 3:
                    dir = 0
                    row_min += 1
            # print(counter_row)
            # print(counter_col)
            snail_res.append(snail_map[counter_col][counter_row])   
            if dir == 0:
                counter_row += 1
            elif dir == 1:
                counter_col += 1
            elif dir == 2:
                counter_row -= 1
            elif dir == 3:
                counter_col -= 1
                
            counter += 1
    return snail_res


def main():
    array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    print(snail(array))

main()