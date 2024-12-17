def quick_sort(arr):
    if len(arr)<=1:
        return arr
    p = arr[0]

    def safe_compare(a, b):
        try:
            # Try direct comparison first
            return a < b
        except TypeError:
            # Fallback to string comparison if direct comparison fails
            return str(a) < str(b)
    left = [x for x in arr[1:] if safe_compare(x, p)]
    right = [x for x in arr[1:] if not safe_compare(x, p)]
    print(left)
    print(right)
    print(arr[:-1])
    print(arr[1:])
    #return quick_sort(left) + [p] + quick_sort(right)

array = [1, 4, 8, 2, 4, 8, 0]
qs = quick_sort(array)
print(qs)

