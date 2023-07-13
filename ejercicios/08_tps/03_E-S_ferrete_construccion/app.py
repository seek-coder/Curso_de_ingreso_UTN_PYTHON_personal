import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

2.	El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado permetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en es lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts = 4
    (F)Poste Quebracho Fino de 2.2 mts = 6
    (V)Varillas = 60
    
    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)

        self.btn_calcular = customtkinter.CTkButton(
            master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

    def btn_calcular_on_click(self):
        length = self.txt_largo.get()
        length_float = float(length) 

        width = self.txt_ancho.get()
        width_float = float(width) 

        #A Metros cuadrados y perímetro
        m2 = length_float * width_float
        m2_float = float(m2)

        perimeter = (length_float + width_float) * 2

        #B Cantidad de (G) , o sea, cada 250mts lineales (X) y en esquinas (4)
        
        g_per_perimeter = (perimeter / 250) + 4
        poste_quebracho_grueso = int(g_per_perimeter)

        #C Cantidad de (V)

        f_per_perimeter = (perimeter / 12) - 4
        poste_quebracho_fino = int(f_per_perimeter)

        #D Cantidad de (F)

        v_per_perimeter = perimeter / 2
        varillas = int(v_per_perimeter)

        #E Alambre de lata resistencia

        wire = perimeter * 7
        wire_float = float(wire)


        #Output
        info_building = "Los metros cuadrados del terreno dan un total de {0}m2 y el perímetro es de {1}mts.\n\nLa cantidad de postes de quebracho grueso es de {2}, la cantidad de postes de quebracho fino es de {3} y de varillas es {4}.\n\nLa cantidad total de alambre alta resistencia 17/15 considerando 7 hilos es un total de {5}mts".format(m2, perimeter, poste_quebracho_grueso, poste_quebracho_fino, varillas, wire_float)

        alert(title="", message=info_building)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
