import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x400")
tk.Label(ventana, text="Soy un Label").place(x=120,y=30)
tk.Button(ventana, text="Da un click").place(x=40, y=30)

ventana.mainloop()