from tp5_fun import *

#Ejercicio 1
dni = input("Ingrese su numero de dni: ")
print(dni_number(dni))





#Ejercicio 2
name_surname = input("Ingrese su nombre y apellido: ")
aux = surname(name_surname)
print(aux)



#Ejercicio 3
# les doy valores que seran sobreescriptos despues para que puedan iniciar los bucles
dni = "1"
# le doy un string vacio a final_id para poder sumarle los resultados despues
final_id = ""
#un bucle infinito que va a salir con break
while True:
    #pido el nombre que vamos a usar
    print("Igresando socios para el club")
    print("Ingrese el nombre o nombres del socio y su primer apellido.\nIngrese solo un apellido.\nNo ingrese nada para terminar de ingresar socios.")
    name_surname = input()
    #si no se ingresa un nombre se sale del bucle con break
    if name_surname == "":
        break
    #uso una funcion que revisa si el dni es un numero valido, si no es lo pido de vuelta
    while dni_number(dni) != True:
        dni = input("Ingrese un DNI valido: ")
    #uso funciones para conseguir las partes que necesito del nombre y del dni y las concateno en final_id
    final_id += first_name(name_surname)
    final_id += str(len(surname(name_surname)))
    final_id += last_three(dni)
    #imprimo la respuesta y preparo para empezar el bucle de nuevo
    print("Su ID es: ", final_id)
    final_id += "\n"
    name_surname = "placeholder"
    dni = "1"
   
#si se generaron IDs los muestra todos aca
if final_id != "":
    print("Los IDs son:\n", final_id)

#ejercicio 4
number_first = int(input("Ingrese un numero: "))
number_second = int(input("Ingrese un segundo numero: "))
i = multiple(number_first,number_second)
if i == True:
    print(number_first , " es multiplo de ", number_second)
else:
    print(number_first, " no es multiplo de ", number_second)

#ejercicio 5
days_amount = int(input("Ingrese la cantidad de dias que se van a ingresar: "))
for i in range(days_amount):
    minimum = int(input("Ingrese la minima temperatura del dia: "))
    maximum = int(input("Ingrese la maxima temperatura del dia: "))
    print("La temperatura media es: ", average_temp(minimum,maximum))
    

#ejercicio 6
messenge = input("Ingrese un mensaje para separar con espacios: ")
print(separate(messenge))

#EJERCICIO 7

list_length = int(input("Ingrese el tamaño de la lista: "))
number_list = []
answer_list = []
for i in range(list_length):
    number = int(input("Ingrese un número: "))
    number_list.append(number)
answer_list = max_min(number_list, list_length) #Encuentra el mayor y el menor número en la lista
print("El mayor número de la lista es " + str(answer_list[0]))
print("El menor número de la lista es " + str(answer_list[1]))


#EJERCICIO 8

import math
radio = int(input("Ingrese el radio de la circunferencia: "))
pi = math.pi
area_perimeter = area_perimeter(radio, pi)  #Calcula el área y el perímetro de la circunferencia

#EJERCICIO 9

attempt = 0
while (True):
    user_name = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    answer, attempt = login(user_name, password, attempt)   #Comprueba si el nombre de usuario y contraseña son correctos
    if (answer == True):
        print("Nombre de usuario y contraseña correcta.")
        print("Bienvenido, " + user_name)
        break
    else:
        print("Ha ingresado datos erroneos.")
        print("Intento # " + str(attempt) + ". Inténtelo de nuevo.")

#EJERCICIO 10

products = {"product1": 500, "product2": 1500, "product3": 700, "product4": 2380, "product5": 5400}
discounts = {"product1": 10, "product2": 50, "product3": 20, "product4": 25, "product5": 70}
total = total_price(products, discounts)        #Calcula el total a pagar con descuentos
print("El total a pagar es de: $" + str(total)) 

#EJERCICIO 11

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista original: ")
print(numbers)
numbers = result(double, numbers)   #Esta función recibe otra función y una lista. La otra función nos da el doble de cada número en la lista. Esta función guarda cada resultado en una lista.
print("Nueva lista:")
print(numbers)



#Ejer 12

phrase=input("ingresar frase: ")
dictionary=dictionary_phrase(phrase)
print(dictionary)

#Ejer 13
vector = (3, 4)#devino el vector
modulo = modulo_vector(vector)#saco el modulo 
print(f"El módulo del vector {vector} es {modulo}")



#Ejer 14
number=int(input("Ingresar numero para ver si es o no primo. "))

if(prime(number)):
    print("El numero",number,"es primo")
else:
    print("El numero",number,"no es primo")    

#Ejer 15
aux=0
while True:
    print("A) Buscar factorial")
    print("B) Salir")
    option=input().lower()
    if option=="a":
        print("ingresar numero")
        number=int(input())
        aux+=1
        print("El factorial del numero",number,"es:",factorial(number))

    elif(option=="b"):
        break    
if(aux>0):
    print("la cantidad de numeros ingresados es de",aux)
#Ejer 16

print("ingresar un numero entero")
number=int(input())
print("ingresa un digito para ver cuantas veces aparece en el numero anteriormente ingresado")
dig=int(input())

print("La cantidad de veces que aparece el digito",dig,"en el numero",number,"es de:",busdig(dig,number),"veces")

#ejer 17

maxx=0
while(True):
    print("ingresar numero primo")
    number=int(input())
    iss=prime(number)
    if(iss>maxx):
        maxx==iss
    if (iss==False):
        break
    else:
        
        dig=input("ingresar un digito para ver cuantas veces aparece en el numero ingresado: ")
        print("la suma de sus digitos es:",primadd(number))
        print("La cantidad de veces q sale el digito",dig," es de:",busdig(dig, number))
        print("El factorial del mayor numero ingresado que es",maxx,"es de:",factorial(maxx))





