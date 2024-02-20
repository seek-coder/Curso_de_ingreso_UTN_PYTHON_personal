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
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_minimo = customtkinter.CTkEntry(master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        # MALA PRÁCTICA
        count = 0
        max_number = None #variable vacía
        min_number = None

        while True:
            ask_number = prompt(title="",prompt=f"Ingrese un número cualquiera:\n\n(Cantidad de números ingresados: {count})")
            if ask_number == None:
                break
            number_float = float(ask_number)
            count += 1
            if count == 1: #establezco el número de referencia para después del primer conteo filtrar el max y el min
                max_number = number_float
                min_number = number_float
            else: #o sea, después de la primera vuelta, donde el primer número deja de ser máximo y mínimo a la vez
                if number_float > max_number:
                    max_number = number_float
                elif number_float < min_number:
                    min_number = number_float
            print(min_number, max_number)
        self.txt_minimo.delete(0, "end")
        self.txt_minimo.insert(0, min_number)
        self.txt_maximo.delete(0, "end")
        self.txt_maximo.insert(0, max_number)

        # SOLUCIÓN 1
        max_number = None #variable vacía
        min_number = None

        while True:
            ask_number = prompt(title="",prompt=f"Ingrese un número cualquiera:\n\n")
            # hago el break antes de parsearlo
            if ask_number == None:
                break
            number_float = float(ask_number)

            if max_number == None or number_float > max_number:
                max_number = number_float
            if min_number == None or number_float < min_number:
                min_number = number_float
            print(min_number, max_number)
        self.txt_minimo.delete(0, "end")
        self.txt_minimo.insert(0, min_number)
        self.txt_maximo.delete(0, "end")
        self.txt_maximo.insert(0, max_number)

        # SOLUCIÓN 2
        bandera_primer_ingreso = False
        maximo = 0
        minimo = 0

        if number_float > maximo or bandera_primer_ingreso == False:
            maximo = number_float
        if number_float < minimo or bandera_primer_ingreso == False:
            minimo = number_float

        bandera_primer_ingreso = True

if __name__ == "__main__":
    app = App()
    app.mainloop()
