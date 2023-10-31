#variables dimensionadas
#ejercicio 1


command = 0
passangers = []
countries = []




while command != 7:
    print("Ingrese el numero correspondiente a la accion que desea: ")
    print("1) Agregar pasajero.")
    print("2) Agregar ciudades.")
    print("3) Encontrar ciudad destino por DNI.")
    print("4) Ver cantidad de pasajeros a una ciudad.")
    print("5) Encontrar pais destino por DNI.")
    print("6) Ver cantidad de pasajeros a un pais.")
    print("7) Salir.")
    command = input()


    if (len(command) != 1) or (command.isdigit() == False):
        print("Por favor ingrese un numero")
        continue


    command = int(command)


    if command == 1:
        name_p = input("Ingrese el nombre del pasagero: ")
        dni_p = input("Ingrese el dni del pasajero: ")
        city_p = input("Ingrese la ciudad destino: ")
        #country_p = input("Ingrese el pais destino")
        temp_tupla = (name_p, dni_p, city_p)
        #temp_tupla_city = (city_p, country_p)


        passangers.append(temp_tupla)
        #countries.append(temp_tupla_city)
        aux = False
        for j in countries:
                if (city_p == j[0]):
                    aux = True
                    print(city_p , j[0], "are the same")
        if aux == False:
            print("A que pais pertenece ", city_p, " ?: ")
            country_p = input()
            temp_tupla_city = (city_p, country_p)
            countries.append(temp_tupla_city)
           
    if command == 2:
        city_p = input("Ingrese la ciudad destino: ")
        country_p = input("Ingrese el pais destino: ")
        temp_tupla_city = (city_p, country_p)
        countries.append(temp_tupla_city)
       
    if command == 3:
        print("Ingrese un DNI para mostrar la ciudad destino de ese pasajero: ")
        found = False
        dni_clue = input()
        for i in passangers:
            if i[1] == dni_clue:
                found = True
                print('Dni ', dni_clue, ' esta viajando a ', i[2])
        if found == False:
            print("Ese DNI no esta registrado.")
                
    if command == 4:
        city_clue = input("Ingrese la ciudad que desea revisar: ")
        amount_found = 0
        for i in passangers:
            if i[2] == city_clue:
                amount_found += 1
        if amount_found == 1:
            print("Un pasajero esta viajando a ", city_clue)
        else:
            print(amount_found, " pasajeros estan viajando a ", city_clue)
   
    if command == 5:
        print("Ingrese un DNI para mostrar el pais destino de ese pasajero: ")
        found = False
        dni_clue = input()
        for i in passangers:
            if i[1] == dni_clue:
                for j in countries:
                    if i[2] == j[0]:
                        found = True
                        print('Dni ', dni_clue, ' esta viajando a ', j[1])
        if found == False:
            print("Ese DNI no esta registrado.")

   
    if command == 6:
        country_clue = input("Ingrese el pais que desea revisar: ")
        amount_found = 0
        for i in countries:
            if i[1] == country_clue:
                print("Encontre el pais es: ", i[1])
                for j in passangers:
                    if i[0] == j[2]:
                        amount_found += 1
        if amount_found == 1:
            print("Un pasajero esta viajando a ", country_clue)
        else:
            print(amount_found, " pasajeros estan viajando a ", country_clue)

#Ejercicio 2

def sendinvoice(shopping_):
    home=[]
    home_=[]
    for i in shopping_:
        home.append(i[3])
                    
    for i in home:
        if i not in home_:
            home_.append(i)
    return home_                              
#[(cliente, dia del mes, monto, domiciolio del cliente)]
shopping=[("Nuria Costa", 5, 1234.5,"Calle 1 – 456"), ("Jorge Russo", 7, 3999, "Calle 2 – 741"),("Nuria Costa", 5, 2000,"Calle 1 – 456")]

home=sendinvoice(shopping)

for i in home:
    print("mandar factura a:",i)



#Ejercicio 3
#Socio n°1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
#Socio n°2, Bárbara Molina, ingresó: 17/03/2009, cuota al día
#Socio n°3, Lautaro Campos, ingresó: 17/03/2009, cuota al día


def show(partners_):
    for i, value in partners_.items():
        print("-----------------------------")
        print("socio",i)
        for key_, val in value.items():
            print(key_+": "+val) 

def amount(partners_):
    con=0          
    for i in partners:
        con+=1
    return con     

def notify_payment(numberso_,partners_):
    print(partners[numberso_]["cuota al dia"])
    partners_[numberso_]["cuota al dia"]="si"
    print("se actualizo el pago de socio "+partners_[numberso_]["nombre"])
    return partners_

def Changedate(partners_):
    for key, value in partners_.items():
        if(value["ingreso"]=="17/03/2009"):
            partners_[key]["ingreso"]="14/03/2018"
            print("Se cambio la feca de ingres de "+value["nombre"]+" de 17/03/2009 al 14/03/2018")

def deletpartner(partners_,name_):
    for key, value in partners_.items():
        if((value["nombre"]).lower()==name_):
            del partners_[key]
            return partners_
    print("No se encontro el nombre")
    return partners_        

def addpartners(partners_):
    aux=len(partners_)+1
    name=input("ingresar nombre: ").title()
    date=input("ingresar fecha formato(dd/mm/aaaa): ")
    
    partners_[aux]={"nombre":name, "ingreso":date,"cuota al dia":"si"}
    return partners_


partners={"1":{"nombre":"Amanda Núñez","ingreso":"17/03/2009","cuota al dia":"si"},
          "2":{"nombre":"Bárbara Molina", "ingreso":"17/03/2009","cuota al dia":"si"},
          "3":{"nombre":"Lautaro Campos", "ingreso":"17/03/2009","cuota al dia":"si"},
          }  


while True:
    print("A) Mostrar ")
    print("B) Ver cantidad de socios")
    print("C) Notificar pago")
    print("D) Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018")
    print("E) Eliminar un socio")
    print("EXIT) salir del menu")
    option=(input()).lower()
    if(option=="a"):
        show(partners)
        print("-----------------------------")
    
    elif(option=="b"):
        print("Cantidad de socios:",amount(partners))
        print("-----------------------------")
    
    elif(option=="c"):
        numberso=input("Ingresar numero de socio para notificar el pago: ")
        partners=notify_payment(numberso,partners)
        print("-----------------------------")
    elif(option=="d"):
        Changedate(partners)
        print("-----------------------------")
    elif(option=="e"):
        name=(input("Ingresar nombre y apellido del socio a eliminar ")).lower()    
        partners=deletpartner(partners, name)
        print("-----------------------------")
    elif(option=="f"):
        partners=addpartners(partners)
        print("-----------------------------")
    elif(option=="exit"):
        print("chau, saliendo del progama... ")
        break    