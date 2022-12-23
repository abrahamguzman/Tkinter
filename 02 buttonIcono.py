import tkinter as tk
from tkinter import ttk
# Creamos un objeto de la clase Tk
window = tk.Tk()
# Tamaño
window.geometry('800x600')
# Título
window.title('Title')
# Cambiar ícono
window.iconbitmap('regalo.ico')

# Crear primer botón
# También se puede usar tk.Button, pero nos da un botón sin formato
boton = ttk.Button(window, text = 'Presióname')
boton.pack()


# Colocar para ejecutar la ventana
window.mainloop()