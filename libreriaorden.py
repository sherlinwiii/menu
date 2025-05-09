
from mezclaequilibrada import mezcla_equilibrada
from mezcladirecta import mezcla_directa
from intercalar import intercalar_varias_listas
from shellshort import shell_sort
from radix import radix_sort
from heapsort import heapsort
from Quicksort import quicksort

def mostrar_menu():
    print("\n--- MENÚ DE ORDENAMIENTOS ---")
    print("1. Mezcla Equilibrada")
    print("2. Mezcla Directa")
    print("3. Intercalar Listas Ordenadas")
    print("4. Shell Sort")
    print("5. Radix Sort")
    print("6. Heap Sort")
    print("7. Quick Sort")
    print("8. Salir")

def pedir_lista():
    entrada = input("Ingrese los números separados por espacio: ")
    return list(map(float, entrada.strip().split()))

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            datos = pedir_lista()
            print("Ordenado:", mezcla_equilibrada(datos))
        elif opcion == '2':
            datos = pedir_lista()
            print("Ordenado:", mezcla_directa(datos))
        elif opcion == '3':
            n = int(input("¿Cuántas listas desea intercalar?: "))
            listas = []
            for i in range(n):
                entrada = input(f"Lista #{i+1}: ")
                lista = list(map(float, entrada.strip().split()))
                listas.append(lista)
            print("Intercalado:", intercalar_varias_listas(listas))
        elif opcion == '4':
            datos = pedir_lista()
            print("Ordenado:", shell_sort(datos))
        elif opcion == '5':
            datos = pedir_lista()
            try:
                print("Ordenado:", radix_sort(datos))
            except ValueError as e:
                print("Error:", e)
        elif opcion == '6':
            datos = pedir_lista()
            print("Ordenado:", heapsort(datos))
        elif opcion == '7':
            datos = pedir_lista()
            print("Ordenado:", quicksort(datos))
        elif opcion == '8':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
