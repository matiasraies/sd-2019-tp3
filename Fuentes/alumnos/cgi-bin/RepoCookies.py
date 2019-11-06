
#!/usr/bin/python3

import csv
import random


class RepoCookies:

    @classmethod
    def new_cookie(self, legajo):
        
        newCookie = random.randint(1000000000, 9000000000)
           
        RepoCookies.guardar_cookie(newCookie, legajo)
        return  newCookie   

    @classmethod
    def borrar_cookie(self, cookie):
        line = list()
        
        with open('RepoCookies.csv', 'r') as readFile:

            reader = csv.reader(readFile)

            for row in reader:
                if not row[0] == cookie:
                    line.append(row)
            
        with open('RepoCookies.csv', 'w') as writeFile:

            writer = csv.writer(writeFile)
            writer.writerows(line)
            
    @classmethod
    def guardar_cookie(self, cookie, legajo):

        myData = [cookie, legajo]              
                               
        myFile = open('RepoCookies.csv', 'a')
        with myFile:
                
            writer = csv.writer(myFile)            
            writer.writerow(myData)
        myFile.close()
       
    @classmethod
    def get_cookie_data(self, cookie):

        result = ""
        
        with open('RepoCookies.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            
            for row in reader:
                if row[0] == cookie:
                    result = row[1]
                    
            csv_file.close()
            
        return result     