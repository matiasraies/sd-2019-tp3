#!/usr/bin/python
import cgi
import csv
import json
import Cookie

"""
Funcion para agregar mensajes.
"""


def add_message(form):
    # Get data from fields
    idUser = form.getvalue('idUser')
    nick = form.getvalue('nick')
    message = form.getvalue('message')
    hora = form.getvalue('hora')

    archivo = open(DBNAME, 'a')
    archivo_csv = csv.writer(archivo)  # Asocio modulo a archivo
    archivo_csv.writerow([idUser, hora, nick, message])
    archivo.close()  

    print ("Content-Type: text/html")
    print ("\n\n")


"""
Funcion para obtener los mensajes.
"""


def get_messages(form):
    count = 0
    countE = 0
    array = []

    # Get data from fields
    lineasEscritas = form.getvalue('lineas')

    with open(DBNAME) as csvarchivo:
        entrada = csv.reader(csvarchivo)
        for reg in entrada:
            if int(lineasEscritas) == count:
                array.append(reg)
                countE += 1
                continue
            count += 1

    cantMsg = int(lineasEscritas) + int(countE)

    # Create a Cookie object.
    a_cookie = Cookie.SimpleCookie()
    # Assign the cookie a value.
    a_cookie["cantMsg"] = cantMsg
    a_cookie["cantMsg"]["path"] = "/chat/"

    print ("Content-Type: application/json")
    print (a_cookie)
    print ("\n\n")
    print(json.JSONEncoder().encode(array))
    print ("\n\n")


DBNAME = "DB.csv"
form = cgi.FieldStorage()
op = form.getvalue('op')

if op == "0":
    add_message(form)
elif op == "1":
    get_messages(form)

