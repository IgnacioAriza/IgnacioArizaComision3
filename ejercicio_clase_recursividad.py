# ejercicio clase recursividad 

#Ejercicio 1

from random import randint

def maze (time_):
    path = randint(1,3)
    if path == 1:
        time_ += maze(0)
        time_ += 3
        return time_
    if path == 2:
        time_ += maze(0)
        time_ += 5
        return time_
    if path == 3:
        time_ += 7
        return time_

final_time = maze(0)

print("El tiempo final en minutos fue: " , final_time)

#Ejercicio 2
#La funcion devuelve el numero entero invertido, por ejemplo convierte 15569 en 96551