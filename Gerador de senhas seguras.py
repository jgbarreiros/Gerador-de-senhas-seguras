from random import randint

lista=["?/<>.,:;|}{][+_=-)(*&^%$#@!9876543210ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba","abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>/?","abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>/?"]

contador_caracteres = 0

while contador_caracteres != 20:
    
    caracter2 = randint(0,2)
    caracter = randint(0,88)
   
    print(lista[caracter2][caracter], end= "")
    
    contador_caracteres+=1
print("\n copie sua senha acima e aproveite ;)" )


import pyfiglet 

assinatura = pyfiglet.figlet_format("@jgbarreiros")#prompzinho de assinatura
print(assinatura)
