import array as arr

def sum_target(arr, target):
    list_num = []
    sorted_list = sorted(arr)
    left , right = 0, len(sorted_list) - 1
    while left < right:
        sum = sorted_list[left] + sorted_list[right]
        if sum == target:
            list_num.append(sorted_list[left])
            list_num.append(sorted_list[right])
            break
        elif sum < target:
            left += 1
        else:
            right -= 1
    if not list_num:
        return "No integers found whose sum equal the target value"
    else:
        return list_num

integer_array1 = arr.array('i', [1, 2, 3, 4, 17 ,5])
print(sum_target(integer_array1, 7))
print(sum_target(integer_array1, 21))
print(sum_target(integer_array1, 3))




def sum_target(arr, target):
    sorted_list = sorted(arr)
    list_int = []
    left, right = 0, len(sorted_list) - 1
    while left< right:
        sum = sorted_list[left] + sorted_list[right]
        if sum  == target:
            list_int.append(sorted_list[left])
            list_int.append(sorted_list[right])
            break
        elif sum < target:
            left += 1
        else:
            right -= 1
    if not list_int:
        return "No two elements in the arr sum to target value"
    else:
        return list_int
integer_array2 = arr.array('i', [1, 2, 3, 4, 17 ,5])
print(sum_target(integer_array2, 7))
print(sum_target(integer_array2, 21))
print(sum_target(integer_array2, 3))




























