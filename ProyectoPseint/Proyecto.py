# Algoritmo Registro Persona (Proyecto PSEINT)

# Importamos pyscopg2
import psycopg2 as bd  # Conectamos a postgres

# Creamos la conexion con nuestra base de datos
conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='Empleados_bd')

# Funcion Menu de INICIO
def inicio():
    opcion = 0
    while opcion != 3:
        print("\n-----------------INICIO DEL SISTEMA-----------------")
        print("1. Crear tabla")
        print("2. Ingresar al menu")
        print("3. Salir")
        opcion = int(input("-----------------SELECCIONE UNA OPCION: "))
        if opcion > 3:
            print("Opcion incorrecta")
        elif opcion == 1:
            tabla()
        elif opcion == 2:
            menu()
        elif opcion == 3:
            cierreConexion()

# Funcion para la creacion de nuestra tabla en la base de datos
def tabla():
    try:
        with conexion:
            with conexion.cursor() as cursor:
                print("Tabla 'empleados_bd' creada con exito")
                sentencia = (
                    f"CREATE TABLE empleados_bd (id_persona SERIAL, nombre VARCHAR(255), apellido VARCHAR(255), dni INT)")
                cursor.execute(sentencia)
    except Exception as e:
        print(f"Ocurrio un error: {e}")
    finally:
        print(f"Proceso finalizado.")

# Funcion MENU. Una vez dentro de el accedemos a las opciones de sistema.
def menu():
    opcion = 0
    while opcion != 6: 
        print("\n-----------------OPCIONES DEL SISTEMA-----------------")
        print("1. Registro de personal")
        print("2. Mostrar registros")
        print("3. Buscar personal")
        print("4. Calcular Vacaciones")
        print("5. Horario Laboral")
        print("6. Salir")
        opcion = int(input("-----------------SELECCIONE UNA OPCION: "))
        if opcion > 6:
            print("Opcion incorrecta")
        elif opcion == 1:
            registrar()
        elif opcion == 2:
            listarRegistros()
        elif opcion == 3:
            buscarEmpleado()
        elif opcion == 4:
            calculoVacaciones()
        elif opcion == 5:
            horarioLaboral()
        elif opcion == 6:
            salirInicio()

# Funcion REGISTRAR. Mediante esta funcion accedemos a la tabla para ingresar un registro
def registrar():
    print("\n-----------------MENU: Registro de personal.-----------------")
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'INSERT INTO empleados_bd (nombre, apellido, dni)VALUES (%s, %s, %s)'
                nombre = input("----Ingrese el NOMBRE: ")
                apellido = input("----Ingrese el APELLIDO: ")
                dni = int(input("----Ingrese el DNI (sin putos ni espacios): "))
                cursor.execute(sentencia, (nombre, apellido, dni))
                registros_insertados = cursor.rowcount
                print(f"Los registros insertados son: {registros_insertados}")
    except Exception as e:
        print(f"Ocurrio un error: {e}")
    finally:
        print("Proceso finalizado")

# Funcion REGISTROS. Mediante esta funcion listamos todos los registros de nuestra tabla.
def listarRegistros():
    print("\n-----------------MENU: Mostrar registros.-----------------")
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'SELECT * FROM empleados_bd'
                cursor.execute(sentencia)
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)
    except Exception as e:
        print(f"Ocurrio un error: {e}")
    finally:
        print("Listado de registros exitoso.\n")

 # Creamos la funcion para buscar un determinado registro dentro de la tabla
def buscarEmpleado():
    print("\n-----------------MENU: Buscar personal.-----------------")
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'SELECT * FROM empleados_bd WHERE dni = %s'
                dni = input("Ingrese el DNI (sin putos ni espacios): ")
                cursor.execute(sentencia, (dni,))
                registros = cursor.fetchone()
                if registros is None:
                    print("El dni ingresado no existe")
                else:
                    print(registros)
    except Exception as e:
        print(f"Ocurrio un error: {e}")
    finally:
        print("Proceso Finalizado")

# Calculamos las vacaciones correspondientes a cada empleado ingresando sus días trabajados.
def calculoVacaciones():
    print("\n-----------------MENU: Calcular vacaciones.-----------------")
    diasT = int(input("Ingrese la cantidad de días trabajados: "))
    if diasT >= 180:
        print("\nLe corresponden 15 días de vacaciones.")
    else:
        print("\nLe corresponden 7 días de vacaciones.")

# Creamos un cronograma de horario laboral por semana.
def horarioLaboral():
    print("\n-----------------MENU: Horario Laboral.-----------------")
    ingreso = input("Horario de Ingreso (digitar hh:mm): ")
    salida = input("Horario de Salida (Digitar hh:mm): ")
    print("\n----------- CRONOGRAMA DE HORARIOS -----------")
    print(f"LUNES  --  MARTES -- MIERCOLES -- JUEVES -- VIERNES -- SABADO")
    print(f"{ingreso}  --  {ingreso}  --   {ingreso}   --  {ingreso} --  {ingreso}  --  {ingreso} ")
    print(f"{salida}  --  {salida}  --   {salida}   --  {salida} --  {salida}  --  {salida} \n")

# Cerramos nuestro menu principal, para volver al inicio.
def salirInicio():
    print("Hasta pronto")

# Mediante esta funcion cerramos la conexion con nuestra tablass
def cierreConexion():
    conexion.close()
    print(conexion)


inicio()
