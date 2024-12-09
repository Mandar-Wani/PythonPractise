"""
target = a+b
a = target-b
"""

import array as arr

#the Naive approach
def sum_target(arr , target):
    list_nums = []
    i , j = 0, 0
    n = len(arr)
    if n <= 1:
        return "Array does not have atleast two elements to check target value against"
    else:
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] + arr[j] == target:
                    list_nums.append(arr[i])
                    list_nums.append(arr[j])
                    return list_nums
        else:
            return "No two numbers in the array sums to the target value"

integer_array = arr.array('i', [1 ,2, 3,6 ,4,5])
print(sum_target(integer_array, 4))


#the better approach
