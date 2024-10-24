def marge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left_arr = marge_sort(array[:mid])
    right_arr = marge_sort(array[mid:])
    
    return marge(left_arr, right_arr)


def marge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])