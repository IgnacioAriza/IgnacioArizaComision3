#EJERCICIO 1
 
numbers = []    #Creamos la lista vacía.
while (True):
	print("Agregará números en una lista. Ingrese 0 para salir.")
	answer = int(input("Ingrese un número: "))  #Le pedimos al usuario que ingrese números.
	if (answer == 0):       #Si ingresa el 0, se termina el ciclo y no se piden más números.
    	print("Programa Finalizado.")
    	break
	else:
    	numbers.append(answer)  #Los números ingresados se guardan en la lista.
 
print("Los números que ingresó: ", numbers) #Mostramos los números por pantalla.
 
 
#EJERCICIO 2
 
delete = int(input("¿Qué número desea borrar de la lista?: "))  #Pedimos al usuario un número para borrar de la lista.
if (delete in numbers):
	numbers.remove(delete)  #Si el número está en la lista, se borra.
	print("El número ", delete, " ha sido borrado de la lista.")
else:
	print("No fue posible eliminar el número ", delete, " ya que no se encontró en la lista.")  #Si no está en la lista, le avisamos al usuario.
print("Su lista de números: ", numbers)
 
 
#EJERCICIO 3
 
addition = 0
for i in range(len(numbers)):
	addition = addition + numbers[i]	#Sumamos cada número de la lista
print("La suma de todos los números de la lista es igual a: ", addition)	#Mostramos el resultado por pantalla.
 
 
#EJERCICIO 4
 
numbers2 = []   	#Creamos una nueva lista.
print("Ahora crearemos una nueva lista que incluirá todos los números que ingresó que sean menores a X")
numberx = int(input("Ingrese el valor de X: ")) #Le pedimos al usuario que ingrese un número.
for i in range(len(numbers)):
	if (numbers[i] < numberx):
    	numbers2.append(numbers[i]) 	#Los números de la lista original que sean menores al número del usuario, se guardan en la nueva lista.
print("Los valores de la nueva lista: ", numbers2)
 
 
#EJERCICIO 5
 
print("A continuación se creará una lista de tuplas con cada número de la lista y la cantidad de veces que aparece.")
unique_numbers = set(numbers)   #Creamos un conjunto con las números de la lista orignal. Los números no estarán repetidos.
list_tuples = []    #Creamos una lista nueva.
for number in unique_numbers:
	list_tuples.append((number, numbers.count(number)))     #Guardaremos una tupla con el número del conjunto y la cantidad de veces que aparece en la lista original.
print("La nueva lista: ", list_tuples)  #Mostramos por pantalla la lista de tuplas.
 
 
#EJERCICIO 6
 
primary_students = []   	#Creamos las listas para alumnos de nivel primario y otra para los del secundario
highschool_students = []
while (True):
	answer = input("Ingrese el nombre de un alumno de nivel primario: ") #El usuario ingresa los nombre de los alumnos.
	if (answer == "x"):
    	break       #Cuando ingrese "x" se termina el ciclo y ya no se le piden nombres.
	else:
    	primary_students.append(answer)     #Los nombres se guardan en la lista correspondiente.
 
while (True):
	answer = input("Ingrese el nombre de un alumno de nivel secundario: ")
	if (answer == "x"):
    	break
	else:
    	highschool_students.append(answer)
 
p_students = set(primary_students)      #Creamos un conjunto para cada lista para que no hayan nombres repetidos.
h_students = set(highschool_students)
print("Alumnos del nivel primario sin repeticiones: ", p_students) #Imprimimos los conjuntos de nombres.
print("Alumnos del nivel secundario sin repeticiones: ", h_students)
 
repeated_names = []     	#Creamos 2 listas. Una para los nombres repetidos y otra para los que no se repiten.
not_repeated_names = []
 
repeated_names = p_students & h_students   #Si el nombre se repite en ambos conjuntos, se guarda en la lista.
not_repeated_names = p_students - h_students   #En esta lista se guardan los nombres de nivel primario que no se repiten en el secundario.
 
print("Los nombres de alumnos que se repiten en nivel primario y secundario: ", repeated_names)    #Imprimimos ambas listas.
print("Los nombres de alumnos que sólo están en nivel primario: ", not_repeated_names)
 
 
#EJERCICIO 7
 
messages = []   	#creamos las listas y el diccionario
letter_list = []
letters = {}
for i in range(2):
	answer = input("Ingrese una letra o un mensaje: ")  #El usuario ingresa un mensaje y se guarda en la lista.
	messages.append(answer)
 
for string in messages:         #Guardamos en otra lista cada caracter ingresado por el usuario de la lista original.
	for word in string:
    	for letter in word:
        	letter_list.append(letter)
 
