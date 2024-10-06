def a(arr):
    big = arr[len(arr) - 1]
    for i in arr:
        if big > arr[i]:
            return big
        elif big < arr[i]:
            big = arr[i]
    return big
print(a([3, 6, 1, 77, 44, 75, 99, 4]))


def b(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 1
    else:
        return 1 + b(arr[1:])
print(b([3, 6, 1, 77, 44, 75, 99, 4]))


def binary_search(arr, target):
    if len(arr) == 0:
        return None

    mid = len(arr) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        recursive_response = binary_search(arr[(mid + 1) :], target)
        return (
            (mid + 1) + recursive_response
            if recursive_response is not None
            else recursive_response
        )


print(binary_search([6, 7, 8, 9, 10], 8))
print(binary_search([6, 7, 8, 9, 10], 6))



#def quicksort(arr):
 #   pivot = arr[0]
 #   less = [i for i in arr[1:] if i <= pivot]
  #  bbb = [i for i in arr[1:] if i > pivot]
#
 #   return quicksort(less) + [pivot] + quicksort(bbb)
#
#print(quicksort([11, 33, 44, 66, 33, 2, 5, 2, 8]))



def double_array_elements(array):
    res = []
    for elem in array:
        res.append( elem * 2)
    return res
    
array = [2, 3, 4, 55]
print(double_array_elements(array))




def double_only_first_el(arr):
    #ress = []
    arr[0] *= 2
    return arr

arr = [4, 55]
print(double_only_first_el(arr))


def table_mm(ar):
    for elem in ar:
        print(f"Тфблиця множення на {elem}")
        for num in range(1, 11):
            print(f"{elem} * {num} = {elem * num}")

ar = [2, 3, 4, 8]
print(table_mm(ar))