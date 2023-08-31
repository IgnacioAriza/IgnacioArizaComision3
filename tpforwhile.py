#Ejercicio 1


letters = "abcdefghijklmnñopqrstuvwxyz"


message_encrip = ""
encrip = int(input("Ingrese el numero para la encriptacion: "))


for i in range(5):
  message = input("Ingrese su mensaje: ")
  message_lower = message.lower()


  for j in message_lower:
    letter = letters.find(j)
    search = letter + encrip


    if search > 26:
      resto = search % 26
      message_encrip += letters[resto]
    else:
      message_encrip += letters[letter + encrip]
  print(f"Su mensaje es: {message_encrip.upper()}")
  message_encrip = ""




#Ejercicio2


number = input("Ingrese un numero real positivo")
evens = 0
odds = 0
evenslocal = 0
oddslocal = 0
while number != "0":
    for i in number:
        i = int(i)
        if i % 2 == 0:
            evens += 1
            evenslocal += 1
            continue
        if i % 2 != 0:
            odds += 1
            oddslocal += 1
            continue
    print("Su numero tenia ", evenslocal , "numeros pares, y ", oddslocal, " numeros impares.")
    evenslocal = 0
    oddslocal = 0
    number = input("ingrese un numero real positivo")


print("Hubieron ", evens, " numeros pares, y ", odds, " numeros impares.")