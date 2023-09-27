import random

#funcion para ingresar letras

def hangman (word_,guesses_):
    valid = False
    while valid == False:
        guess = input("Adivine: ").lower()
        #validacion
        if len(guess) != 1 or not guess.isalpha() :
            print("Por favor ingrese una sola letra.")
        else:
            valid = True
    for i in word_:
        if guess == i:
            guesses_ += guess
            break
    return guesses_

#funcion para mostrar las letras adivinadas

def hangmanword (word_,guesses_):
    answer_ = ""
    for i in word_:
        aux = True
        for j in guesses_:
            if i==j :
                answer_ += i
                aux = False
                break
        if aux == True:
            answer_ += "_"
    return answer_




print("El Juego del Ahorcado:")
#palabras posibles
words = ["test","cactus","iceberg","goblin","hospital","python"]
word = random.choice(words)
#cantidad de intentos
tries = 6
guesses =""
answer = ""
correct = True
#bucle principal
while (tries > 0) :
    print("La palabra es: ")
    answer = hangmanword(word,guesses)
    correct = True
    for i in answer:
        if i == "_":
            correct = False
            break
    print(answer)
    #sale del bucle si se gana
    if correct == True:
        print("Felicitaciones! ", word, " es la palabra.")
        break
    temp_guesses = hangman(word,guesses)
    #resta intentos en un intento incorrecto
    if temp_guesses == guesses:
        tries -= 1
        print("Incorrecto")
        if tries > 1:
            print("Quedan ", tries, " intentos.")
        else:
            print("Queda ", tries, "intento.")
    else:
        print("Correcto!")
    guesses = temp_guesses
    

if tries == 0: 
    print("Ups, se quedo sin intentos.")
    print("La palabra era ", word)
