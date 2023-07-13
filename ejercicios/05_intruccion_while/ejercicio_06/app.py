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
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        sum = self.txt_suma_acumulada.get()
        average = self.txt_promedio.get()

    #    number1 = prompt(title="",prompt="Ingrese el primer número (de cinco)")
    #    number2 = prompt(title="",prompt="Ingrese el segundo número (de cinco)")
    #    number3 = prompt(title="",prompt="Ingrese el tercer número (de cinco)")
    #    number4 = prompt(title="",prompt="Ingrese el cuarto número (de cinco)")
    #    number5 = prompt(title="",prompt="Ingrese el último número (de cinco)")

    #    number1_float = float(number1)
    #    number2_float = float(number2)
    #    number3_float = float(number3)
    #    number4_float = float(number4)
    #    number5_float = float(number5)

    #    numbers_sum_of_5 = number1_float + number2_float + number3_float + number4_float + number5_float
    #    average_sum_of_5 = (number1_float + number2_float + number3_float + number4_float + number5_float) / 5
        count = 0
        sum_number = 0
        average_number = 0
        numbers = []

        while True:
            count += 1
            ask_number = prompt(title="",prompt=f"Ingrese un número para la posición {count}:")
            number = float(ask_number)

            numbers.append(ask_number)

            sum_number += number
            average_number += number / 5

            if (count == 5):
                self.txt_suma_acumulada.delete(0, "end")
                self.txt_suma_acumulada.insert(0, sum_number)
                self.txt_promedio.delete(0, "end")
                self.txt_promedio.insert(0, average_number)

                break
if __name__ == "__main__":
    app = App()
    app.mainloop()
