import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Catriel
apellido: Gatto
---
Ejercicio: instrucion_if_06
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener contenido en la caja de texto txtEdad, transformarlo en número 
y calcular si es mayor, niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años) o adolescente (edad entre 13 y 17 años) de edad, 
se deberá informar utilizando el Dialog alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        edad = self.txt_edad.get()
        edad_int = int(edad)
        
        if edad_int < 10:
            mensaje = "NIÑO"
        elif edad_int >= 10 and edad_int < 13:
            mensaje = "PRE-ADOLESCENTE"
        elif edad_int >= 13 and edad_int < 18:
            mensaje = "ADOLESCENTE"
        else:
            mensaje = "MAYOR"

        alert(title="Mensaje", message=mensaje)

    # ----- 6bis -----
    # A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha,
    # considerando los siguientes parametros:

    # Menos de 160 cm: Base
    # Entre 160 cm y 179 cm: Escolta
    # Entre 180 cm y 199 cm: Alero
    # 200 cm o más: Ala-Pívot o Pívot

    # PRIMER INTENTO
    def btn_mostrar_on_click(self):
        altura = self.txt_altura.get()
        altura_int = int(altura)
        
        if altura_int < 160:
            mensaje = "Base"
        elif altura_int >= 160 and altura_int < 180:
            mensaje = "Escolta"
        elif altura_int >= 180 and altura_int < 200:
            mensaje = "Alero"
        else:
            mensaje = "Ala-Pívot o Pívot"

        alert(title="Mensaje", message=mensaje)

    # SEGUNDO INTENTO
    altura = self.txt_altura.get()
        altura_int = int(altura)
        
        if altura_int < 160:
            posicion = "Base"
        elif altura_int >= 160 and altura_int < 180:
            posicion = "Escolta"
        elif altura_int >= 180 and altura_int < 200:
            posicion = "Alero"
        else:
            posicion = "Ala-Pívot o Pívot"

        mensaje = f"Su posición es {posicion}"
        
        alert(title="Mensaje", message=mensaje)
        
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
