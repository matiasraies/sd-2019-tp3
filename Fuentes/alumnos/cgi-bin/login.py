#!/usr/bin/python3

from HttpResponse import HttpResponse
import cgi
import cgitb; cgitb.enable()  # Optional; for debugging only
from RepoAlumnos import RepoAlumnos
import os
from http import cookies
from RepoCookies import RepoCookies

# Recupero los argumentos de la llamada               
arguments = cgi.FieldStorage()

if arguments.getvalue("operacion") == "alta":
    
    HttpResponse.nuevo_alumno()
       
elif arguments.getvalue("operacion") == "saveAlta":
    
    try:    
        if not RepoAlumnos.existe_alumno(arguments.getvalue("legajo")):
            RepoAlumnos.guardar_alumno(arguments.getvalue("legajo"), arguments.getvalue("nombre"), arguments.getvalue("sexo"), arguments.getvalue("edad"), arguments.getvalue("pwd"))
            HttpResponse.operacion_exitosa()        
        else:
            HttpResponse.operacion_erronea("Ya existe el legajo")
             
    except Exception as err:
        
        HttpResponse.operacion_erronea(err)        
    
elif arguments.getvalue("operacion") == "modif":   
   
    # Recupero la cookie de sesion si esta presente en la llamada
    legajo = ""

    try:
        cookie = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
        legajo = RepoCookies.get_cookie_data(cookie["session"].value) 
        
        if legajo == "":
            HttpResponse.login_alumno()
        else:
            try:  
                result = RepoAlumnos.get_alumno(legajo) 
                cookieKey = None
                HttpResponse.modificar_alumno(result[0], result[1], result[2], result[3], result[4], cookieKey)
            except Exception as err:
                
                HttpResponse.operacion_erronea(err)   
   
    except (cookies.CookieError, KeyError):
        
        HttpResponse.login_alumno ()
        
elif arguments.getvalue("operacion") == "login":  
    
    try:
        if RepoAlumnos.validarUsuario (arguments.getvalue("legajo"), arguments.getvalue("pwd")): 
            
            result = RepoAlumnos.get_alumno(arguments.getvalue("legajo"))
            
            cookieKey = RepoCookies.new_cookie(arguments.getvalue("legajo"))
            
            HttpResponse.modificar_alumno(result[0], result[1], result[2], result[3], result[4], cookieKey)

        else:
            HttpResponse.operacion_erronea("ATENCION !!! Usuario o contrasena inval&iacute;da.")  
    
    except Exception as err:
        
        HttpResponse.operacion_erronea(err)    
      
elif arguments.getvalue("operacion") == "saveModif":   
    
    try:    
        
        RepoAlumnos.guardar_alumno("123456", arguments.getvalue("nombre"), arguments.getvalue("sexo"), arguments.getvalue("edad"), arguments.getvalue("pwd"))
        HttpResponse.operacion_exitosa()        
             
    except Exception as err:
        
        HttpResponse.operacion_erronea(err)
        
elif arguments.getvalue("operacion") == "listNombre":  
    
    try:
        
        lista = RepoAlumnos.lista_alumnos_nombre(arguments.getvalue("nombre"))
        HttpResponse.lista_filtro_nombre(lista)
    
    except Exception as err:
        
        HttpResponse.operacion_erronea(err)

elif arguments.getvalue("operacion") == "listEdad":  
    
    try:
        
        lista = RepoAlumnos.lista_alumnos_rango_edad(arguments.getvalue("minEdad"), arguments.getvalue("maxEdad"))
        HttpResponse.lista_filtro_edad(lista)
    
    except Exception as err:
        
        HttpResponse.operacion_erronea(err)
