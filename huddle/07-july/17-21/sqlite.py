# Better Comments extension for visualization

import sqlite3
from user import User  

conn = sqlite3.connect('users.db') #! Run me first
c = conn.cursor()

# 17. Creación de tabla: Escribe una consulta SQL para crear una tabla Usuarios con columnas id y nombre. #! Run me second
# c.execute("""CREATE TABLE IF NOT EXISTS users (
#           id INTEGER PRIMARY KEY AUTOINCREMENT,
#           user_name TEXT
#           )""")

def print_all_users():
    with conn:
        c.execute("SELECT * FROM users")
        rows = c.fetchall()

    for row in rows:
        print(f"User ID: {row[0]}, User Name: {row[1]}")

def insert_user(user):
    with conn:
        c.execute("INSERT INTO users (user_name) VALUES (?)", (user.user_name,))
        conn.commit()

def select_all_users():
    with conn:
        c.execute("SELECT * FROM users")
        rows = c.fetchall()

    for row in rows:
        print(f"User ID: {row[0]}, User Name: {row[1]}")

def update_user_name(user_id, new_user_name):
    with conn:
        c.execute("UPDATE users SET user_name = ? WHERE id = ?", (new_user_name, user_id))
        conn.commit()

def delete_user(user):
    with conn:
        c.execute("DELETE FROM users WHERE user_name = :user_name", {'user_name': user.user_name})
        conn.commit()

# Example users
user1 = User("Tommy")
user2 = User("Rambo")
user3 = User("Carlos")

# 18. Inserción de datos: Escribe una consulta SQL para insertar un solo registro en la tabla Usuarios. #! Run me third
# insert_user(user1)

# 19. Consulta básica: Escribe una consulta SQL para seleccionar todos los registros de la tabla Usuarios. #! Run me fourth
# print("All users:")
# print_all_users()

''' 
20. Actualizar registros: Escribe una consulta SQL 
para actualizar el nombre de un usuario específico en la tabla Usuarios. #! Run me fifth
'''
# update_user_name(1, "Carlyle") 
# print("Updated users:")
# print_all_users()

# 21. Eliminar registros: Escribe una consulta SQL para eliminar un usuario específico de la tabla Usuarios. #! Run me sixth
# delete_user(user1) 
# print("Updated users:")
# print_all_users()

# Close connection
conn.close()
