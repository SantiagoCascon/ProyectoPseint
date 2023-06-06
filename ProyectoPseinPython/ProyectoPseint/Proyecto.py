import psycopg2 as bd  # Conectamos a postgres

conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='Empleados_bd')
