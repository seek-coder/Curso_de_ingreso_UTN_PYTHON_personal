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
Al presionar el botón ‘Validar número’, mediante prompt solicitar al usuario que ingrese un número. 
Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no coincidir con el rango, 
volverlo a solicitar hasta que la condición se cumpla
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_numero = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_numero_on_click)
        self.btn_validar_numero.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    def btn_validar_numero_on_click(self):

        number = prompt(title="", prompt="Ingrese un número: ")

        while int(number) < 0 or int(number) > 9: 
            alert(title="", message="Número inválido")
            number = prompt(title="", prompt="Ingrese un número: ")
        alert(title="", message="Número válido")



    
if __name__ == "__main__":
    app = App()
    app.mainloop()