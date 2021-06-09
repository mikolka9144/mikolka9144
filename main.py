def sort(elements: list):
    current_list = [[item]for item in elements]
    while len(current_list) != 1:
        current_list = split_group(current_list)
    return current_list[0]


def split_group(arrays: list):
    new_arrays = list()
    arrays_pointer = 0
    while len(arrays) != arrays_pointer:
        array_remaining = len(arrays) - arrays_pointer
        if array_remaining >= 2:
            new_arrays.append(split_arrays(arrays[arrays_pointer], arrays[arrays_pointer + 1]))
            arrays_pointer += 2
        elif array_remaining == 1:
            new_arrays.append(arrays[arrays_pointer])
            arrays_pointer += 1
    print(f'Verbose:{new_arrays}') #Verbose
    return new_arrays


def split_arrays(array1: list, array2: list):
    array3 = list()
    array1_pointer = 0
    array2_pointer = 0
    while len(array2) != array2_pointer or len(array1) != array1_pointer:
        if len(array1) == array1_pointer:
            array3.append(array2[array2_pointer])
            array2_pointer += 1
        elif len(array2) == array2_pointer:
            array3.append(array1[array1_pointer])
            array1_pointer += 1
        elif array1[array1_pointer] < array2[array2_pointer]:
            array3.append(array1[array1_pointer])
            array1_pointer += 1
        elif array1[array1_pointer] > array2[array2_pointer]:
            array3.append(array2[array2_pointer])
            array2_pointer += 1
    return array3


print(sort([2,5,15,23,1]))