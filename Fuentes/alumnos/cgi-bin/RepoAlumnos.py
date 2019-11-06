#!/usr/bin/python3

import csv


class RepoAlumnos:
    
    @classmethod
    def borrar_alumno(self, legajo):
        line = list()
        
        with open('RepoAlumnos.csv', 'r') as readFile:

            reader = csv.reader(readFile)

            for row in reader:
                if not row[0] == legajo:
                    line.append(row)
            
        with open('RepoAlumnos.csv', 'w') as writeFile:

            writer = csv.writer(writeFile)
            writer.writerows(line)
            
    @classmethod
    def guardar_alumno(self, legajo, nombre, sexo, edad, pwd):

        myData = [legajo, nombre, sexo, edad, pwd]              
        
        RepoAlumnos.borrar_alumno(legajo)
                       
        myFile = open('RepoAlumnos.csv', 'a')
        with myFile:
                
            writer = csv.writer(myFile)            
            writer.writerow(myData)
        myFile.close()
       
    @classmethod
    def existe_alumno(self, legajo):

        existe = False
        
        with open('RepoAlumnos.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            
            for row in reader:
                if row[0] == legajo:
                    existe = True
            csv_file.close()
        return existe        
    
    @classmethod
    def validarUsuario(self, legajo, pwd):

        result = False
        
        if RepoAlumnos.existe_alumno(legajo):
            with open('RepoAlumnos.csv', 'r') as csv_file:
                reader = csv.reader(csv_file)
            
                for row in reader:
                    if row[0] == legajo:
                        if row[4] == pwd:  
                            result = True                  
        
        return result
     
    @classmethod
    def get_alumno(self, legajo):

        results = []
        if RepoAlumnos.existe_alumno(legajo):
            
            with open('RepoAlumnos.csv', 'r') as csv_file:
                reader = csv.reader(csv_file)
            
                for row in reader:
                    if row[0] == legajo:
                        results.append(row[0])
                        results.append(row[1])
                        results.append(row[2])
                        results.append(row[3])
                        results.append(row[4])                     
                        return results            
                        
        else:
            raise Exception('ATENCION ! El nro. de legajo no existe. ')    
    
    @classmethod
    def lista_alumnos_nombre(self, patronBusqueda):

        line = list()
        
        with open('RepoAlumnos.csv', 'r',) as readFile:

            reader = csv.reader(readFile)

            for row in reader:   
                
                if patronBusqueda is None or patronBusqueda == "":
                    line.append(row[:-1])           
                elif patronBusqueda.upper() in row[1].upper():
                    line.append(row[:-1])
                    
        return line
    
    @classmethod
    def lista_alumnos_rango_edad(self, minEdad, maxEdad):

        line = list()
        
        if minEdad is None or minEdad == "":
            minEdad = 0
            
        if maxEdad is None or maxEdad == "":   
            maxEdad = 150
        
        with open('RepoAlumnos.csv', 'r',) as readFile:

            reader = csv.reader(readFile)

            for row in reader:   
                
                if int(maxEdad) >= int(row[3])  and int(minEdad) <= int(row[3]):      
                    line.append(row)
                    
        return line