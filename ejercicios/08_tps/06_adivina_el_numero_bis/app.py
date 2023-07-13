import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre: Catriel
apellido: Gatto
---
Adivina el número (v 1.0):
Al comenzar el juego generamos un número secreto del 1 al 100, en la pantalla del juego dispondremos de un cuadro de texto 
para ingresar un número y un botón “Verificar”, si el número ingresado es el mismo que el número secreto se dará por terminado
 el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “usted es un Psíquico”.
	2° intento: “excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	Más de 6 intentos: “afortunado en el amor!!”.

de no ser igual se debe informar si 
“falta…”  para llegar al número secreto  o si 
“se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.txt_numero = customtkinter.CTkEntry(master=self)
        self.txt_numero.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.numero_secreto = random.randrange(1, 100)
        self.numero_intento = 0
        print(self.numero_secreto)


    def btn_mostrar_on_click(self):
        self.numero_intento += 1

        num = self.txt_numero.get()
        num_int = int(num)

        secret_num = int(self.numero_secreto)

        mensaje_victoria = f"Ganó en {self.numero_intento} intento/s"
        
        if num_int == secret_num:
            match self.numero_intento:
                case 1:
                    mensaje = f"{mensaje_victoria}. Usted es un Psíquico"
                case 2:
                    mensaje = f"{mensaje_victoria}. Excelente percepción"
                case 3:
                    mensaje = f"{mensaje_victoria}. Esto es suerte"
                case  4 | 5 | 6:
                    mensaje = f"{mensaje_victoria}. Excelente técnica"
                case _ :
                    mensaje = f"{mensaje_victoria}. Afortunado en el amor!!."
        elif num_int < secret_num:
            mensaje = "¡Un número más alto! Falta..."
        else:
            mensaje = "¡Un número más bajo! Se pasó..."
        
        self.txt_numero.delete(0, "end")

        alert(title="", message=mensaje)

if __name__ == "__main__":
    app = App()
    app.mainloop()