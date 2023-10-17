import random

## Version 1
# numero = random.randint(0, 10)
# my_value = input("Adivina el numero:")
# my_value = int(float(my_value))

# intentos = 1
# while my_value != numero:
#     my_value = input("Numero Incorrecto, Intenta otra vez: ")
#     my_value = int(float(my_value))
#     intentos += 1
    
# print("Adivinaste el numero, es: ", my_value)
# print("Numero de intentos: ", intentos)

# Version 2
numero = random.randint(0, 10)
intentos = 1
while True:
    my_value = input("Adivina el numero:")
    my_value = int(float(my_value))
    if my_value == numero:
        print("Adivinaste el numero, es: ", my_value)
        print("Numero de intentos : ", intentos)
        break

    intentos += 1
