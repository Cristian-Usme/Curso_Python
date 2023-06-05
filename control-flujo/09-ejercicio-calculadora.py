# verificar si ya existe un número, si no, ingrese un número, luego
# que el usuario ingrese una operación, luego le pedimos un nuevo
# número y efectuamos la operación solicitada, luego, el resultado
# lo almacenaremos como el primer número y pediremos una operación
# un nuevo número y así sucesivamente hasta que el usuario escriba
# salir.

print("""
Bienvenidos a la calculadora
Para salir escribe \"Salir\" 
Las operaciones son suma, multi, div y resta""")

n1 = input("Ingresa número: ")

while True:
    n1 = int(n1)
    operacion = input("Ingresa operación: ")
    if operacion == "suma":
        n2 = int(input("Ingrese siguiente número: "))
        n1 = n1 + n2
    elif operacion == "multi":
        n2 = int(input("Ingrese siguiente número: "))
        n1 = n1 * n2
    elif operacion == "div":
        n2 = int(input("Ingrese siguiente número: "))
        n1 = n1 / n2
    elif operacion == "resta":
        n2 = int(input("Ingrese siguiente número: "))
        n1 = n1 - n2
    elif operacion.lower() == "salir":
        break
    else:
        print("Operación no valida")
        break
    print(f"El resultado es {n1}")
