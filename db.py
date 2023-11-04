import pymysql

def connect():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="exercise_class_1",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("db connected ...")
    return conn

def disconnect(conn):
    conn.close()