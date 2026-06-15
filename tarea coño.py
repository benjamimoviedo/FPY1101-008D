tareas = [] #Inicialización de la lista
def agregar_tarea():
 global tareas
 nombre = input("Ingrese la tarea a agregar: ") #Variable renombrada
#Verificar duplicado correctamente
 for tarea in tareas:
  if tarea["tarea"] == nombre:
   print("La tarea ya existe en la lista.")
   return
 descripcion = input("Ingrese una descripción para la tarea: ")
#try/except fuera del if, siempre se ejecuta
 try:
  tiempo = int(input("Ingrese el tiempo estimado (en minutos): "))
  prioridad = int(input("Ingrese la prioridad de la tarea (1-10): "))
  prioridad = (prioridad if 1 <= prioridad <= 10 else 10)
 except ValueError:
  print("Error: Ingrese un número entero válido.")
  return
#Crear dict con nombre correcto y agregar a la lista
 nueva_tarea = {
  "tarea": nombre,
  "descripcion": descripcion,
  "tiempo": tiempo,
  "prioridad": prioridad
 }
 tareas.append(nueva_tarea)
 print("Tarea agregada exitosamente.")
def buscar_tarea():
 nombre = input("Ingrese el nombre de la tarea a buscar: ")
 for tarea in tareas:
  if tarea["tarea"] == nombre: #Compara con nombre, no consigo mismo
   print("\n====== Tarea encontrada ======")
   print(f"Tarea: {tarea['tarea']}")
   print(f"Descripción: {tarea['descripcion']}")
   print(f"Tiempo estimado: {tarea['tiempo']} minutos")
   print(f"Prioridad: {tarea['prioridad']}")
   return
 print("Tarea no encontrada en la lista.")
def eliminar_tarea():
 nombre = input("Ingrese el nombre de la tarea a eliminar: ")
 for tarea in tareas:
  if tarea["tarea"] == nombre:
   tareas.remove(tarea)
   print("Tarea eliminada exitosamente.")
   return
 print("Tarea no encontrada en la lista.")
def actualizar_tarea():
 nombre = input("Ingrese el nombre de la tarea a actualizar: ")
 for tarea in tareas:
  if tarea["tarea"] == nombre:
   descripcion = input("Ingrese la nueva descripción de la tarea: ") #Un solo input
   try:
    tiempo = int(input("Ingrese el nuevo tiempo estimado (en minutos): "))
    prioridad = int(input("Ingrese la nueva prioridad (1-10): "))
    prioridad = (prioridad if 1 <= prioridad <= 10 else 10)
   except ValueError:
    print("Error: Ingrese un número entero válido.")
    return
   tarea["descripcion"] = descripcion
   tarea["tiempo"] = tiempo
   tarea["prioridad"] = prioridad
   print("Tarea actualizada exitosamente.")
   return
  print("Tarea no encontrada en la lista.")
def mostrar_tareas():
  global tareas
  print(f"Las Tareas ingresadas son: \n{tareas}")
  if len(tareas) == 0:
    print("La lista de tareas está vacía.")
  return
print("\n====== Lista de tareas ======")
for tarea in tareas:
  print(f"Tarea: {tarea['tarea']}")
  print(f"Descripción: {tarea['descripcion']}")
  print(f"Tiempo estimado: {tarea['tiempo']} minutos")
  print(f"Prioridad: {tarea['prioridad']}")
  print("*****************************")
#El while está al nivel raíz, fuera de todas las funciones
while True:
  print("\n======Gestor de tareas======")
  print("1. Agregar tarea")
  print("2. Buscar tarea")
  print("3. Eliminar tarea")
  print("4. Actualizar tarea")
  print("5. Mostrar todas las tareas")
  print("6. Salir")
  opcion = input("Seleccione una opción: ")
  if opcion == "1":
    agregar_tarea()
  elif opcion == "2":
    buscar_tarea()
  elif opcion == "3":
    eliminar_tarea()
  elif opcion == "4":
    actualizar_tarea()
  elif opcion == "5":
    mostrar_tareas()
  elif opcion == "6":
    print("Saliendo del gestor de tareas.")
    break
  else:
    print("Opción no válida. Seleccione una opción del 1 al 6.")