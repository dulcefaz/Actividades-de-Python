import tkinter as tk
ventana=tk.Tk()
ventana.geometry("400x500")
tk.Label(ventana,text="Etiqueta 1", bg="red").pack()
tk.Label(ventana,text="Etiqueta 2", bg="green").pack()
tk.Label(ventana,text="Etiqueta 3", bg="blue").pack()
ventana.mainloop()