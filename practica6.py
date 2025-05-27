numero_secreto=8
intento=int(input("Ingresa un numero entre 1 y 10 "))
while intento !=numero_secreto:
    print("Valor incorrecto ")
    intento=int(input("Escribe otro numero "))
print("Numero correcto ")