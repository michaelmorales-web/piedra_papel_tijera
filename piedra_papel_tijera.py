# Programa para jugar piedra papel o tijera

# librerias
import random

#------
# input
#------
print("------------------------")
print("-----Vamos a jugar------")
print("------------------------")
print("La computadora ha generado un número entre 1 y 3")
print("-----Escoge entre 1 y 3-----")
computer_number = random.randint(1,3)

user_number = int(input("Escoge bien: "))

#----------
# procesing
#----------

# Verificar si el número ingresado este entre 1 y 3
if(user_number>=1 and user_number<=3):
    print