import pymysql

def register_user(db_conn:pymysql.Connection, name, email, password, dob, phone):
    cursor = db_conn.cursor()
    sql = f"""
        INSERT INTO user (name, email, password, dob, phone, created_at) 
        VALUES ("{name}", "{email}", "{password}", "{dob}", "{phone}", NOW()) 
    """
    print(sql)
    try:
        cursor.execute(sql)
        db_conn.commit()
        return {"message": "User added successfully"}
    except pymysql.err.Error as e:
        return {"errors": [e.args[1]]}

def get_users(db_conn: pymysql.Connection):
    cursor = db_conn.cursor() 
    sql = "SELECT * FROM user"
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        return {"data": data}
    except pymysql.err.Error as e:
        return {"errors": [e.args[1]]}
    
def change_password(db_conn: pymysql.Connection, id, new_password):
    cursor = db_conn.cursor()
    sql = f"""
        UPDATE user SET password = "{new_password}" WHERE id = {id}
    """
    try:
        cursor.execute(sql)
        db_conn.commit()
        return {"message": "Password updated successfully"}
    except pymysql.err.Error as e:
        return {"errors": [e.args[1]]}
    

def login(db_conn: pymysql.Connection, email, password):
    cursor = db_conn.cursor()
    sql = f"""
        SELECT * FROM user WHERE email="{email}" AND password="{password}"
    """
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        if (data != None):
            return {"data": data, "message": "User login successfully"}
        else:
            return {"message": "Invalid email or password"}
    except pymysql.err.Error as e:
        return {"errors": [e.args[1]]}
