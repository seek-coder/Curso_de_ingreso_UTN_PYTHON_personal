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
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
Calcular la suma acumulada de los positivos y multiplicar los negativos. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_producto = customtkinter.CTkEntry(master=self, placeholder_text="Producto")
        self.txt_producto.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        count = 0
        sum_positive = 0
        mul_negative = 1 #acá establezco 1 en vez de 0 porque sino la multiplicación se va a igualar siempre a 0! (que era el problema que no me dejaba avanzar)

        while True:
            ask_number = prompt(title="",prompt=f"Ingrese un número cualquiera:\n\n(Cantidad de números ingresados: {count})")
            if ask_number == None:
                break

            number_float = float(ask_number)

            if number_float == 0: #si coloco la condición antes del casteo, se evalúa antes y me tira TypeError
                break
            count += 1
            
            if number_float > 0:
                sum_positive += number_float
            elif number_float < 0:
                mul_negative *= number_float
            #print(sum_positive, mul_negative) #por razones informativas ;)
        self.txt_suma_acumulada.delete(0, "end")
        self.txt_suma_acumulada.insert(0, sum_positive)
        self.txt_producto.delete(0, "end")
        self.txt_producto.insert(0, mul_negative)


    
if __name__ == "__main__":
    app = App()
    app.mainloop()
