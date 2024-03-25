from school_db import con, cur
import os
import bcrypt

STATUS_MENU = True

def hash_password(passwd):
    """
    Función para generar el hash de una contraseña utilizando bcrypt.

    Parameters:
    passwd (str): La contraseña a ser hasheada.

    Returns:
    bytes: El hash de la contraseña.
    """
    return bcrypt.hashpw(passwd.encode(), bcrypt.gensalt())

def create_user():
    """
    Crea un nuevo usuario en la base de datos.

    Solicita al usuario que ingrese información como id_users, email, password, etc.
    Luego, inserta esta información en la tabla Users de la base de datos.

    No tiene argumentos de entrada, pero solicita información al usuario a través de la entrada estándar.

    No devuelve nada, pero imprime un mensaje indicando si el usuario ha sido creado exitosamente.
    """
    os.system('clear')
    print("::: Signup form :::")
    id_users = input("Your id_users: ")
    email = input("Your email: ")
    passwd = input("Your password: ")
    passwd_hashed = hash_password(passwd)
    status = input("Your status: ")
    created = input("Your created_at: ")
    updated = input("Your updated_at: ")
    deleted = input("Your deleted_at: ")

    new_user = f'''
        INSERT INTO 
            Users (id_users, email, password, status, created_at, updated_at, deleted_at) 
            VALUES ('{id_users}', '{email}', '{passwd_hashed.decode()}', '{status}', '{created}', '{updated}', '{deleted}')
    '''
    cur.execute(new_user)
    con.commit()

    print("::: New user has been created successfully :::")
    os.system('pause')

def create_student():
    """
    Crea un nuevo estudiante en la base de datos.

    Solicita al usuario que ingrese información como id_Students, code, id_persons, etc.
    Luego, inserta esta información en la tabla Students de la base de datos.

    No tiene argumentos de entrada, pero solicita información al usuario a través de la entrada estándar.

    No devuelve nada, pero imprime un mensaje indicando si el estudiante ha sido creado exitosamente.
    """
    os.system('clear')
    print("::: Signup form :::")
    id_students = input("Your id_Students: ")
    code = input("Your code : ")
    id_persons = input("Your id_persons : ")
    status = input("Your status: ")
    created = input("Your created_at: ")
    updated = input("Your updated_at: ")
    deleted = input("Your deleted_at: ")

    new_student = f'''
        INSERT INTO 
            Students (id_Student, code, id_persons, status, created_at, updated_at, deleted_at) 
            VALUES ('{id_students}', '{code}', '{id_persons}', '{status}', '{created}', '{updated}', '{deleted}')
    '''
    cur.execute(new_student)
    con.commit()

    print("::: New student has been created successfully :::")
    os.system('pause')

def menu():
    while STATUS_MENU:
        os.system('clear')
        print(":::::::::::::::::::::::")
        print(":::::: MAIN MENU ::::::")
        print(":::::::::::::::::::::::")
        print("[1]. Create a new user")
        print("[2]. Create student")
        print("[3]. Create identification type")
        print("[4]. Create person")
        print("[5]. Create city")
        print("[6]. Create department")
        print("[7]. Create country")
        print("[8]. Exit")

        opt = input("Press an option: ")
        if opt == '1':
            create_user()
        elif opt == '2':
            create_student()
        elif opt == '8':
            print("::: See you soon :::")
            break
        else:
            print(".:::::: Invalid option, try again.")

if __name__ == "__main__":
    menu()

# Close connection
con.close()