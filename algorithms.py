from random import randint


# variant of selection sort
def selection_sort(lst: list) -> list:
    for i in range(len(lst) - 1):

        m = i

        for j in range(i + 1, len(lst)):

            if lst[j] < lst[m]:
                m = j

        lst[i], lst[m] = lst[m], lst[i]

    return lst


# variant of insertion sort
def insertion_sort(lst: list) -> list:
    for i in range(1, len(lst)):

        item_to_insert = lst[i]
        j = i - 1

        while j >= 0 and lst[j] > item_to_insert:

            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = item_to_insert

    return lst


# variant of bubble sort

def bubble_sort(lst: list) -> list:
    for i in range(len(lst)):

        for j in range(i + 1, len(lst)):

            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst


# variant of merge sort
def merge_sort(lst: list) -> list:

    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

        return lst


# variant of quick sort
def quick_sort(lst: list) -> list:
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[randint(0, len(lst) - 1)]
        less = [i for i in lst if i < pivot]
        great = [j for j in lst if j > pivot]

        return quick_sort(less) + [pivot] + quick_sort(great)


# variant of heap sort
def heapify(lst: list, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lst[i] < lst[left]:
        largest = left

    if right < n and lst[largest] < lst[right]:
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]

        heapify(lst, n, largest)


def heap_sort(lst: list) -> list:
    n = len(lst)

    for i in range(n, -1, -1):
        heapify(lst, n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)

    return lst


def binary_search(array: list, value: int) -> int:
    l = 0
    r = len(array) - 1

    while l <= r:
        mid = (l + r) // 2

        if array[mid] == value:
            return mid

        elif value < array[mid]:
            r = mid - 1

        else:
            l = mid + 1


def recursive_binary_search(array: list, value: int, left=0, right=None) -> int:
    if right is None:
        right = len(array) + 1

    mid = (left + right) // 2
    if array[mid] == value:
        return mid

    elif value < array[mid]:
        return recursive_binary_search(array, value, left, mid - 1)

    else:
        return recursive_binary_search(array, value, mid + 1, right)
