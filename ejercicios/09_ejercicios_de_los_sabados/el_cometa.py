import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

'''
La juguetería El MUNDO DE OCTAVIO nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

COMETA: 

AB = Diámetro mayor (se debe calcular)
DC = diámetro menor (se ingresa por prompt)
BD y BC = lados menores (se ingresa por prompt)
AD y AC = lados mayores (se ingresa por prompt)

Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
El cometa estará construido con papel de alta resistencia.
La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="El Cometa", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.label_diametro_menor = customtkinter.CTkLabel(master=self, text="Diametro Menor DC")
        self.label_diametro_menor.grid(row=1, column=0, padx=20, pady=10)

        self.txt_diametro_menor= customtkinter.CTkEntry(master=self)
        self.txt_diametro_menor.grid(row=1, column=1)
        
        self.label_lados_menores = customtkinter.CTkLabel(master=self, text="Lados Menores BD y BC")
        self.label_lados_menores.grid(row=2, column=0, padx=20, pady=10)

        self.txt_lados_menores = customtkinter.CTkEntry(master=self)
        self.txt_lados_menores.grid(row=2, column=1)

        self.label_lados_mayores = customtkinter.CTkLabel(master=self, text="Lados Mayores AD y AC")
        self.label_lados_mayores.grid(row=3, column=0, padx=20, pady=10)

        self.txt_lados_mayores = customtkinter.CTkEntry(master=self)
        self.txt_lados_mayores.grid(row=3, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        from math import sqrt

        diametro_menor = self.txt_diametro_menor.get()
        diametro_menor_float = float(diametro_menor)

        lado_menor = self.txt_lados_menores.get()
        lado_menor_float = float(lado_menor)

        lado_mayor = self.txt_lados_mayores.get()
        lado_mayor_float = float(lado_mayor)


        altura_triangulo1 = diametro_menor_float/2
        altura_triangulo1_float = float(altura_triangulo1)

        lado_menor_x1_x2 = sqrt(lado_menor_float**2 - (altura_triangulo1_float)**2) #cateto triangulo 1
        lado_mayor_y1_y2 = sqrt(lado_mayor_float**2 - (altura_triangulo1_float)**2) #cateto triangulo 2

        diametro_mayor = lado_menor_x1_x2 + lado_mayor_y1_y2
        diametro_mayor_float = float(diametro_mayor)

        area_rombo = (diametro_mayor_float * diametro_menor_float) / 2

        varillas_total = lado_mayor_float*2 + lado_menor_float*2 + diametro_mayor_float + diametro_menor_float

        papel_adicional = (area_rombo * 0.1)
        papel_total = area_rombo + papel_adicional

        varillas_total_10 = varillas_total * 10
        papel_total_10 = papel_total * 10

        # 100cm = 1m

        varillas_total_mts = float(varillas_total / 100)
        varillas_total_10_mts = float(varillas_total_10 / 100)
        papel_total_mts = float(papel_total / 100)
        papel_total_10_mts = float(papel_total_10 / 100)



        descripción_cometa = "----------\n\nINFO. EN CENTÍMETROS.\n\n----------\n\nEl diametro menor del cometa es de {0:.2f}cms.\n\nCada lado menor es de {1:.2f}cms y cada lado mayor es de {2:.2f}cms.\n\nEl diametro mayor calculado es de {3:.2f}cms.\n\nEL área total del cometa es de {4:.2f}cms.\n\n----------\n\nINFO. EN METROS\n\n----------\n\nLos mts de varilla necesitados son {5:.4f}mts y de papel son {6:.4f}mts para 1 COMETA.\n\nLos cms de varilla necesitados son {7:.4f}mts y de papel son {8:.4f}mts para 10 COMETAS.".format(diametro_menor_float, lado_menor_float,lado_mayor_float,diametro_mayor_float,area_rombo, varillas_total_mts, papel_total_mts, varillas_total_10_mts, papel_total_10_mts)

        alert(title="",message=descripción_cometa)


    
if __name__ == "__main__":
    app = App()
    app.mainloop()