for letter in letter_list:  	#Eliminamos los espacios en blanco. Nos quedamos solo con las letras.
	if (letter == " "):
    	letter_list.remove(" ")
 
for letter in letter_list:      #En un diccionario guardamos cada letra como clave y le asignamos como valor el número de veces que se ingresó.
	letters.update({letter:letter_list.count(letter)})
print(letters)
 
 
#EJERCICIO 8
 
#Creamos unaa matriz. En ella se pondrá cuántos goles le hizo cada equipo a los demás.
 
goals = []  #Creamos la matriz.
 
for i in range(10):
	rows = []   #Se creará una lista para cada fila. Habrá una fila y una columna por cada equipo.
	for j in range(10):
    	if (i == j):   	#Cuando coincida el número de fila y de columna, se rellenará el lugar con un "0".
        	rows.append(0)
    	else:
        	print("¿Cuántos goles le hizo el equipo ", (i+1), " al equipo ", (j+1), "?: ")
        	answer = int(input("Respuesta: "))  #En los demás lugares, el usuario ingresará un valor que se guarda en una fila.
        	rows.append(answer)
	goals.append(rows)  #Agregamos cada fila a la matriz.
 
for i in range(10): #Mostraremos los resultados de cada partido.
	print("Equipo #", (i+1), ":")
	points = 0
	for j in range(10):
    	if (i == j):	#Cuando coincida el número de fila y columna (hablamos de un solo equipo), se saltea.
        	continue
    	else:
        	if (goals[i][j] > goals[j][i]): 	#Mostramos si el equipo ganó, perdió o empató y la diferencia de goles.
            	print("...contra Equipo #", (j+1), ": GANADO")
            	print("El equipo #", (i+1), " ganó por una diferencia de ", (goals[i][j] - goals[j][i]), " goles")
  	          points = points + 1 	#El equipo recibe un punto por cada victoria.
        	elif (goals[i][j] < goals[j][i]):
            	print("...contra Equito#", (j+1), ": PERDIDO")
            	print("El equipo #", (i+1), " perdió por una diferencia de ", (goals[j][i] - goals[i][j]), " goles")
        	else:
            	print("...contra Equito#", (j+1), ": EMPATADO")
	print("Cantidad de puntos: ", points)   #Mostramos cuántos puntos tiene cada equipo.
	print("Se da un punto por cada partido ganado.")
 
 
#EJERCICIO 9
 
#Se creará un juego de la memoria.
def printing1(row1, row2, column1, column2, game, coded):
	for i in range(4):  	#Se mostrará el número en la ubicación que dio el usuario.
    	for j in range(4):  #En los demás lugares se muestra la lista codificada con "x" y con los números adivinados.
        	if ((i == row1 and j == column1) or (i == row2 and j == column2)):
            	print(game[i][j], "   ", end="")
        	else:
            	print(coded[i][j], "   ", end="")
    	print("\n")
 
game = [[3, 5, 5, 3], [7, 4, 2, 1], [6, 6, 2, 7], [8, 4, 1, 8]] #Se crea matriz con los pares de números desordenados.
coded = [["x", "x", "x", "x"], ["x", "x", "x", "x"], ["x", "x", "x", "x"], ["x", "x", "x", "x"]] #Se crea la misma lista codificada, en vez de números tiene "x"
points = 0
print("Bienvenido al juego de la memoria.")
print("Debes encontrar pares iguales.")
print("El juego tiene 4 filas y 4 columnas.")
print("Se ve así:")
for i in range(4):  	#Se imprime el tablero solo con cruces.
	for j in range(4):
    	print("x   ", end="")
	print("\n")
 
