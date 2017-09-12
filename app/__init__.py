import pymysql

db = pymysql.connect("localhost","root","Gloriela1996","test")
cursor = db.cursor()

# PRUEBA DE INSTALACION DE MARIADB
#cursor.execute("SELECT VERSION()")
#data = cursor.fetchone()
#print("version de MariaDB: %s" % data)

# ELIMINACION/CREACION DE TABLAS
#cursor.execute("DROP TABLE IF EXISTS EMPLEADO")
#sql = """CREATE TABLE EMPLEADO(
#  NOMBRE VARCHAR(20) NOT NULL,
#  APELLIDO VARCHAR(20),
#  EDAD INT,
#  SEXO CHAR(1),
# SALARIO FLOAT
#  )"""
#cursor.execute(sql)

#INSERTAR DATOS A LA TABLA
sql = """INSERT INTO EMPLEADO(NOMBRE,APELLIDO,SEXO,EDAD,SALARIO)
        VALUES ('PETRA','PETROV', 88, 'F', 15000)"""
try:
   cursor.execute(sql)
   db.commite()
except:
   db.rollback()

#LEER DATOS D LA TABLA EMPLEADO
#e = int(input("EDAD DE PETRA> "))
#salario = []
#sql = "SELECT * FROM EMPLEADO WHERE EDAD > '%d'" % e

#try:
#    cursor.execute(sql)
#    resultado = cursor.fetchall()
#    for registrar in resultado:
#        salario = resultado(4)
#        salario.append(salario)
#except:
#    print("ERROR AL OBTENER DATOS")
#db.close()

#if len(salario) > 0:
#    print("El salario mas alto de petra fue de $" + str(max(salario)))
#else:
#    print("No ay salario de petra para ese rango de edad")

#ACTUALIZAR DATOS
#sql = "UPDATE EMPLEADO SET EDAD = EDAD + 1 WHERE SEXO = 'F'"
#try:
#    cursor.execute(sql)
#    db.commit()
#except:
#    db.rollback()
db.close()