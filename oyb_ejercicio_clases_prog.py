# Función para ordenar una lista usando Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Función para ordenar una lista usando Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Función para ordenar una lista usando Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Función para ordenar una lista usando Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Función para realizar una búsqueda lineal en una lista
def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

# Función para realizar una búsqueda binaria en una lista ordenada
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def sort_and_search(arr, target):
    # Bubble Sort
    bubble_sorted = arr.copy()
    bubble_sort(bubble_sorted)

    # Selection Sort
    selection_sorted = arr.copy()
    selection_sort(selection_sorted)

    # Insertion Sort
    insertion_sorted = arr.copy()
    insertion_sort(insertion_sorted)

    # Merge Sort
    merge_sorted = arr.copy()
    merge_sort(merge_sorted)

    # Búsqueda Lineal
    linear_result = linear_search(arr, target)

    # Búsqueda Binaria (requiere que la lista esté ordenada)
    binary_result = binary_search(merge_sorted, target)

    print("Lista Original:", arr)
    print("Bubble Sort:", bubble_sorted)
    print("Selection Sort:", selection_sorted)
    print("Insertion Sort:", insertion_sorted)
    print("Merge Sort:", merge_sorted)
    print(f"Búsqueda Lineal: {'Elemento encontrado en la posición ' + str(linear_result) if linear_result != -1 else 'Elemento no encontrado'}")
    print(f"Búsqueda Binaria: {'Elemento encontrado en la posición ' + str(binary_result) if binary_result != -1 else 'Elemento no encontrado'}")

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
target = 22
sort_and_search(arr, target)
