import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Catriel
apellido: Gatto
---
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''



class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        season = self.combobox_estaciones.get()
        destiny = self.combobox_destino.get()

        stay_price = 15000
        discount = 0
        increase = 0
        
        match(season):
            case "Invierno":
                match (destiny):
                    case "Bariloche":
                        increase = 20
                    case "Mar del plata":
                        discount = 20
                    case _ :
                        discount = 10
            case "Verano":
                match (destiny):
                    case "Bariloche" :
                        discount = 20
                    case "Mar del plata":
                        increase = 20
                    case _ :
                        increase = 10
            case _ :
                match (destiny):
                    case "Cordoba":
                        discount = 0
                    case _ :
                        increase = 10


        discount_total = stay_price * (discount / 100)
        final_price_discount = stay_price - discount_total

        increase_total = stay_price * (increase / 100)
        final_price_increase = stay_price + increase_total

        trip_buy_info = "La estación es {0}, el destino es {1}, el descuento es de %{2} y el incremento es de %{3}.\n\nEl importe final es de ${4} respecto del incremento.\nEl importe final es de ${5} respecto del descuento.".format(season, destiny, discount, increase, final_price_increase, final_price_discount)

        alert(title="", message=trip_buy_info)
                
    
if __name__ == "__main__":
    app = App()
    app.mainloop()