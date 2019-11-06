#!/usr/bin/python3

from http import cookies


class HttpResponse:
    
    @classmethod
    def operacion_erronea(self, err):
        
        print ("Content-type:text/html\r\n\r\n")

        print ("<HTML><HEAD><TITLE>Nuevo Alumno</TITLE>")
                      
        print ("       </HEAD>")
        print ("<BODY>")
        print ("    <CENTER>")
        print ("        <paragraph> ERROR: Se ha producido un error al guardar los datos: ", err)
        print ("    </CENTER>")
        print ("<HR>")

        print ("</form>")
        print ("</BODY>")
        print ("</HTML>")
    
    @classmethod
    def operacion_exitosa(self):
        
        print ("Content-type:text/html\r\n\r\n")

        print ("<HTML><HEAD><TITLE>Admin Alumnos</TITLE>")
        print ("   <meta http-equiv='refresh' content='2;url=http://localhost/alumnos/public_html/' />")       
                      
        print ("       </HEAD>")
        print ("<BODY>")
        print ("    <CENTER>")
        print ("        <paragraph> La operaci&oacute;n se realizo exitosamente !!! ")
        print ("    </CENTER>")
        print ("<HR>")

        print ("</form>")
        print ("</BODY>")
        print ("</HTML>")
    
    @classmethod
    def nuevo_alumno(self):
        print ("Content-type:text/html\r\n\r\n")
        
        print ("<!DOCTYPE html>")
        print ("<HTML><HEAD><TITLE>Nuevo Alumno</TITLE>")
               
        print ("   <script type='text/javascript'>")

        print ("    function mySubmit(op)")
        print ("            {")
                    
        print ("                document.getElementById('operacion').value = op;")
                    
        print ("           }")

        print ("       </script>")
               
        print ("       </HEAD>")
        print ("<BODY>")
        print ("    <CENTER>")
        print ("    <FORM method='GET' action='http://localhost/alumnos/cgi-bin/login.py'>")
        print ("        <input type='hidden' id='operacion' name='operacion' value='' />")
        print ("<table>")
        print ("<tr>")
        print ("<td align='right'> <html><span> Legajo: </span></label> </td>")
        print ("                 <td> <input type='text'  id='legajo' name='legajo' minlength='6' maxlength='10' required /> </td> ")
        print ("</tr>")
        print ("<tr>")
        print ("<td align='right'> <html><span> Nombre y Apellido: </span></label> </td>")
        print ("                 <td> <input type='text' id='nombre' name='nombre' maxlength='70' required/> </td>")
        print ("<tr>")
        print ("<td align='right' > Sexo: </td> ")
        
        print ("                 <td><select name='sexo' required >   ")
        print ("                        <option>Hombre</option>   ")
        print ("                        <option>Mujer</option>   ")
        print ("                     </select> </td>")
        print ("</tr>")
        print ("<tr>")
        print ("<td align='right'> Edad: </td>")
        print ("                 <td> <input type='number' min='1' max='99'  id='edad' name='edad' required />  </td> ")
        print ("</tr>")
        print ("<tr>")
        print ("<td align='right' > Password: </td> ")
        print ("                 <td> <input type=password id='pwd' name='pwd' required /> </td>")
        print ("</tr>")
        print ("<tr>")
        print ("<td colspan=2 align='center' >")
        print ("        <input type='submit' value='Guardar Datos' onclick=mySubmit('saveAlta') />")
        print ("</td>")
        print ("</tr>")
        print ("</table>")
        print ("    </FORM>")
        print ("    </CENTER>")
        print ("<HR>")

        print ("</form>")
        print ("</BODY>")
        print ("</HTML>")

    @classmethod
    def login_alumno(self):
        print ("Content-type:text/html\r\n\r\n")
        
        print ("<!DOCTYPE html>")
        print ("<HTML><HEAD><TITLE>Login Alumno</TITLE>")
               
        print ("   <script type='text/javascript'>")

        print ("    function mySubmit(op)")
        print ("            {")
                    
        print ("                document.getElementById('operacion').value = op;")
                    
        print ("           }")

        print ("       </script>")
               
        print ("       </HEAD>")
        print ("<BODY>")
        print ("    <CENTER>")
        print ("    <FORM method='GET' action='http://localhost/alumnos/cgi-bin/login.py'>")
        print ("        <input type='hidden' id='operacion' name='operacion' value='' />")
        print ("<table>")
        print ("<tr>")
        print ("<td align='right'> <html><span> Legajo: </span></label> </td>")
        print ("                 <td> <input type='text'  id='legajo' name='legajo' minlength='6' maxlength='10' required /> </td> ")
        print ("</tr>")
        print ("<tr>")
        print ("<td align='right' > Password: </td> ")
        print ("                 <td> <input type=password id='pwd' name='pwd' required /> </td>")
        print ("</tr>")
        print ("<tr>")
        print ("<td colspan=2 align='center' >")
        print ("        <input type='submit' value='Ingresar' onclick=mySubmit('login') />")
        print ("</td>")
        print ("</tr>")
        print ("</table>")
        print ("    </FORM>")
        print ("    </CENTER>")
        print ("<HR>")

        print ("</form>")
        print ("</BODY>")
        print ("</HTML>")

    @classmethod
    def modificar_alumno(self, legajo, nombre, sexo, edad, pwd, cookieKey):
        
        # Seteo la cookie  
                
        if not (cookieKey is None or cookieKey == ""):
            cookie = cookies.SimpleCookie()
            cookie["session"] = cookieKey
            
            print ("Content-type: text/plain")
            print (cookie.output())
                
        print ("Content-type:text/html\r\n\r\n")

        print ("<!DOCTYPE html>")
        print ("<HTML><HEAD><TITLE>Modificar Alumno</TITLE>")
               
        print ("   <script type='text/javascript'>")

        print ("    function mySubmit(op)")
        print ("            {")
                    
        print ("                document.getElementById('operacion').value = op;")
                    
        print ("           }")

        print ("       </script>")
               
        print ("       </HEAD>")
        print ("<BODY>")
        print ("    <CENTER>")
        print ("    <FORM method='GET' action='http://localhost/alumnos/cgi-bin/login.py'>")
        print ("        <input type='hidden' id='operacion' name='operacion' value='' />")
        print ("<table>")
        print ("<tr>")
        print ("<td align='right'> <html><span> Legajo: </span></label> </td>")
        print ("                 <td> <input type='text'  id='legajo' name='legajo' minlength='6' maxlength='10' disabled value='" + legajo + "' /> </td> ")
        print ("</tr>")
        print ("<tr>")
        print ("<td align='right'> <html><span> Nombre y Apellido: </span></label> </td>")
        print ("                 <td> <input type='text' id='nombre' name='nombre' maxlength='70' required value='" + nombre + "'/> </td>")
        print ("<tr>")
        print ("<td align='right' > Sexo: </td> ")
        
        print ("                 <td><select id='sexo' name='sexo' required >   ")
        print ("                        <option>Hombre</option>   ")
        print ("                        <option>Mujer</option>   ")
        print ("                     </select> </td>")
        print ("</tr>")
        
        print ("           <script type='text/javascript'>")
        print ("                document.getElementById('sexo').value='" + sexo + "';")
        print ("           </script>")        
        
        print ("<tr>")
        print ("<td align='right'> Edad: </td>")
        print ("                 <td> <input type='number' min='1' max='99'  id='edad' name='edad' required value='" + edad + "' />  </td> ")
        print ("</tr>")
        print ("<tr>")
        print ("<td align='right' > Password: </td> ")
        print ("                 <td> <input type=password id='pwd' name='pwd' required value='" + pwd + "' /> </td>")
        print ("</tr>")
        print ("<tr>")
        print ("<td colspan=2 align='center' >")
        print ("        <input type='submit' value='Guardar Datos' onclick=mySubmit('saveModif') />")
        print ("</td>")
        print ("</tr>")
        print ("</table>")
        print ("    </FORM>")
        print ("    </CENTER>")
        print ("<HR>")

        print ("</form>")
        print ("</BODY>")
        print ("</HTML>")
        
    @classmethod
    def lista_filtro_nombre(self, listaAlumnos):
        print ("Content-type:text/html\r\n\r\n")
        
        print ("<!DOCTYPE html>")
        print ("<HTML><HEAD><TITLE>Busqueda Alumnos</TITLE>")
        print ("    <style>")
        
        print ("                table") 
        print ("                {") 
        print ("                    border-collapse:collapse;") 
        print ("                }") 
        print ("                tr:nth-child(3)") 
        print ("                {") 
        print ("                    background-color: #eef2f3;") 
        print ("                    color:black;") 
        print ("                }") 
        print ("                td") 
        print ("                {") 
        print ("                    border:1px solid white;") 
        print ("                }") 
        print ("                th") 
        print ("                {") 
        print ("                    background-color: #71b9d4;") 
        print ("                    border:1px solid white;") 
        print ("                    color:black;") 
        print ("                }") 
        print ("    </style>")
        print ("   <script type='text/javascript'>")
                 
        print ("    function mySubmit(op)")
        print ("            {")
                    
        print ("                document.getElementById('operacion').value = op;")
                    
        print ("           }")

        print ("       </script>")
                
        print ("       </HEAD>")
        print ("<BODY>")
        print ("    <CENTER>")
        print ("    <FORM method='GET' action='http://localhost/alumnos/cgi-bin/login.py'>")
        print ("        <input type='hidden' id='operacion' name='operacion' value='' />")
        print ("<table>")
        print ("<tr>")
        print ("                 <td> <input type='search' placeholder='Busque un nombre o parte de el' id='nombre' name='nombre' maxlength='70' required /> </td>")
        print ("                 <td>")                  
        print ("                  <input type='submit' value='Buscar' onclick=mySubmit('listNombre') />")
        print ("</td>")
        print ("</tr>")
        print ("</table>")
        print ("    </FORM>")
        print ("    </CENTER>")
       
        if len(listaAlumnos) == 0:
            
            print ("<div> No se han encontrado alumnos que coincidan con el patr&oacute<n buscado !!! </div>")
        
        else:
            print ("    <CENTER>")    
            print ("<font size='2' face='Verdana' >")        
            print ("<table width='700' > ")
            print ("<tr>")  
            print ("    <th> Legajo </th><th> Nombre </th><th> Sexo </th><th> Edad </th>")  
            print ("</tr>") 
                
            for alumno in listaAlumnos:
                print ("<tr>") 
                
                for atrubuto in alumno:
                    print ("    <td>" + atrubuto + "</td>")  
                                
                print ("</tr>") 
                    
            print ("</table>")
            print ("    </CENTER>")
            
        print ("</form>")
        print ("</BODY>")
        print ("</HTML>")
        
    @classmethod
    def lista_filtro_edad(self, listaAlumnos):
        print ("Content-type:text/html\r\n\r\n")
        
        print ("<!DOCTYPE html>")
        print ("<HTML><HEAD><TITLE>Busqueda Alumnos</TITLE>")
        print ("    <style>")
        
        print ("                table") 
        print ("                {") 
        print ("                    border-collapse:collapse;") 
        print ("                }") 
        print ("                tr:nth-child(3)") 
        print ("                {") 
        print ("                    background-color: #eef2f3;") 
        print ("                    color:black;") 
        print ("                }") 
        print ("                td") 
        print ("                {") 
        print ("                    border:1px solid white;") 
        print ("                }") 
        print ("                th") 
        print ("                {") 
        print ("                    background-color: #71b9d4;") 
        print ("                    border:1px solid white;") 
        print ("                    color:black;") 
        print ("                }") 
        print ("    </style>")
        print ("   <script type='text/javascript'>")
                 
        print ("    function mySubmit(op)")
        print ("            {")
                    
        print ("                document.getElementById('operacion').value = op;")
                    
        print ("           }")

        print ("       </script>")
                
        print ("       </HEAD>")
        print ("<BODY>")
        print ("    <CENTER>")
        print ("    <FORM method='GET' action='http://localhost/alumnos/cgi-bin/login.py'>")
        print ("        <input type='hidden' id='operacion' name='operacion' value='' />")
        print ("<table>")
        print ("<tr>")
        print ("                 <td> Edad m&iacute;ninima: <input type='number' min='1' max='99'  id='minEdad' name='minEdad' required  /> Edad m&aacute;ninima: <input type='number' min='1' max='99'  id='maxEdad' name='maxEdad' required  /> </td>")
        print ("                 <td>")                  
        print ("                  <input type='submit' value='Buscar' onclick=mySubmit('listEdad') />")
        print ("</td>")
        print ("</tr>")
        print ("</table>")
        print ("    </FORM>")
        print ("    </CENTER>")
       
        if len(listaAlumnos) == 0:
            
            print ("<div> No se han encontrado alumnos que coincidan con el patr&oacute<n buscado !!! </div>")
        
        else:
            print ("    <CENTER>")    
            print ("<font size='2' face='Verdana' >")        
            print ("<table width='700' > ")
            print ("<tr>")  
            print ("    <th> Legajo </th><th> Nombre </th><th> Sexo </th><th> Edad </th>")  
            print ("</tr>") 
                
            for alumno in listaAlumnos:
                print ("<tr>") 
                print ("    <td>" + alumno[0] + "</td>") 
                print ("    <td>" + alumno[1] + "</td>") 
                print ("    <td>" + alumno[2] + "</td>") 
                print ("    <td>" + alumno[3] + "</td>")
                print ("</tr>") 
                    
            print ("</table>")
            print ("    </CENTER>")
            
        print ("</form>")
        print ("</BODY>")
        print ("</HTML>")