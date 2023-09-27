import pymysql


def createDatabase():
    sql = '''create database RDSDB'''
    cursor.execute(sql)
    cursor.connection.commit()
    print("Crated Database!")

def dropTable():
    sql = '''drop database RDSDB'''
    cursor.execute(sql)
    print("Metodo DROP TABLE hecho")

def createTable():
    sql = '''create table Usuarios'''
    cursor.execute(sql)
    print("Metodo CREAR TABLA HECHO")

def useDB():
    sql = '''USE DATABASE RDSDB'''
    cursor.execute(sql)
    print("Metodo USE HECHO")


def select():
    sql = '''select * from RDSDB'''
    cursor.execute(sql)
    print("Metodo SELECT HECHO")


def delete():
    sql = '''delete * from RDSDB'''
    cursor.execute(sql)
    print("Metodo delete HECHO")

def update():
    sql = '''
    create table Usuarios (
    id int not null auto_increment,
    nombre text,
    apellido text,
    mail text,
    primary key (id)
    )
    '''
    cursor.execute(sql)
    print("Metodo CREAR TABLA HECHO")


def insert():
    sql = '''INSERT INTO Usuarios VALUES (NULL,'Erik','Diaz','erik@gmail.com')'''
    cursor.execute(sql)
    print("Metodo INSERTAR HECHO")


if __name__ == '__main__':
    db = pymysql.connect(host='DATABASE ENDPOINT', user='admin', password='admin1998')

    cursor = db.cursor()
    cursor.execute("select version()")
    data = cursor.fetchone()
    print("Database version : %s " % data)

    #We call each method to create, instead we could automatice it

    #createDatabase()
    #print("BD created")

    # useDB()
    # print("We are using RDSBD ")

    #createTable()
    #print("USUARIOS table created")


    #insert()

