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
