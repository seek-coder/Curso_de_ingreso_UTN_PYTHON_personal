import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Catriel
apellido: Gatto
---
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        
        trademark = self.combobox_marca.get()
        quantity = self.combobox_cantidad.get()
        quantity_int = int(quantity)

        lamp_price = 800 * quantity_int
        discount_percent = 0
        '''
        if (quantity_int >= 6):
            discount_percent = 50
        elif (quantity_int == 5):
            if (trademark == "ArgentinaLuz"):
                discount_percent = 40
            else:
                discount_percent = 30
        elif (quantity_int == 4):
            if (trademark == "ArgentinaLuz" or trademark == "FelipeLamparas"):
                discount_percent = 25
            else:
                discount_percent = 20
        elif (quantity_int == 3):
            if (trademark == "ArgentinaLuz"):
                discount_percent = 15
            elif (trademark == "FelipeLamparas"):
                discount_percent = 10
            else:
                discount_percent = 5

        discount_total = lamp_price * (discount_percent / 100)
        final_price = lamp_price - discount_total
        discount_ad = 0

        if (final_price > 4000):
            final_price -= final_price * 0.05
            discount_ad = 5

        buy_info = "La marca es {0} y la cantidad total es de {1} lámpara/s.\n\nEl descuento por cantidad es de %{2}.\n\nEl descuento adicional es de %{3}.\n\nEl importe total a pagar es de ${4}".format(trademark, quantity_int, discount_percent, discount_ad, final_price)

        alert(title="", message=buy_info)
        '''

        match quantity_int:
            case 1 | 2:
                discount_percent = 0
            case 3:
                match trademark:
                    case "ArgentinaLuz":
                        discount_percent = 15
                    case "FelipeLamparas":
                        discount_percent = 10
                    case _ :
                        discount_percent = 5
            case 4:
                match trademark:
                    case "ArgentinaLuz" | "FelipeLamparas":
                        discount_percent = 25
                    case _ :
                        discount_percent = 20
            case 5:
                match trademark:
                    case "ArgentinaLuz":
                        discount_percent = 40
                    case _ :
                        discount_percent = 30
            case _ :
                discount_percent = 50
            
        discount_total = lamp_price * (discount_percent / 100)
        final_price = lamp_price - discount_total
        discount_ad = 0

        if (final_price > 4000):
            final_price -= final_price * 0.05
            discount_ad = 5    

        buy_info = "La marca es {0} y la cantidad total es de {1} lámpara/s.\n\nEl descuento por cantidad es de %{2}.\n\nEl descuento adicional es de %{3}.\n\nEl importe total a pagar es de ${4}".format(trademark, quantity_int, discount_percent, discount_ad, final_price)

        alert(title="", message=buy_info)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()