import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Catriel
apellido: Gatto
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números DESCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
            i = 11 #no es un contador porque no arranca en 0

            while i > 1 :
                i -= 1
                alert(title="", message=i)

        # BIS 2 (1)
        suma = 0
        numero = 1

        while numero <= 10:
            if numero % 2 == 0:
                suma += numero
            numero += 1

        # BIS 2 (2)
        # Inicializamos la variable de suma
        suma = 0
        # Inicializamos el número en 2, ya que es el primer número par dentro del rango
        numero = 2
        
        # Mientras el número sea menor o igual a 10
        while numero <= 10:
            # Sumamos el número a la variable de suma
            suma += numero
            # Aumentamos el número en 2 para pasar al siguiente número par
            numero += 2
    
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
