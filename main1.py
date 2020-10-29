import mysql.connector

bd = mysql.connector.connect(
    user='jazmin', password='123456',
    database='cinemapp')

cursor = bd.cursor()

while True:
    print('1) Agregar usuario')
    print('2) Mostrar usuarios')
    print('0) Salir')
    op = input()

    if op == '1':
        correo = input('correo: ')
        contra = input('contraseña: ')

        consulta = "INSERT INTO usuario (correo, contraseña) " \
                   "VALUES (%s, %s)" 
        cursor.execute(consulta, (correo, contra))
        bd.commit()
        if cursor.rowcount:
            print('Se agregó usuario')
        else:
            print("Error")

    elif op == '2':
        consulta = "SELECT * FROM usuario"

        cursor.execute(consulta)
        for row in cursor.fetchall():
            print('id: ', row[0])
            print('correo: ', row[1])
            print('contraseña: ', row[2])
            
    elif op == '0':
        break