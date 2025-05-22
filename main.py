def leer_empleados(nombre_archivo):
    empleados = []
    try:
        with open(nombre_archivo, 'r') as file:
            for linea in file:
                nombre, ocupacion, precio = linea.strip().split(';')
                empleados.append({
                    'nombre': nombre,
                    'ocupacion': ocupacion,
                    'precio': int(precio)
                })
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
    return empleados

def leer_clientes(nombre_archivo):
    clientes = []
    try:
        with open(nombre_archivo, 'r') as file:
            for linea in file:
                nombre, ocupacion, presupuesto = linea.strip().split(';')
                clientes.append({
                    'nombre': nombre,
                    'ocupacion': ocupacion,
                    'presupuesto': int(presupuesto)
                })
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
    return clientes

def emparejar_empleados_clientes(empleados, clientes):
    emparejamientos = []
    empleados_usados = set()

    for cliente in clientes:
        for i, empleado in enumerate(empleados):
            if i not in empleados_usados and \
               cliente['ocupacion'] == empleado['ocupacion'] and \
               cliente['presupuesto'] >= empleado['precio']:
                emparejamientos.append({
                    'cliente': cliente['nombre'],
                    'empleado': empleado['nombre'],
                    'precio_empleado': empleado['precio'],
                    'presupuesto_cliente': cliente['presupuesto']
                })
                empleados_usados.add(i)
                break 

    return emparejamientos

empleados = leer_empleados("docs/empleados.txt")
clientes = leer_clientes("docs/clientes.txt")

emparejamientos = emparejar_empleados_clientes(empleados, clientes)

print("\n========== EMPAREJAMIENTOS REALIZADOS ==========\n")

if emparejamientos:
    for e in emparejamientos:
        print(f"{e['cliente']} contrató a {e['empleado']} "
              f"(Precio/hora: ${e['precio_empleado']} | Presupuesto: ${e['presupuesto_cliente']})")
else:
    print("No se realizaron emparejamientos.")

print(f"\n🔢 Total de emparejamientos realizados: {len(emparejamientos)}")
