#repaso parcial

health = {0:"las nueces", 1:"la leche", 2:"el trigo", 3:"los huevos", 4:"el pescado"}
healthanswer = {0:False, 1:False, 2:False, 3:False, 4:False}
answer = 0
for i in range(len(health)):
    print("Tiene usted una alergia a " + health[i] + " ?")
    print("1) Si")
    print("2) No")
    print("3) No tengo ninguna otra alergia")
    answer = int(input())
    while answer != 1 and answer != 2 and answer != 3:
        print("Ingrese 1, 2 o 3")
        print("Tiene usted una alergia a " + health[i] + " ?")
        print("1) Si")
        print("2) No")
        print("3) No tengo ninguna otra alergia")
        answer = int(input())


    if answer == 2:
        continue
    elif answer == 3:
        break
    healthanswer[i] = True


if healthanswer[0] == False and healthanswer[1] == False and healthanswer[2] == False and healthanswer[3] == False and healthanswer[4] == False:
    print("Usted no tiene alergias")
else:
    print("Usted tiene alergias a:")




for i in range(len(healthanswer)):
    if healthanswer[i] == False:
        continue
    print(health[i])