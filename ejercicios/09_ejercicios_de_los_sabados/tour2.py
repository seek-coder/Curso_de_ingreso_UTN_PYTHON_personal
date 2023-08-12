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
        higher_price_trip = None
        less_price_trip = None

        most_selected_trip_type = ""

        caminata_count = 0
        vehiculo_count = 0

        price_sum = 0

        count = 0

        while True:
            name = prompt(title="", prompt="Ingrese el nombre: ")
            while name == None or name == "" or name.isdigit() == True:
                alert(title="", message="Datos inválidos.")
                name = prompt(title="", prompt="Ingrese el nombre: ")

            age = prompt(title="", prompt="Ingrese su edad: ")
            while age == None or age == "" or age.isdigit() == False:
                alert(title="", message="Datos inválidos.")
                age = prompt(title="", prompt="Ingrese su edad: ")
            age_int = int(age)

            genre = prompt(title="", prompt="Ingrese su sexo(Masculino, Femenino u Otro): ")
            while genre != "Masculino" and genre != "Femenino" and genre != "Otro":
                alert(title="", message="Datos inválidos.")
                genre = prompt(title="", prompt="Ingrese su sexo(Masculino, Femenino u Otro): ")
            
            height = prompt(title="", prompt="Ingrese su altura en CM: ")
            while height == None or height == "" or height.isdigit() == False:
                alert(title="", message="Datos inválidos.")
                height = prompt(title="", prompt="Ingrese su altura: ")
            height_int = int(height)
            
            if height_int < 140:
                height_info = "pequeño (menor a 140cm)"
            elif height_int < 170:
                height_info = "del promedio (entre 140 y 170cm)"
            elif height_int < 190:
                height_info = "es alto (entre 170 y 190cm)"
            else:
                height_info = "es MUY alto! (mas de 190cm)"

            info_message = f"Usted es {name}, tiene {age_int} años de edad y su sexo es {genre},\n\nUsted es{height_info}"
    
            alert(title="", message=info_message)

            trip_amount = prompt(title="", prompt="Elija la cantidad de excursiones a realizar (no menor a 0 y no mayor a 11):")
            while trip_amount == None or trip_amount == "" or trip_amount.isdigit() == False or int(trip_amount) < 0 or int(trip_amount) > 11:
                alert(title="", message="Datos inválidos.")
                trip_amount = prompt(title="", prompt="Elija la cantidad de excursiones a realizar (no menor a 0 y no mayor a 11):")
            trip_amount_int = int(trip_amount)

            trip_price = prompt(title="", prompt="Elija el precio: ")
            while trip_price == None or trip_price == "" or trip_price.isdigit() == False:
                alert(title="", message="Datos inválidos.")
                trip_price = prompt(title="", prompt="Eliga el precio: ")
            trip_price_int = int(trip_price)
            price_sum += trip_price_int

            trip_type = prompt(title="", prompt="Elija el tipo de excursión(caminata o vehículo): ")
            while trip_type != "caminata" and trip_type != "vehículo":
                alert(title="", message="Datos inválidos.")
                trip_type = prompt(title="", prompt="Elija el tipo de excursión(caminata o vehículo): ")

            if trip_type == "caminata":
                caminata_count += 1
            elif trip_type == "vehículo":
                vehiculo_count += 1
            
            if higher_price_trip == None or trip_price_int > higher_price_trip:
                higher_price_trip = trip_price_int
            
            if less_price_trip == None or trip_price_int < less_price_trip:
                less_price_trip = trip_price_int

            count += 1

            if caminata_count > vehiculo_count:
                most_selected_trip_type = "Caminata"
            elif vehiculo_count > caminata_count:
                most_selected_trip_type = "Vehiculo"
            else:
                most_selected_trip_type = "Empate"

            print(higher_price_trip)
            
            cancel = question(title="", message="¿Continuar ingresando datos?")
            if cancel == False:
                break

        if count > 0:
            average_price = price_sum / count

        final_info_message = f"Precio más caro es {higher_price_trip} y precio más barato es {less_price_trip}.\n\nEl promedio de precios es {average_price}.\n\nEl tipo de excursión más seleccionada es: {most_selected_trip_type}."

        alert(title="", message=final_info_message)
        
        

    
if __name__ == "__main__":
    app = App()
    app.mainloop()