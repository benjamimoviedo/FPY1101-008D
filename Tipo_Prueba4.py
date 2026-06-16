tareas = []

#Funciones de Validacion
def validar_descripcion(descripcion):
    """
    Esta funcion recibe la descripcion de la tarea en fomrato str, mide 
    su cantidad de caracteres y retorna si la descripcion es valida o no.
    Si se ingresa solamente espacion vacios (en blanco), se usa un .strip() 
    para eliminarlos y que len() sea igual a 0.
    """
    if  len(descripcion.strip()) > 0:
        return True
    else:
        return False

def validar_prioridad(prioridad):
    """
    Esta funcion recibe la prioridad de la tarea en formato int, si esta
    esta entre 1 y 10 retorna dicho valor de priroridad.
    Si esto no se cumple o se ingresa un valor no valido la funcion retorna 
    un False.
    """
    try:
        if 1 <= prioridad <= 10:
            return True
        return False
    except ValueError:
        return False
    

def validar_tiempo(tiempo_str):
    """
    Esta funcion recibe el timepo destinado a la tarea en formato str, lo convierte 
    a float (decimal) y si este es mayor a 0, se reotrna dicho valor.
    Si hay un error de valor, se retorna False.
    """
    try:
        tiempo = float(tiempo_str)
        return tiempo > 0
    except ValueError:
        return False

#Funciones de menu

def menu():
    """
    Esta solo muestra en terminal lo escrito.
    No tiene ni parametros ni retorno.
    """
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar tarea")
    print("2. Buscar tarea")
    print("3. Eliminar tarea")
    print("4. Actualizar estado")
    print("5. Mostrar tareas")
    print("6. Salir")
    print("="*36)

def leer_opcion():
    """

    """
    opcion = input("Seleccione una opción: ")
    if opcion.isdigit() and 1 <= int(opcion) <= 6:
        return int(opcion)
    else:
        print("Opción inválida. Intente nuevamente.")
        return 0

#Funciones de proceso

def agregar_tarea(tareas):
    descripcion = input("Ingrese la descripción de la tarea: ")
    prioridad = input("Ingrese la prioridad (1 al 10): ")
    tiempo = input("Ingrese el tiempo estimado en horas: ")
    
    
    if not validar_descripcion(descripcion):
        print("Error: La descripción no puede estar vacía.")
        return
    if not validar_prioridad(prioridad):
        print("Error: La prioridad debe ser un número entero entre 1 y 10.")
        return
    if not validar_tiempo(tiempo):
        print("Error: El tiempo estimado debe ser un número decimal mayor que cero.")
        return
        
    nueva_tarea = {
        "descripcion": descripcion,
        "prioridad": prioridad,
        "tiempo_estimado": float(tiempo),
        "completada": False  
    }
    tareas.append(nueva_tarea)
    print("Tarea registrada exitosamente.")

def buscar_tarea(descripcion, tareas):
    i = 0
    while i < len(tareas):
        if descripcion == tareas[i]["descripcion"]:
            return i
        i += 1
    return -1

def eliminar_tarea(tareas):
    descripcion = input("Ingrese la tarea a eliminar")
    posicion = buscar_tarea(descripcion,tareas)
    if posicion != -1:
        tareas.pop(posicion)
    else:
        return -1

def actualizar_estado(tareas):
    for tarea in tareas:
        if tarea["prioridad"] >= 5:
            tarea["completada"] = True
        else:
            tarea["completada"] = False

def mostrar_tareas(tareas):
    actualizar_estado(tareas)
    print("=== LISTA DE TAREAS ===")
    for tarea in tareas:
        
        print(f"Descripcion: {tarea['descripcion']}") 
        print(f"Prioridad: {tarea['prioridad']}") 
        print(f"Tiempo estimado: {tarea['tiempo_estimado']}")
        if tarea["completada"] == True:
            print(f"Estado: COMPLETADA")
        else:
            print(f"Estado: PENDIENTE")
        print("*********************************************")

while True:
    menu()               
    opcion = leer_opcion() 
    
    if opcion == 1:
        agregar_tarea(tareas)
        
    elif opcion == 2:
        descripcion_buscar = input("Ingrese la descripción de la tarea a buscar: ")
        posicion = buscar_tarea(descripcion_buscar, tareas)
        if posicion != -1:
            print(f"Tarea encontrada en la posición {posicion}:")
        else:
            print("Tarea no encontrada.")
            
    elif opcion == 3:
        eliminar_tarea(tareas)
        
    elif opcion == 4:
        actualizar_estado(tareas)
        print("Estados actualizados exitosamente")
        
    elif opcion == 5:
        mostrar_tareas(tareas)
        
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break 
        
