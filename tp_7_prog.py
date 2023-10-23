#TP7 - Programación

#---------------FUNCIONES—------------

#EJERCICIO 1

def bubble_sort(numbers):   #Ordenamiento de burbuja
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


#EJERCICIO 2

def selection_sort(fruits):    #Orden de selección
    n = len(fruits)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if fruits[j] < fruits[min_idx]:
                min_idx = j
        fruits[i], fruits[min_idx] = fruits[min_idx], fruits[i]


#EJERCICIO 4

def insertion_sort(list):       #Tipo de inserción
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and len(key) < len(list[j]):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key


#EJERCICIO 5

def bubble_sort_desc(numbers):  #Ordenamiento de burbuja
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


#EJERCICIO 6

def counting_sort(numbers):
    max_value = max(numbers)
    min_value = min(numbers)
    range_of_values = max_value - min_value + 1

    count = [0] * range_of_values
    output = [0] * len(numbers)

    for num in numbers:
        count[num - min_value] += 1

    for i in range(1, range_of_values):
        count[i] += count[i - 1]

    for num in reversed(numbers):
        output[count[num - min_value] - 1] = num
        count[num - min_value] -= 1

    return output


#EJERCICIO 7

def number_string_items(item):
    if isinstance(item, int):
        return (0, item)  # Tupla con 0 para números
    elif isinstance(item, str):
        return (1, item)  # Tupla con 1 para cadenas de texto


#EJERCICIO 8

def merge_sort(numbers):    #Combinar ordenamiento
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left_half = numbers[:mid]
        right_half = numbers[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                numbers[k] = left_half[i]
                i += 1
            else:
                numbers[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            numbers[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            numbers[k] = right_half[j]
            j += 1
            k += 1

#---------------PROGRAMA—------------

#EJERCICIO 1

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original: ", numbers)
bubble_sort(numbers)
print("Ordenamiento de burbuja (Bubble Sort): ", numbers)


#EJERCICIO 2

fruits = ["ananá", "zanahoria", "manzana", "banana", "frutilla"]
print("Lista Original:", fruits)
selection_sort(fruits)
print("Orden de selección (Selection Sort):", fruits)


#EJERCICIO 3

ordered_list = []
book_list = [{"title":"El principito", "author":"Antoine de Saint-Exupéry", "year":1943}, {"title":"El mago de oz", "author":"L. Frank Baum", "year":1900}, {"title":"El Eternauta", "author":"Héctor Germán Oesterheld", "year":1957}, {"title":"Tokio Blues", "author":"Haruki Murakami", "year":1987}, {"title":"El sabueso de los Baskerville", "author":"Arthur Conan Doyle", "year":1902}]
ordered_list = sorted(book_list, key=lambda x: x['year'])
print(ordered_list)


#EJERCICIO 4

string_list = ["Hola a todos", "Cómo están el día de hoy", "Bien", "Mal", "Mas o menos"]
insertion_sort(string_list)
print(string_list)


#EJERCICIO 5

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original:", numbers)
bubble_sort_desc(numbers)
print("Ordenamiento de burbuja (Bubble Sort) ORDEN DESCENDENTE: ", numbers)


#EJERCICIO 6

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original: ", numbers)
ordered_list = counting_sort(numbers)
print("Ordenamiento por Conteo (Counting Sort):", ordered_list)


#EJERCICIO 7

list = [5, "manzana", 3, "banana", 1, "ananá", 2, "zanahoria", 4, "naranja"]
print("Lista desordenada: ", list)
sorted_list = sorted(list, key=number_string_items)
print("Lista ordenada:", sorted_list)


#EJERCICIO 8

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original:", numbers)
merge_sort(numbers)
print("Combinar ordenamiento (Merge Sort): ", numbers)


