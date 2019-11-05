#!/usr/bin/python
import cgi
import csv
import random
import json
import Cookie

"""
Funcion para agregar usuarios.
"""


def add_user(user):
    idUser = random.randrange(1000) 

    archivo = open(DBNAME, 'a')
    archivo_csv = csv.writer(archivo)
    archivo_csv.writerow([idUser, user])
    archivo.close()         

    # Create a Cookie object.
    a_cookie = Cookie.SimpleCookie()

    # Assign the cookie a value.
    a_cookie["session"] = str(idUser) + "-" + str(user)
    a_cookie["session"]["path"] = "/chat/"

    print ("Content-Type: text/html")
    print (a_cookie.output()) 
    print ("\n\n")


"""
Funcion para borrar usuarios.
"""


def delete_user(user):
    new_rows = [] 

    with open(DBNAME) as csvarchivo:
        entrada = csv.reader(csvarchivo)
        for reg in entrada:
            if reg[0] != user:
                new_rows.append(reg)

    with open(DBNAME, 'wb') as csvarchivo:
        writer = csv.writer(csvarchivo)
        writer.writerows(new_rows)

    print ("Content-Type: text/html")
    print ("\n\n")


"""
Funcion para obtener los usuarios.
"""


def get_users():
    array = []

    with open(DBNAME) as csvarchivo:
        entrada = csv.reader(csvarchivo)
        for reg in entrada:
            array.append(reg)

    print ("Content-Type: application/json")
    print ("\n\n")
    print(json.JSONEncoder().encode(array))
    print ("\n\n")
    

DBNAME = "DBUser.csv"
form = cgi.FieldStorage()    
user = form.getvalue('user')
op = form.getvalue('op')

if op == "0":
    add_user(user)
elif op == "1":
    delete_user(user)
elif op == "2":
    get_users()