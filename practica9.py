x=10 #Global
def mostrar():
    x=5 #Local
    print("Dentro de la funcion: ", x)
mostrar()
print("Fuera de la funcion: ",x)