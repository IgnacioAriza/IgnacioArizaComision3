#tp3

#Ejercicio 1


word = input("Ingrese una palabra: ")


for k in range(10):


 print(word)


#Ejercicio 2


age = int(input("Ingrese su edad: "))


for i in range(age):


    print(i + 1)


#Ejercicio 3


num = int(input("Ingrese un numero entero positivo: "))


for i in range(num):


 if (i % 2 != 0):
 
  print(i, end= ", " )


#Ejercicio 4


num = int(input("Ingrese un numero positivo: "))


for i in range(num, -1, -1):


 print(i, end=", ")


#Ejercicio 5


inv = int(input("Ingrese la cantidad que inversinó: "))


anual_interest = int(input("Ingrese su interés anual en $: "))


years = int(input("Ingrese la cantidad de años que durará la inversión: "))


for i in range(years):


    inv = inv + anual_interest;


    print("Su inversión generó: ", anual_interest )


    print("---------------------------")


print("El dinero total que recaudó con esa inversión fue de: ", inv)


#Ejercicio 6


num= int(input("Ingrese un numero entero: "))


for i in range(1, num + 1):
       
  print('*' * i)


#Ejercicio 7


print("TABLAS DE MULTIPLICAR: ")


for i in range(11):
 
   for j in range(11):
 
    print(i, " x ", j ," = ", i*j)




   print("--------------")


#Ejercicio 8


num = int(input("Ingrese un numero entero: "))


num_impares = num if num % 2 != 0 else num - 1


for i in range(num_impares, 0, -2):
 
 for j in range(i, num_impares + 1, 2):
     
     print(j, end=" ")
     
 print()


 #Ejercicio 9


 
password = input("Ingrese una contraseña, esta se guardara y tendra que ingresarla después: ")
exit = False


while exit == False:


 tried = input("Ingrese su contraseña: ")


 if(tried != password):
 
  print("Su contraseña es incorrecta, intentalo nuevamente")


 elif(tried == password):
   
      exit = True


print("Ha accedido al sistema")


#Ejercicio 10
number1 = int(input("Ingrese un numero entero positivo: "))
counter = 1
divisor = 0
if (number1 == 0 or number1 < 0):
    print("Debe ingresar un numero mayor a 0")
else:
    while counter <= number1:
        if (number1 % counter == 0):  
            divisor = divisor + 1
            counter = counter + 1
        else:
            counter = counter + 1
    if (divisor == 2):
        print(f"El número {number1} es primo")
    else:
        print(f"El número {number1} no es un número primo")


#Ejercicio 11
palabra = input("Ingrese una palabra: ")
largo1 = len(palabra)
largo2 = largo1
alreves = ""


for i in range(largo1):
    largo2 = largo2 - 1
    letra = palabra[largo2]
    alreves = alreves + letra
print(alreves)

#Ejercicio 12
phrase = str(input("Escriba una frase: "))
letter = str(input("Escriba una letra: "))
counter = 0

for i in range(len(phrase)):
    if (letra == phrase[i]):
        counter = counter + 1

print(counter)

#Ejercicio 13

val = "oh yeah"

while (val == "oh yeah"):
  phrase = input("Escriba algo o escriba salir para salir: ")
  if (phrase == "salir"):
    val = "Oh no"
    print("Saliendo")

#Ejercicio 14
number_1 = int(input("Ingrese un primer nùmero: "))
number_2 = int(input("Ingrese un segundo nùmero: "))

bigger = number_1
smaller = number_2

if (number_2 > bigger):
  bigger = number_2
  smaller = number_1

while (smaller < bigger):
  if (smaller % 2 != 0):
    print(f"{smaller} es impar")
  else:
    print(f"{smaller} es par")
  smaller = smaller + 1

#Ejercicio 15


number1 = int(input("Ingrese un número entero positivo: "))
counter = 1
if (number1 == 0 or number1 < 0):
    print("Debe ingresar un número mayor a 0.")
else:
    print(f"Los siguientes números son divisores de {number1}:")
    while counter <= number1:
        if (number1 % counter == 0):  
            print(counter)
            counter = counter + 1
        else:
            counter = counter + 1



#Ejercicio 16
numbers = int(input("¿Cuantos nameros va a introducir? "))

counter = 0

for i in range(numbers):
  number = int(input(f"Ingrese el {i+1}º  nùmero: "))
  if (number < 0):
    counter += 1

print(f"Introdujo {counter} nùmeros negativos")


#Ejercicio 17
phrase = input("Ingrese una frase: ")
used1 = 0
used2 = 0
used3 = 0
used4 = 0
used5 = 0
vowels = ""
large = len(phrase)
print("Las siguientes vocales están en su frase: ")
for i in range(large):
    if (phrase[i] == "a" and used1 == 0):
        vowels = vowels + phrase[i] + ", "
        used1 = used1 + 1
    elif (phrase[i] == "e" and used2 == 0):
        vowels = vowels + phrase[i] + ", "
        used2 = used2 + 1
    elif (phrase[i] == "i" and used3 == 0):
        vowels = vowels + phrase[i] + ", "
        used3 = used3 + 1
    elif (phrase[i] == "o" and used4 == 0):
        vowels = vowels + phrase[i] + ", "
        used4 = used4 + 1
    elif (phrase[i] == "u" and used5 == 0):
        vowels = vowels + phrase[i] + ", "
        used5 = used5 + 1
print(vowels)

#Ejercicio 18
last_number_1 = 0
last_number_2 = 1

print("0, 1", end="" + ", ")

for i in range(10):
  fibo = last_number_1 + last_number_2
  if (i != 9):
    print(fibo, end="" + ", ")
  else:
    print(fibo, end="")
  last_number_1 = last_number_2
  last_number_2 = fibo

#Ejercicio 19
piggy_bank = int(input("¿Cuánto dinero quieres ahorrar?: $"))
money2 = 0
while money2 < piggy_bank:
    money1 = int(input("¿Cuánto dinero guardarás?: $"))
    if (money1 < 0):
        print("No se admiten números negativos.")
    money2 = money2 + money1
print(f"¡Lograste tu objetivo! Ahorraste ${money2}")

#Ejercicio 20
val = "oh yeah"
add = 0

while (val == "oh yeah"):
  number = int(input("Ingrese un nùmero: "))
  if (number == 0):
    val = "oh no"
  else:
    add += number 

print("Sumatoria: ",add)

#Ejercicio 21

val = "oh yeah"
bigger = 0

while (val == "oh yeah"):
  number = int(input("Ingrese un nùmero positivo: "))
  if (number == 0):
    val = "oh no"
  elif (number > bigger):
    bigger = number

print("Mayor: ",bigger)


#Ejercicio 23, 24

cost = input("Ingrese el monto de la compra o ingrese 0 para terminar ")
cost = int(cost)
totalcost = 0
while cost != 0:
    if cost < 0:
        cost = input("Por favor, ingrese un monto positivo ")
        cost = int(cost)
        continue
    totalcost = totalcost + cost
    cost = input("Ingrese el monto de la compra o ingrese 0 para terminar ")
    cost = int(cost)
   
if totalcost > 1000 :
    discount = totalcost/10
    totalcost = totalcost - discount
   
print("Su precio final es: $", totalcost)


#Ejercicio 25

numberfac = input("Ingrese un numero entero positivo para recibir su factorial: ")
numberfac = int(numberfac)
factorial = 1
for i in range(1,numberfac):
   factorial = factorial * i

print(factorial)
