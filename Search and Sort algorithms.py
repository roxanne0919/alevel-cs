def linear_search(list, item):
    for i in range(len(list)):
        if list[i] == item:
            print(f"{item} found in index {i}")
            return i
    return -1
    

def binary_search(list, item):
    length = len(list)
    upper = length - 1
    lower = 0
    while lower <= upper:
        mid = (upper + lower) // 2
        if list[mid] == item:
            print(f"{item} found in index {mid}")
            return mid
        elif item > list[mid]:
            lower = mid + 1
        elif item < list[mid]:
            higher = mid - 1
    return -1


def bubble_sort(list):
    length = len(list)
    upper = length
    lower = 0
    for i in range(length):
        swap = False
        for j in range(lower, upper - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j] 
                swap = True
        upper -= 1
        if swap == False:
            break
    return list 
            
        
def insertion_sort(list):
    length = len(list)
    for i in range(1, length):
        key = list[i]
        index = i

        while index > 0 and key < list[index - 1]:
            list[index] = list[index-1]
            index -= 1
        list[index] = key
    return list

            
