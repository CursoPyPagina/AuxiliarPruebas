# Imprimir todos los números anteriores a un número dado
# Si el número es negativo o nulo no imprimir nada

def antescesores(n):
    if n > 0:
        print(n)
        return antescesores(n-1)
    else:
        print("Error")

antescesores(5)
print("-" * 20)
antescesores(0)