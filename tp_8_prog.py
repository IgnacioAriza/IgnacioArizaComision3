#Ejercicio 1:
def count(n, d = 0):
   n = str(n)

   if len(n) != 1: count(int(n[:-1]), d + 1)
   else: print(f"Cantidad de Digitos: {d + 1}")

count(144445)


#ejercicio 2

def power(n,b):
    if(n==b):
        return True
    elif((n%b)!=0):
        return False
    else:
        return power((n/b),b)         


while True:
    print("buscar si n es potencia de b, ingresar 0 si se quiere salir")
    n=int(input("ingresar n: "))
    b=int(input("ingresar b: "))        
    if(n!=0 and b!=0):
        option=power(n,b)
        if option==True:
            print(n,"si es potencia de",b)
        else:
            print(n,"no es potencia de",b)    
    else:
        break    


#Ejercicio 3

def find_in (body_, sample_, start_, answer_list_):
    aux = body_.find(sample_,start_)
    if aux != -1:
      answer_list_.append(aux)
      find_in(body_,sample_,(aux + len(sample_)),answer_list_)
    return answer_list_

array_temp = []

print(find_in("scooby dooby doo","oo",0,array_temp))


#Ejercicio 4
def odd(number):
    if number==1:
        return "impar"
    elif(even(number-1)=="par"):
        return "impar"
    else:
        return even(number)    

def even(number):
    if (number==1):
        return odd(number)
    elif (odd(number-1)=="impar"):
        return "par"
    else:
        return odd(number)    

print("El numero 4 es ",even(4))        

#Ejercicio  5:
def max_list(list, pos = 0, max = 0):
   if pos > len(list) - 1:
      print(f"El mayor numero es: {max}")
   else:
      if list[pos] > max: max_list(list, pos + 1, list[pos])
      else: max_list(list, pos + 1, max)

array = [12, 46, 100, 525, 200]
max_list(array)

#Ejercicio 6:
def repeat(list, length, new_list = [], count = 0, pos = 0):
   if pos > len(list) - 1:
      print(f"Nuevo Arreglo: {new_list}")
   else:
      if count < length:
         new_list.append(list[pos])
         repeat(list, length, new_list, count + 1, pos)
      else:
         repeat(list, length, new_list, 0, pos + 1)

repeat(array, 2)

# Ejercicio 7: 
def sumatory(number, count):
   if count == 1: return number + 2
   else:
      return number + count * sumatory(number, count - 1)

number = int(input("Ingrese un numero: "))
number_count = int(input("Ingrese cantidad: "))

print(sumatory(number, number_count))


#Ejercicio 8:

def pascal(n, k):
    if (n==k):#si n y k son iguales retorna 1 porque cuando los valores se repiten esta al costado del triangulo
        return 1
    elif(n==0): #siempre q n=20 retorta 1 porque n=0 representa que estas a la izquierda del triangulo 
        return 1
    else:
        return pascal(n-1,k-1)+pascal(n,k-1) #sumo el pascal de las posiciones contiguas del numero que quiero sacar el pascal
      


print("El valor de columna 3 fila 5= ",pascal(3,5))      


#Ejercicio 9:


def combinations(lista, k, aux=""):#recibe la lista y longitud eje ["a","b","c"], 3
    if k == 0:
        print(aux)#muestra el string 
        return

    for character in lista:#en la primera vuelta recorre cada caracter ["a","b","c"] toma "a" 
        combinations(lista, k - 1, aux + character)#manda ["a","b","c"],2,"a" // en la segunda manda ["a","b","c"],1,"aa" (tambien con "ab", etc) // en la tercera manda ["a","b","c"],0,"aaa"
    

characters = ['a', 'b', 'c']
length = 6
combinations(characters, length)
 


#Ejercicio 10:
def sheet_measurements(n, h = 841, w = 1189):
   if n == 0: 
      return (h, w)
   else: 
      aux = w
      w = h
      h = aux
      return sheet_measurements(n - 1, round(h / 2), w)
      
print(sheet_measurements(4))
