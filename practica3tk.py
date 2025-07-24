import tkinter as tk 

ventana=tk.Tk()
ventana.geometry("400x400")
etiqueta1=tk.Label(ventana,text="user: ").grid(row=1, column=1)
entrada1=tk.Entry(ventana).grid(row=2, column=1)

tk.Label(ventana,text="").grid(row=2, column=1)

etiqueta2=tk.Label(ventana, text="password: ").grid(row=3, column=1)
entrada2=tk.Entry(ventana).grid(row=3, column=3)
boton1=tk.Button(ventana,text="Acceder").grid(row=4, column=3)
boton2=tk.Button(ventana,text="recuparar contraseña").grid(row=4, column=4)

ventana.mainloop()