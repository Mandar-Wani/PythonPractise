from Array_max_element import char_array

import array as arr
def duplicates_hasmap(array):
    frequency_element = {}
    result = []
    for num in array:
        frequency_element[num] = frequency_element.get(num, 0) + 1

    for key, value in frequency_element.items():
        if value > 1:
            result.append(key)

    if not result:
        result.append(-1)

    return result

ca = arr.array('u', ['a', 'b', 'c', 'd', 'a', 'e', 'b'])
print(duplicates_hasmap(ca))
