# Programa para jugar piedra papel o tijera

# librerias
import random

#------
# input
#------
print("------------------------")
print("-----PIEDRA PAPEL O TIJERA------")
print("------------------------")
print("La computadora ha generado un número entre 1 y 3")
print("-----Escoge entre 1 y 3-----")
print("----El número 1 significa PIEDRA----")
print("----El número 2 significa PAPEL----")
print("----El número 3 significa TIJERAS----")
computer_number = random.randint(1,3)

user_number = int(input("Escoge bien: "))

#----------
# procesing
#----------

if user_number == 1:
    if computer_number == 1:
        print("EMPATE")
    elif computer_number == 2:
        print("PERDIO")
    else:
        print("GANO")
elif user_number == 2:
    if computer_number == 1:
        print("GANO")
    elif computer_number == 2:
        print("EMPATE")
    else:
        print("PERDIO")
elif user_number == 3:
    if computer_number == 1:
        print("PERDIO")
    elif computer_number == 2:
        print("GANO")
    else:
        print("EMPATE")
else:
    print("ERROR")
    exit()
print("____________________________________________________")
print("____________________________________________________")
