import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

'''
Se deben pedir los siguientes datos de un tour  de vacaciones a un destino en particular


1 -nombre , edad y sexo de una persona, mostrar el mensaje , "usted es  xxxx tiene xx de edad y susexo es xxx"

2 -pedir la altura de la persona e informar si es bajo menor a 140 cm,  
medio entre 140 y 170 cm , alto hasta 190 cm y muy alto para mayores a esa altura.1


3- validar todos los datos

4- en las vacaciones se pueden seleccionar distintas excursiones para realizar , 
se pueden hacer desde 0 excursión a 11 excursiones

5- una vez ingresada la cantidad se debe pedir por cada excursión 
el importe y el tipo de excursión(caminata  o vehículo). 
informar cual es el precio más caro el más barato y el promedio

6- informar cual es el tipo de excursión(caminata  o vehículo). 
más seleccionada o si se seleccionó las mismas veces (caminata  o vehículo)


'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Tour", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
            while True: 
                name = prompt(title="NOMBRE", prompt="Ingrese su nombre: ")
                if name == None or name == "" or name.isdigit() is True:
                    alert(title="ERROR", message="Nombre inválido. Ingreselo nuevamente.")
                    continue
                break

            while True:
                age = prompt(title="EDAD", prompt="Ingrese su edad (en números): ")
                if age == None or age == "" or age.isdigit() is False:
                    alert(title="ERROR", message="Edad inválida. Ingresela nuevamente.")
                    continue
                break

            while True:
                genre = prompt(title="GÉNERO", prompt="Especifique su género (Masculino/Femenino/Otro): ")
                if genre == None or genre == "" or genre not in ["Masculino", "Femenino", "Otro"]:
                    alert(title="ERROR", message="Género inválido. Escriba exactamente una de las tres opciones.")
                    continue
                break
            
            first_message = f"Hola. Usted es {name}, tiene {age} años de edad y su género es {genre}.\n\n"

            while True:
                height = prompt(title="ALTURA", prompt="Ingrese su altura (en CM): ")
                if height == None or height == "" or height.isdigit() is False:
                    alert(title="ERROR", message="Altura inválida. Ingresela nuevamente.")
                    continue

                height_float = float(height)
                if height_float < 140:
                    height_info = f"Ud. es una persona de baja estatura ({height_float}cm)."
                elif  height_float <= 170:
                    height_info = f"Ud. es una persona de estatura promedio ({height_float}cm)."
                elif  height_float <= 190:
                    height_info = f"Ud. es una persona alta ({height_float}cm)."
                else:
                    height_info = f"¡Es Ud. muy alto! ({height_float}cm)."
                break

            alert(title="VALIDACIÓN DE DATOS", message= first_message + height_info)

            while True:
                trip = prompt(title="EXCURSIÓN", prompt="Escriba cuántas excursiones realizará, donde 0 es el mínimo (ninguna) y 11 el máximo: ")
                if trip == None or trip == "" or trip.isdigit() is False:
                    alert(title="ERROR", message="Escriba la cantidad de excursiones comprendida entre 0 y 11.")
                    continue
                trip_int = int(trip)
                if trip_int < 0 or trip_int > 11:
                    alert(title="ERROR", message="Eliga un número de excursiones entre 0 y 11.")
                    continue
                break
                
            count = 0
            high_price = None
            low_price = None
            high_price_type = ""
            low_price_type = ""
            total_price = 0
            while count < trip_int:
                price = prompt(title="IMPORTE", prompt="Ingrese su importe (en números): ")
                if price == None or price == "" or not price.isdigit():
                    alert(title="CANCELAR", message="Escriba el importe.")
                    continue
                price_int = int(price)

                trip_type = prompt(title="TIPO DE VIAJE", prompt="Ingrese el tipo de excursión (caminata/vehiculo): ")
                if trip_type == None or trip_type == "" or trip_type not in ["caminata", "vehiculo"]:
                    alert(title="CANCELAR", message="Escriba específicamente el tipo de excursión.")
                    continue

                if low_price == None or price_int < low_price:
                    low_price = price_int
                    low_price_type = trip_type
                
                if high_price == None or price_int > high_price:
                    high_price = price_int
                    high_price_type = trip_type

                total_price += price_int
                count += 1

            average_price = total_price / trip_int
            info = f"El precio más caro es ${high_price}, el más barato es ${low_price} y el promedio es ${average_price}\n\nEl precio total es de ${total_price}"
            alert
            alert(title="DESCRIPCIÓN DEL VIAJE", message=info)







if __name__ == "__main__":
    app = App()
    app.mainloop()