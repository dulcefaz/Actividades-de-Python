numero1= float(input("Introduzca el primer numero"))
numero2= float (input("Introduzca el segundo numero"))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
potencia= numero1 % numero2
residuo = numero1 ** numero2

print (" La suma es de: " + str(suma))
print (" La resta es de: " + str (resta))
print (" La multiplicacion  es de: " + str(multiplicacion))
print (" La division  es de: " + str (division))
print (" La potencia  es de: " +  str(potencia))
print (" El residuo es de: " + str (residuo))

if numero1 == numero2:
    print (" Son del mismo valor ")
elif numero1 > numero2:
    print ("El numero "+str(numero1)+"es mayor a "+str(numero2))
else: 
    print(" El numero "+str(numero2)+"es mayor a "+str(numero1))