def dictionary_phrase(fhrase): #entrego una frase 
        fhrase=fhrase.split() #lo separa segun los espacio y lo mando a una lista 
        dictionary={}
        for i in range(len(fhrase)):#en diccionario guardo la frase separada por espacios usando la palabra como key y el tamaño como dato
            dictionary[fhrase[i]]=[len(fhrase[i])]
           
        return dictionary 


def multiple(number_first_, number_second_):# veo si los numeros ingresados son multiplos 
    if (number_second_ % number_first_) == 0:
        return True
    else:
        return False

def average_temp(minimum_,maximum_):#saco la media de 2 numeros 
    return (minimum_ + maximum_) / 2

def separate(messenge_):#separao con espacios un string 
    answer = " ".join(messenge_)
    return answer


#EJERCICIO 7

def max_min(number_list, list_length):      #Encuentra el mayor y el menor número en la lista
    max =  number_list[0]
    min =  number_list[0]
    for i in range(list_length):
        if ( number_list[i] > max):
            max =  number_list[i]
        elif ( number_list[i] < min):
            min =  number_list[i]
    return [max, min]

#EJERCICIO 8

def area_perimeter(radio, pi):      #Calcula el área y el perímetro de la circunferencia
    area = (radio**2) * pi
    print("El area de la circunferencia es: " + str(area))
    perimeter = (2*pi)*radio
    print("El perímetro de la circunferencia es: " + str(perimeter))
    return

#EJERCICIO 9

def login(user_name, password, attempt):    #Comprueba si el nombre de usuario y contraseña son correctos
    if (user_name == "usuario1" and password == "asdasd"):
        answer = True
    else:
        answer = False
        attempt = attempt + 1
    return answer, attempt

#EJERCICIO 10

def total_price(products, discounts):       #Calcula el total a pagar con descuentos
    total = 0
    for product, price in products.items():
        if (product in discounts):
         item_discount = discounts[product]
         item_price = price - (price * item_discount / 100)
         total = total + item_price
        else:
           total = total
    return total

#EJERCICIO 11
def double(numbers):        #Esta función nos da el doble de cada número de la lista de números.
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2
    return numbers

def result(double, numbers):    #Esta función envía la lista de números a la función "double" la cual nos duplicará los números de la lista. Luego, esta función creará una lista nueva para guardar los resultados que reciba de la función "double".
    new_list = []
    new_list = double(numbers)
    return new_list

def modulo_vector(vector):#saca el modulo de un vector 
    modulo_cuadrado = sum(x**2 for x in vector)
    modulo = modulo_cuadrado ** 0.5
    return modulo

#ejer 17 y 16
def prime(number_):# ver si es primo o no (number=int)
    if((number_%2)!=0 and (number_%3)!=0 and (number_%5)!=0 or number_==2 or number_==3):
        return True
    else:
        return False

def primadd(number): # suma digitos de un numero number= (int)
    number_=number
    aux=0
    sum=0
    while(number_>0):
        aux=int(number_%10)
        sum+=aux
        number_/=10
        
    return sum
                   
def busdig(dig_,number_):#La cantidad de veces q sale el digito",dig," busting contiene (int,int)
    con=0              
    for i in str(number_):
        if (i==str(dig_)):
            con+=1
    return con

def factorial(number_): #saca el factorial de un numero ingresado (number_=int)
    if (number_==1):
        return 1
    elif(number_==2):
        return 2   
    else:
        return (number_*factorial(number_-1))
    


#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
 


def dni_number(dni_): #
    if len(dni_) >= 7 and len(dni_) <=8:
        if dni_.isdigit() == True:
            return True
        else:
            return False
    else:
        return False


def surname(name_surname_):
    splitname = name_surname_.split()
    return splitname[len(splitname)-1]


def first_name(name_surname_):
    splitname = name_surname_.split()
    return splitname[0]


def last_three(dni_):
    return (dni_[len(dni_)-3]+dni_[len(dni_)-2]+dni_[len(dni_)-1])    