while(True):
	while(True):
    	row1 = int(input("Ingrese la FILA: "))  	#Pedimos al usuario que ingrese la ubicación del primer número.
    	column1 = int(input("Ingrese la COLUMNA: "))
    	if (row1 != 1 and row1 != 2 and row1 != 3 and row1 != 4):
        	print("Número de Fila incorrecto. Ingrese un número del 1 al 4.")
    	elif (column1 != 1 and column1 != 2 and column1 != 3 and column1 != 4):
        	print("Número de Columna incorrecto. Ingrese un número del 1 al 4.")	#Si no ingresa ingresa un valor válido, se le pedirá que ingrese los datos nuevamente.
    	else:
        	row1 = row1 - 1
        	column1 = column1 - 1
        	number1 = game[row1][column1]
        	print("El número elegido es el: ", number1)
        	printing1(row1, row1, column1, column1, game, coded)    #Luego llamamos a la función que mostrará el número en la posición que eligió.
        	break
	while (True):   
    	row2 = int(input("Ingrese la FILA: "))      	#Pedimos la ubicación del segundo número.
    	column2 = int(input("Ingrese la COLUMNA: "))
    	if (row2 != 1 and row2 != 2 and row2 != 3 and row2 != 4):
        	print("Número de Fila incorrecto. Ingrese un número del 1 al 4.")
    	elif (column2 != 1 and column2 != 2 and column2 != 3 and column2 != 4):
        	print("Número de Columna incorrecto. Ingrese un número del 1 al 4.")	#Si ingresa un número no valido, deberá volver a ingresar los datos.
    	else:
        	row2 = row2 - 1
        	column2 = column2 - 1
        	number2 = game[row2][column2]
        	print("El número elegido es el: ", number2)
        	printing1(row1, row2, column1, column2, game, coded)    #Se llama a la función que muestra el tablero con el primer número y el segundo número que eligió.
        	break
	if (number1 == number2):     #Si encuentra dos números iguales, gana un punto.
    	print("¡Muy bien, encontraste un par!")
    	coded[row1][column1] = number1  #Guardamos los números adivinados en su lugar de la lista codificada
    	coded[row2][column2] = number2  #de este modo siempre se mostrarán en el tablero.
    	points = points + 1
    	if (points == 8):   #Al adivinar todos los números se termina el juego.
        	break
print("Felicidades. Ganaste.")
 
 
#EJERCICIO 10
 
matrix = [[1,2,3], [4, 5, 6], [7, 8, 9]]	#Creamos una matriz cuadrada y las listas para las diagonales.
diagonal = []
reverse = []
 
for i in range(3):  #Con un ciclo for mostramos la matriz.
	for j in range(3):
    	print(matrix[i][j], end="")
	print("\n")
 
for i in range(3):  	#Con un ciclo for obtenemos la diagonal (cada vez que i sea igual a j) y la guardamos en la lista.
	for j in range(3):
    	if (i == j):
        	diagonal.append(matrix[i][j])
 
print("La diagonal de la matriz cuadrada es: ", diagonal)   #Imprimimos la diagonal.
 
i = len(matrix) - 1
 
while (i >= 0):         	#Con un ciclo while recorremos la matriz desde el final hasta el principio
	j = len(matrix) - 1     #y obtenemos la diagonal al revés (cuando i es igual a j) y la guardamos en una lista.
	while (j >= 0):
    	if (i == j):
        	reverse.append(matrix[i][j])
    	j = j - 1
	i = i - 1
print("La diagonal inversa de la matriz cuadrada es: ", reverse)	#Imprimimos la diagonal inversa.
 
 
#EJERCICIO 11
 
money_dictionary = {"EURO":"€", "DOLLAR":"$", "YEN":"¥"}   #Creamos el diccionario con divisas
money = input("Ingrese una divisa: ").upper()   #El usuario ingresa la divisa
 
if money in money_dictionary:       #Se busca la divisa en el diccionario.
	symbol = money_dictionary[money]       #Se guarda el símbolo de la divisa.
	print("El símbolo de " + money + " es " + symbol)   #Si está le mostramos el símbolo.
else:
	print("La divisa ingresada no está en el diccionario.") #Si no se encontró la divisa, le avisamos al usuario.
 
 
#EJERCICIO 12
 
information = {}    #Creamos el diccionario vacío.
name = input("Ingrese su nombre: ") 	#Le pedimos al usuario que ingrese su información.
information.update({"nombre":name})     #Agregamos al diccionario una clave y el valor agregado por el usuario.
age = input("Ingrese su edad: ")
information.update({"edad":age})
address = input("Ingrese su dirección: ")
information.update({"dirección":address})
phone = input("Ingrese su teléfono: ")
information.update({"teléfono":phone})  #Luego mostramos toda la información del diccionario.
print(information["nombre"], " tiene ", information["edad"], " años. Vive en ", information["dirección"], ". Y su número de teléfono es ", information["teléfono"] )
 
 
#EJERCICIO 13
 
fruits_prices = {"MANZANAS":100, "BANANAS":200, "PERAS":250, "FRUTILLAS":500, "NARANJAS":150}    #Creamos el diccionario con las frutas y sus precios.
print("¿De qué fruta desea conocer el precio?")
fruit = input("Ingrese el nombre en plural: ").upper()   #El usuario ingresa una fruta.
if fruit in fruits_prices:      #Con un ciclo for buscamos la fruta en el diccionario.
	price = fruits_prices[fruit]    #Si la fruta está en el diccionario, guardamos el precio en la variable price.
	print("El kilo de ", fruit.lower(), " cuesta $", price)  #Mostramos el precio por la terminal.	
else:
	print("La fruta ingresada no está en el diccionario.")  #Si la fruta no está en el diccionario, lo avisamos por la terminal.