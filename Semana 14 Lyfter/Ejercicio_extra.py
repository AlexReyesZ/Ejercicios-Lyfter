def bubble_sort_steps(data_list):
    n=len(data_list)
    interaction=0
    swaps=0

    for i in range(n):
        interaction+=1
        swapped= False

        for j in range(0, n-i-1):
            if data_list[j] > data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
                swaps += 1       
                swapped = True
        if not swapped:
            break   
    
    print("Lista ordenada:")
    print(data_list)
    print(f"Iteraciones: {interaction}")
    print(f"Intercambios: {swaps}")
    
    return data_list

my_test_list = [5, 1, 4, 2, 8]
bubble_sort_steps(my_test_list)

def validated_bubble_sort(data_list):
    if not data_list:
        return 'ERROR, the list is empty'
    
    for element in data_list:
        if isinstance(element, (int, float)) or not isinstance(element, (int, float)):
            return 'ERROR, the list contains non-numeric elements'
    return bubble_sort_steps(data_list)

#TESTS

print("--- PRUEBA 1: Lista Valida ---")
sample_list = [5, 1, 4, 2, 8]
validated_bubble_sort(sample_list)

print("\n--- PRUEBA 2: Elemento No Numerico ---")
invalid_list = [5, "hola", 2]
print(validated_bubble_sort(invalid_list))

print("\n--- PRUEBA 3: Lista Vacia ---")
empty_list = []
print(validated_bubble_sort(empty_list))

# Entrega Semana 14