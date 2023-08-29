# Ejercicio 1 & 2


edad = int(input("Ingrese la edad de su computadora: "))
if (edad <= 2 and edad >= 0):
    print("El computador es nuevo")
elif (edad < 0):
    print("ERROR: Ingrese un número válido")
else:
    print("El computador es viejo")


#Ejercicio 3


nombre1=input("ingresa nombre 1: ")
nombre2=input("ingresa nombre 2: ")
if (nombre1[0:1]==nombre2[0:1]):
    print("Coincidencia")
else:
    print("No hay coincidencia")  


#Ejercicio 4 


voto=input("Candidatos a votar: candidato A, candidato B o candidato C: ")
voto=voto.lower()


if (voto == "candidato a" or voto=="a"):
    print("voto por el partido rojo")
elif(voto == "candidato b" or voto=="b"):
    print("voto por el partido verde")
elif(voto == "candidato c" or voto=="c"):
    print("voto por el partido azul")


# Ejercicio 5 


letra = input("Ingrese una letra: ")
if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
    print("Es una vocal.")
elif (letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u"):
    print("No es una vocal")
elif (len(letra) != 0):
    print("No se puede procesar el dato")


# Ejercicio 6 


anio = int(input("Ingrese un año: "))
if ((anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print("El año no es bisiesto.")


#Ejercicio  7


num1=input("ingresar un numero: ")
num2=input("ingresar un numero: ")
num3=input("ingresar un numero: ")


menor=num1
if(menor>num2):
    menor=num2
elif(menor>num3):
    menor=num3
print("El menor es: ",menor)    


#Ejercicio 8


usuario=input("ingesar usuario: ")
contrasena=input("ingresar contraseña: ")
if (usuario=="Gwenevere" and contrasena=="excalibur"):
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")


# Ejercicio 9 


nombre = input("Ingrese su nombre: ").lower()
sexo = input("Ingrese su genero (hombre/mujer): ")
inicial = nombre[0]
if ((sexo == "mujer" and inicial <= "m") or (sexo == "hombre" and inicial >= "n")):
    print("GRUPO A")
else:
    print("GRUPO B")


#Ejercicio 10 


edad=int(input("ingresar edad: "))
if(edad<4):
    print("Puede entrar gratis")
elif(edad>=4 or edad<=18):
    print("Tiene que pagar $500")
elif(edad>18):
    print("Tiene que pagar $1000")






#Ejercicio 11 


print("Bienvenido a la pizzeria Bella Napoli")
orden=input("¿Quiere el menu vegetariano? si/no ")
orden=orden.lower()
if(orden=="si" or orden =="s"):
     print("Ingredientes vegetarianos:")
     print(".Pasto")
     print(".Pimiento")
     print(".Tofu")
elif(orden=="no" or orden =="n"):
    print("Ingredientes no vegetarianos:")
    print(".Peperoni")
    print(".Jamón")
    print(".Salmón")


ingre=input("Que ingrediente quiere? ")
if(orden=="si" or orden =="s"):
     print("Su pizza vegetariana tiene: mozzarella, tomate y",ingre)
elif(orden=="no" or orden =="n"):
     print("Su pizza tiene: mozzarella, tomate y",ingre)


# Ejercicio 12 


anio_actual = int(input("Ingrese el año actual: "))
anio = int(input("Ingrese otro año: "))
pasaron = anio_actual - anio
falta = anio - anio_actual
if (anio_actual > anio):
    print(f"Pasaron {pasaron} años.")
elif (anio_actual < anio):
    print(f"Faltan {falta} años.")
else:
    print("Es el mismo año.")


# Ejercicio 13 


num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
mayor = 0
menor = 0


if (num1 < 0 or num2 < 0):
    print("Ingresó un número negativo.")
elif (num1 == 0 or num2 == 0):
    print("Ingresó un número nulo")


if (num1 > num2):
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1


if (mayor == 0 or menor == 0):
    print("0 sólo es múltiplo de 0")
else:
    if (mayor % menor == 0):
        print("Son múltiplos.")
    elif (mayor % menor != 0):
        print("No son múltiplos.")




#Ejercicio 14 


print("Ingrese los coeficientes de una ecuación de primer grado (a x + b = 0)")
coe_a=int(input("Ingrese ¨a¨ "))
coe_b=int(input("Ingrese ¨b¨ "))
respues_=-coe_b/coe_a
coe_a=str(coe_a)
coe_b=str(coe_b)
respues_=str(respues_)
print("El valor de x es: "+respues_)
print("La formula quedaria: "+coe_a
      +"*"+respues_+"+"+coe_b+"="+"0")


#Ejercicio 15: 


import math


print("c: area de un circulo / t: area de un triangulo")


operacion = input("¿Que operaciòn desea realizar?: ")
operacion = operacion.lower()


if operacion == "t":
  base = int(input("Ingrese base: "))
  altura = int(input("Ingrese altura: "))
  print(f"Resultado: {(base*altura)/2}")
elif operacion == "c":
  radio = int(input("Ingrese radio: "))
  print(f"Resultado: {round(math.pi * radio**2, 2)}")
else:
    print("Operacion invalida")


#Ejercicio 16:  


valor1 = int(input("Ingrese primer valor: "))
valor2 = int(input("Ingrese segundo valor: "))


print("1. Suma, 2. Multiplicaciòn, 3. Resta, 4. Division")


operacion = int(input("Operacion que desea realizar: "))


if operacion == 1:
  print(f"Resultado: {valor1 + valor2}")
elif operacion == 2:
  print(f"Resultado: {valor1 * valor2}")
elif operacion == 3:
  print(f"Resultado: {valor1 - valor2}")
elif operacion == 4:
  print(f"Resultado: {valor1 / valor2}")
else:
  print("Operacion invalida")




#Ejercicio 17: 


dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
mensaje_dia = ["Feliz Lunes", "Buen Martes", "Que lindo Miercoles", "Dia Jueves", "Hoy es Viernes", "Sabado, hoy se sale", "Domingo, hoy se duerme"]


dia_semana = input("Ingrese dia de la semana: ")
dia_semana = dia_semana.lower()


if dia_semana not in dias_semana:
  print("El dia ingresado no es un dia valido")
else:
  if dia_semana == dias_semana[0]:
    print(mensaje_dia[0])
  elif dia_semana == dias_semana[1]:
    print(mensaje_dia[1])
  elif dia_semana == dias_semana[2]:
    print(mensaje_dia[2])
  elif dia_semana == dias_semana[3]:
    print(mensaje_dia[3])
  elif dia_semana == dias_semana[4]:
    print(mensaje_dia[4])
  elif dia_semana == dias_semana[5]:
    print(mensaje_dia[5])
  else:
    print(mensaje_dia[6])


# Ejercicio 18:


horas_trabajo = int(input("Ingrese cantidad de horas trabajadas en el mes: "))
salario_hora = int(input("Ingrese salario por hora: "))


if horas_trabajo > 48:
  hora_extra = horas_trabajo - 48
  trabajo_minimo = salario_hora * 48
  pago_extra = hora_extra * salario_hora
  ingreso_total = trabajo_minimo + pago_extra + (pago_extra * .10)
  print(f"Salario total: ${round(ingreso_total)}")
else:
  ingreso_total = salario_hora * horas_trabajo
  print(f"Salario total: ${round(ingreso_total)}")


#Ejercicio 19:


precio_lapiz = 60
descuento = .7


cantidad_lapices = int(input("Ingrese cantidad de lapices: "))


if cantidad_lapices >= 1000:
  total = precio_lapiz * cantidad_lapices
  precio_final = total - (total * descuento)
  print(f"Precio final: ${round(precio_final)}")




#Ejercicio 20


pre_notas = input("Ingrese nota 1: ") + "," + input("Ingrese nota 2: ") + "," + input("Ingrese nota 3: ") + "," + input("Ingrese nota 4: ")


nota1, nota2, nota3, nota4 = pre_notas.split(",")


promedio = (int(nota1) + int(nota2) + int(nota3) + int(nota4)) / 4


if promedio >= 6:
  print(f"Nota: {round(promedio, 2)}, Aprobado")
else:
  print(f"Nota: {round(promedio, 2)}, Desaprobado")