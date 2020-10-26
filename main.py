import mysql.connector

bd = mysql.connector.connect(
    user='admin', password='123456',
    database='nopalito')

cursor = bd.cursor()

while True:
    print('1) Agregar usuario')
    print('2) Mostrar usuarios')
    print('0) Salir')
    op = input()

    if op == '1':
        nombre = input('Nombre: ')
        apellidop = input('Apellido paterno: ')
        apellidom = input('Apellido materno: ')
        cp = input('Codigo postal: ')
        contra = input('Contraseña: ')

        consulta = "INSERT INTO usuario (Nombre, apellido_paterno, apellido_materno, codigo_postal, password) " \
                   "VALUES (%s, %s, %s, %s, %s)" 
        cursor.execute(consulta, (nombre, apellidop, apellidom, cp, contra))
        bd.commit()
        if cursor.rowcount:
            print('Se agregó usuario')
        else:
            print("Error")

    elif op == '2':
        consulta = "SELECT * FROM usuario"

        cursor.execute(consulta)
        for row in cursor.fetchall():
            print('Id: ', row[0])
            print('Apellido paterno: ', row[1])
            print('Apellido materno: ', row[2])
            print('Codigo postal: ', row[3])
            print('Contraseña: ', row[4])
            
    elif op == '0':
        break