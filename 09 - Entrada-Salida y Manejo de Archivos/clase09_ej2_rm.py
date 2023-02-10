""" Reciba como un valor de temperatura en grados centígrados, un valor de humedad y por último si llovio (Con True o False).
    Y que cada vez que sea invocado, cargue en el archivo provisto "clase09_ej2.csv" una marca de tiempo y esa información.
"""

import sys
from datetime import date, time, datetime 
   
if (len(sys.argv) == 4):
    grados  = sys.argv[1]
    humedad = sys.argv[2]
    lluvia  = sys.argv[3]

    d = datetime.now()
    objeto_datetime = d.strftime('%d-%m-%Y %H:%M:%S')

   # marca_de_tiempo = d.fromtimestamp(objeto_datetime)


    archivo = open('clase09_ej2_rm.csv','w')
    
    archivo.write(str(objeto_datetime) + '\n')
    archivo.write(grados + '\n')
    archivo.write(humedad + '\n')
    archivo.write(lluvia + '\n')
    
    archivo.close
else:
    print('Error debe ingresar 3 paràmetros.')
