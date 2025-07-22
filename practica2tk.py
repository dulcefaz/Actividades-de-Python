import tkinter as tk 

def saludar():
    nombre = entrada.get()
    etiqueta.config(text=f"Hola,{nombre}!")

ventana = tk.Tk()
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Escribe tu nombre: ")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="saludar", command=saludar)

boton.pack()

ventana.mainloop()
    
