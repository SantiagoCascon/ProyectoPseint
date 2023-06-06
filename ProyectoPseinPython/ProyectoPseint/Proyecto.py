import psycopg2 as bd  # Conectamos a postgres

conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='Empleados_bd')

# Creamos el menu de nuestro programa
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
            salir()
               
 # Creamos las funciones para cada una de las opciones de nuestro menú
# FUNCION PARA REGISTRAR PERSONAL
def registrar():
    print("\n-----------------MENU: Registro de personal.-----------------")
    try:
        with conexion:
            with conexion.cursor() as cursor:
                # Placheholder
                sentencia = 'INSERT INTO empleados_bd (nombre, apellido, dni)VALUES (%s, %s, %s)'
                nombre = input("----Ingrese el NOMBRE: ")
                apellido = input("----Ingrese el APELLIDO: ")
                dni = int(input("----Ingrese el DNI (sin putos ni espacios): "))
                # Ejecutamos sentencia
                cursor.execute(sentencia, (nombre, apellido, dni))
                registros_insertados = cursor.rowcount
                print(f"Los registros insertados son: {registros_insertados}")
    except Exception as e:
        print(f"Ocurrio un error: {e}")
    finally:
        print("Registro ingresado con excito.")

# FUNCION PARA LISTAR REGISTROS 
def listarRegistros():
    print("\n-----------------MENU: Mostrar registros.-----------------")
    try:
        with conexion:
            with conexion.cursor() as cursor:
                # Placheholder
                sentencia = 'SELECT * FROM empleados_bd'
                cursor.execute(sentencia)  # Ejecutamos sentencia
                registros = cursor.fetchall()
                for registro in registros:
                    print(registros)
    except Exception as e:
        print(f"Ocurrio un error: {e}")
    finally:
        print("Listado de registros exitoso.\n")

 #  FUNCION PARA BUSCAR UN REGISTRO POR SU DNI
def buscarEmpleado():
    print("\n-----------------MENU: Buscar personal.-----------------")
    try:
        with conexion:
            with conexion.cursor() as cursor:
                # Placheholder
                sentencia = 'SELECT * FROM empleados_bd WHERE dni = %s'
                dni = input("Ingrese el DNI (sin putos ni espacios): ")
                cursor.execute(sentencia, (dni,))  # Ejecutamos sentencia
                registros = cursor.fetchone()
                print(f"Registro encontrado con excito.\n {registros}")
    except Exception as e:
        print(f"Ocurrio un error: {e}")
    finally:
        print(" ")

 # FUNCION PARA CALCULAR VACACIONES
def calculoVacaciones():
    print("\n-----------------MENU: Calcular vacaciones.-----------------")
    diasT = int(input("Ingrese la cantidad de días trabajados: "))
    if diasT >= 180:
        print("\nLe corresponden 15 días de vacaciones.")
    else:
        print("\nLe corresponden 7 días de vacaciones.")

 # FUNCION PARA CRONOGRAMA DE HORARIOS 
def horarioLaboral():
    print("\n-----------------MENU: Horario Laboral.-----------------")
    ingreso = input("Horario de Ingreso (digitar hh:mm): ")
    salida = input("Horario de Salida (Digitar hh:mm): ")
    print("\n----------- CRONOGRAMA DE HORARIOS -----------")
    print(f"LUNES  --  MARTES -- MIERCOLES -- JUEVES -- VIERNES -- SABADO")
    print(f"{ingreso}  --  {ingreso}  --   {ingreso}   --  {ingreso} --  {ingreso}  --  {ingreso} ")
    print(f"{salida}  --  {salida}  --   {salida}   --  {salida} --  {salida}  --  {salida} \n")
    
# FUNCION PARA FINALIZAR PROGRAMA Y CERRAR LA CONEXION CON LA BASE DE DATOS
def salir():
    print("Hasta pronto")
    conexion.close()
    print(conexion)
    
# POR ULTIMO LLAMAMOS A LA FUNCION DE MENU PARA DARLE VIDA A NUESTRO PROGRAMA
menu()
