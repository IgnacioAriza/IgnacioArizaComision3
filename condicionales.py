#Ejercicios en clase - Condicionales

date = input("Ingrese la fecha (formato día, DD/MM): ")
print(date.lower())

day_sem = date [0:date.find(",")]
day = int(date[date.find(" ") + 1:
            date.find("/")])
month = int(date[date.find("/") + 1:])
day_sem = day_sem.lower()

if (day_sem != "lunes" and day_sem != "martes" and day_sem != "miercoles" and day_sem != "jueves" and day_sem != "viernes" ):
    print("day incorrecto")
elif (day < 1 or day > 31):
    print("Fecha (día) incorrecta")
elif (month < 1 or month > 12):
    print("Fecha (mes) incorrecta")
else:
    print("Fecha ingresada válida") 

if (day_sem == "lunes"):
    print("Nivel inicial")
    dec = str(input("¿Se tomaron exámenes? "))
    if (dec == "si"):
        alu_aprob = int(input("Ingrese el número de alumnos aprobados: "))
        alu_desaprob = int(input("Ingrese el número de alumnos desaprobados: "))
        total = alu_aprob + alu_desaprob
        print(f"El porcentaje de aprobados es {(alu_aprob / total) * 100} %")
    
    else:
        print("No se tomaron exámenes")
elif (day_sem == "martes"):
    print("Nivel intermedio")
    dec = str(input("¿Se tomaron exámenes? "))
    if (dec == "si"):
        alu_aprob = int(input("Ingrese el número de alumnos aprobados: "))
        alu_desaprob = int(input("Ingrese el número de alumnos desaprobados: "))
        total = alu_aprob + alu_desaprob
        print(f"El porcentaje de aprobados es {(alu_aprob / total) * 100} %")
    else:
        print("No se tomaron exámenes")
elif (day_sem == "miercoles"):
    print("Nivel avanzado")
    dec = str(input("¿Se tomaron exámenes? "))
    if (dec == "si"):
        alu_aprob = int(input("Ingrese el número de alumnos aprobados: "))
        alu_desaprob = int(input("Ingrese el número de alumnos desaprobados: "))
        total = alu_aprob + alu_desaprob
        print(f"El porcentaje de aprobados es {(alu_aprob / total) * 100} %")
    else:
        print("No se tomaron exámenes")
elif (day_sem == "jueves"):
    print("Práctica hablada")
    asistencia = int(input("Ingrese el porcentaje de alumnos que asistieron a clase: %"))
    if (asistencia > 50):
        print("Asistió la mayoría")
    elif (asistencia < 50):
        print("No asistió la mayoría")
    else:
        print("Asistió la mitad del curso")    
else:
    print("Inglés para viajeros")
    if (day == 1 and (month == 1 or month == 7)):
        print("Comienzo de nuevo ciclo")
        alu_new = int(input("Ingrese cantidad de alumnos del nuevo ciclo: "))
        alu_arancel = int(input("Ingrese el arancel por cada alumno: $"))
        tot_arancel = print(f"El ingreso total es de ${alu_arancel * alu_new}")
    else:
        print("Ciclo comenzado")