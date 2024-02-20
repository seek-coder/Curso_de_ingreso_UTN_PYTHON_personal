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
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        count = 0
        sum_positive = 0
        sum_negative = 0
        positive_quantity = 0
        negative_quantity = 0
        zero_quantity = 0
        positive_i_minus_negative_i = 0

        while True:
            ask_number = prompt(title="",prompt=f"Ingrese un número cualquiera:\n\n(Cantidad de números ingresados: {count})")
            if ask_number == None:
                break
            number_float = float(ask_number)
            count += 1

            if number_float > 0:
                sum_positive += number_float
                positive_quantity += 1
            elif number_float < 0:
                sum_negative += number_float
                negative_quantity += 1
            elif number_float == 0:
                zero_quantity += 1

            positive_i_minus_negative_i = abs(positive_quantity - negative_quantity) #abs para valor absoluto, en este caso, positivo
            #print(count, sum_positive, sum_negative, positive_quantity, negative_quantity, zero_quantity, positive_i_minus_negative_i,)
        alert(title="",message=f"La suma acumulada de los negativos es {sum_positive} y de negativos es {sum_negative}.\n\nLa cantidad de numeros positivos ingresados es de {positive_quantity}, de numeros negativos es de {negative_quantity} y de ceros es de {zero_quantity}.\n\nLa diferencia entre la cantidad de los números positivos ingresados y de los números negativos es de {positive_i_minus_negative_i}.")


        # TRY 2:
        def btn_comenzar_ingreso_on_click(self):
            count = 0
            sum_positive = 0
            sum_negative = 0
            positive_quantity = 0
            negative_quantity = 0
            zero_quantity = 0
            positive_i_minus_negative_i = 0
    
            while True:
                ask_number = prompt(title="",prompt=f"Ingrese un número cualquiera:\n\n(Cantidad de números ingresados: {count})")
                
                if ask_number == None:
                    break
                number_float = float(ask_number)
                count += 1
    
                if number_float > 0:
                    sum_positive += number_float
                    positive_quantity += 1
                    print("Cantidad de positivos: " + str(positive_quantity))
                elif number_float < 0:
                    sum_negative += number_float
                    negative_quantity += 1
                    print("Cantidad de negativos: " + str(negative_quantity))
                else:
                    zero_quantity += 1
                    print("Cantidad de ceros: " + str(zero_quantity))
    
            positive_i_minus_negative_i = abs(positive_quantity - negative_quantity) #abs para valor absoluto, en este caso, positivo
            #print(count, sum_positive, sum_negative, positive_quantity, negative_quantity, zero_quantity, positive_i_minus_negative_i,)
            alert(title="",message=f"La suma acumulada de los positivos es {sum_positive} y de negativos es {sum_negative}.\n\nLa cantidad de numeros positivos ingresados es de {positive_quantity}, de numeros negativos es de {negative_quantity} y de ceros es de {zero_quantity}.\n\nLa diferencia entre la cantidad de los números positivos ingresados y de los números negativos es de {positive_i_minus_negative_i}.")
if __name__ == "__main__":
    app = App()
    app.mainloop()
