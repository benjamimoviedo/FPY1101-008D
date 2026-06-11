inventario = [
    {
        "codigo": "L001",
        "titulo": "Python Básico",
        "autor": "Juan Pérez",
        "cantidad": 10,
        "precio": 19990
    },
    {
        "codigo": "L002",
        "titulo": "Cien Años de Soledad",
        "autor": "Gabriel García Márquez",
        "cantidad": 15,
        "precio": 24500
    },
    {
        "codigo": "L003",
        "titulo": "El Principito",
        "autor": "Antoine de Saint-Exupéry",
        "cantidad": 20,
        "precio": 12000
    },
    {
        "codigo": "L004",
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "cantidad": 8,
        "precio": 28990
    },
    {
        "codigo": "L005",
        "titulo": "Introducción a Data Science",
        "autor": "Ana Martínez",
        "cantidad": 12,
        "precio": 35000
    },
    {
        "codigo": "L006",
        "titulo": "1984",
        "autor": "George Orwell",
        "cantidad": 18,
        "precio": 15990
    },
    {
        "codigo": "L007",
        "titulo": "El Psicoanalista",
        "autor": "John Katzenbach",
        "cantidad": 7,
        "precio": 18500
    },
    {
        "codigo": "L008",
        "titulo": "Clean Code",
        "autor": "Robert C. Martin",
        "cantidad": 5,
        "precio": 42000
    },
    {
        "codigo": "L009",
        "titulo": "Crónica de una Muerte Anunciada",
        "autor": "Gabriel García Márquez",
        "cantidad": 14,
        "precio": 14990
    },
    {
        "codigo": "L010",
        "titulo": "Aprende SQL en un Fin de Semana",
        "autor": "Antonio Rivero",
        "cantidad": 22,
        "precio": 17500
    }
]

#Funciones

def registra_libro():
    """
    Esta funcion regisra un nuevo libro en una lista de diccionarios ya existente.
    Para ello, pide primero el codigo, valida si este no existe y luego pide los demas 
    datos para poder ingresarlos en forma de diccionario a la lista de diccionarios 
    llamada "inventario".

    Para comodiad del usuario, se usaron try-excepts y whiles con bandera para 
    que, en caso de error de tipeo y/o codigo, la ejecucion no se detenga y 
    se termine ingresando el libro correctamente sin repetir continuamente 
    datos correctos.
    """

    codigo_nuevo = input("Ingrese el codigo del libro a registrar: ")
    for libro in inventario:
            if libro["codigo"] == codigo_nuevo:
                print("El codigo ya existe, intente nuevamente.")
                break
    
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")

    error_cant = True
    error_precio = True

    #Whiles para que los parametros precio y cantidad sean ingresadon en formato int
    while error_cant == True:
        try:
            cantidad = int(input("Ingrese la cantidad disponible del libro: "))
            error_cant = False
        except ValueError:
            print("Error, Favor de ingresar un dato valido.")

    while error_precio == True:
        try:
            precio = float(input("Ingrese el precio del libro: "))
            error_precio = False
        except ValueError:
            print("Error, Favor de ingresar un dato valido.")
    
    #Ingreso de datos del nuevo libro para agregarlo al inventario
    libro_nuevo = {
            "codigo": codigo_nuevo,
            "titulo": titulo,
            "autor" : autor,
            "cantidad": cantidad,
            "precio": precio
        }

    inventario.append(libro_nuevo)
    print("Libro ingresado con exito")
    return 

def buscar_libro():

    codigo = input("Ingrese el codigo del libro a registrar: ")
    for libro in inventario:
        print("-LIBRO ENCONTRADO-")
        print(f"Codigo: {libro[codigo]}")
        print(f"Titulo: {libro["titulo"]}")
        print(f"Autor: {libro["autor"]}")
        print(f"Cantidad disponible: {libro["cantidad"]}")
        print(f"Precio: {libro["precio"]}")
        return
    return "Libro no encontrado"
def actualizar_stock():
    codigo = input("Ingrese el codigo del libro: ")
    for libro in inventario:
        if codigo in libro["codigo"]:
            try:
                cant_actu = int(input("Ingrese la nueva cantidad en stock: "))
                inventario["cantidad"] = cant_actu
                print("Se ha actualizado el stock sin problemas.")
            except ValueError:
                print("Por favor, ingrese un número entero.")
            return
    
    print("Libro no encontrado.")

def mostrar_inventrio():
    if len(inventario) > 0:
        for libro in inventario:
            print(f"Codigo: {libro["codigo"]}")
            print(f"Titulo: {libro["titulo"]}")
            print(f"Autor: {libro["autor"]}")
            print(f"Cantidad dicsponible: {libro["cantidad"]}")
            print(f"Precio: {libro["precio"]}")
            return
    
    else:
        print("El inventario se encuentra vacio.")
        return 

def mostrar_mas_caro():
    if len(inventario) == 0:
        print("El inventario se encuentra vacio.")
        return 
    
    costoso = inventario[0]

    for libro in inventario:
        if libro["precio"] > costoso["precio"]:
           costoso = libro 
    
    print("-LIBRO MÁS CARO-")
    print(f"Codigo: {costoso["codigo"]}")
    print(f"Titulo: {costoso["titulo"]}")
    print(f"Autor: {costoso["autor"]}")
    print(f"Cantidad dicsponible: {costoso["cantidad"]}")
    print(f"Precio: {costoso["precio"]}")
    return

def eliminar_libro():
    codigo = input("Ingrese el codigo de llibro a eliminar: ")
    for libro in inventario: 
        if libro["codigo"] == codigo:
            inventario.remove(libro)
            print("Libro eliminado con exito.")
        return
    
    print("Libro no encontrado.")


while True:
    print("----LIBRERIA----")
    print("1. Registrar libro")
    print("2. Buscar libro")
    print("3. Actualizar stock")
    print("4. Mostrar Inventario")
    print("5. Mostrar libro más caro")
    print("6. Eliminar libro")
    print("7. salir")

    try:
        opcion = input("Ingrese una opcion valida: ")

        match opcion:
            case "1":
                registra_libro()
            case "2":
                buscar_libro()
            case "3":
                actualizar_stock()
            case"4":
                mostrar_inventrio()
            case "5":
                mostrar_mas_caro()
            case "6":
                eliminar_libro()
            case "7":
                break
            case _:
                print("Opcion Invalida")
    except ValueError:
        print("Ingrese una opcion valida")
        
