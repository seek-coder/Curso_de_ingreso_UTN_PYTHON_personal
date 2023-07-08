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
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        amount1 = self.txt_importe_1.get()
        amount2 = self.txt_importe_2.get()
        amount3 = self.txt_importe_3.get()
        amount1_float = float(amount1)
        amount2_float = float(amount2)
        amount3_float = float(amount3)
        sum = amount1_float + amount2_float + amount3_float

        alert(title="",message="La suma total del precio de los productos es: " + "$" + str(sum))

    def btn_promedio_on_click(self):
        amount1 = self.txt_importe_1.get()
        amount2 = self.txt_importe_2.get()
        amount3 = self.txt_importe_3.get()
        amount1_float = float(amount1)
        amount2_float = float(amount2)
        amount3_float = float(amount3)
        average = (amount1_float + amount2_float + amount3_float) / 3

        alert(title="",message="El promedio total del precio de los productos es: " + "$" +str(average))

    def btn_total_iva_on_click(self):
        amount1 = self.txt_importe_1.get()
        amount2 = self.txt_importe_2.get()
        amount3 = self.txt_importe_3.get()
        amount1_float = float(amount1)
        amount2_float = float(amount2)
        amount3_float = float(amount3)
        sum = amount1_float + amount2_float + amount3_float
        iva = 21
        sum_with_iva = sum * (iva / 100)
        final_price = sum + sum_with_iva


        alert(title="",message="La suma total del precio de los productos más IVA 21% es: " + "$" +str(final_price))     
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()