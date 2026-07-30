def bubble_sort(data_list):
    n = len(data_list)                
    for i in range(n):
        swapped= False
        for j in range(0, n-i-1):
            if data_list[j] > data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
                swapped= True
        if not swapped:
            break

    return data_list

def bubble_sort_reverse(data_list):
    n=len(data_list)
    for i in range(n):
        swapped= False
        for j in range(n -1, i,-1):
            if data_list[j] < data_list[j-1]:
                data_list[j], data_list[j-1] = data_list[j-1], data_list[j]
                swapped= True
        if not swapped:
            break
    return data_list


# TEST /
print("EJERCICIO 1: Bubble Sort Estandar")
numbers1 = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numbers1)
print("Resultado:     ", bubble_sort(numbers1))

print("EJERCICIO 2: Bubble Sort Invertido (Imagen)")
numbers2 = [9, 8, 7, 1, 6, 5, 4, 3, 2]
print("Lista original:", numbers2)
print("Resultado:     ", bubble_sort_reverse(numbers2))