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

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #CANTIDAD DE FEMENINO
        f_sum = 0
        f_count = 0
        f_age_average = 0

        #CANTIDAD DE MASCULINO
        m_count = 0
        m_count_gio_facu = 0

        #DATOS DEL VOTANTE MÁS JOVEN QUE VOTÓ A GIANNI
        gianni_youngest_vote_name = ""
        gianni_youngest_vote_age = 0

        #RANGO TOTAL DEL FOR PRINCIPAL
        total_range = 2

        #PORCENTAJE DE VOTOS QUE RECIBIÓ CADA PARTICIPANTE
        total_vote_sum = 0
        giovanni_vote_sum = 0
        gianni_vote_sum = 0
        facu_vote_sum = 0

        for i in range(0, total_range):

            vote_name = prompt(title="", prompt="Ingrese su nombre: ")
            for i in range(100): ##100 como valor "infinito"
                if vote_name == None or vote_name == "":
                    alert(title="", message="Datos inválidos.\n\nPruebe nuevamente.")
                    vote_name = prompt(title="", prompt="Ingrese su nombre: ")

            age = prompt(title="", prompt="Ingrese su edad (mayor a 13): ")
            for i in range(100):
                if age == None or age == "" or age.isdigit() == False or int(age) <= 13:
                    alert(title="", message="Datos inválidos.\n\nPruebe nuevamente.")
                    age = prompt(title="", prompt="Ingrese su edad (mayor a 13): ")
            age_int = int(age)

            genre = prompt(title="", prompt="Ingrese su género (escriba especificamente 'Masculino', 'Femenino' u 'Otro'): ")
            for i in range(100):
                if genre == None or genre == "" or genre not in ["Masculino", "Femenino", "Otro"]:
                    alert(title="", message="Datos inválidos.\n\nPruebe nuevamente.")
                    genre = prompt(title="", prompt="Ingrese su género (escriba especificamente 'Masculino', 'Femenino' u 'Otro'): ")

            vote_negative = prompt(title="", prompt="Ingrese el voto negativo (escriba específicamente 'Giovanni', 'Gianni' o 'Facu'): ")
            for i in range(100):
                if vote_negative == None or vote_negative == "" or vote_negative not in ["Giovanni", "Gianni", "Facu"]:
                    alert(title="", message="Datos inválidos.\n\nPruebe nuevamente.")
                    vote_negative = prompt(title="", prompt="Ingrese el voto negativo (escriba específicamente 'Giovanni', 'Gianni' o 'Facu'): ")
            total_vote_sum += 1

            match vote_negative:
                case "Giovanni":
                    giovanni_vote_sum += 1
                case "Gianni":
                    gianni_vote_sum += 1
                case "Facu":
                    facu_vote_sum += 1
        
            match genre:
                case "Femenino":
                    f_count += 1
                    f_sum += age_int
                case "Masculino":
                    m_count += 1
                    if (age_int > 25 and age_int < 40) and (vote_negative == "Giovanni" or vote_negative == "Facu"):
                        m_count_gio_facu += 1

            if gianni_vote_sum == 1:
                    gianni_youngest_vote_name = vote_name
                    gianni_youngest_vote_age = age_int
            elif age_int < gianni_youngest_vote_age:
                    gianni_youngest_vote_age = age_int
                    gianni_youngest_vote_name = vote_name
        
        if f_count != 0:
            f_age_average = f_sum / f_count

        giovanni_vote_sum_percent = (giovanni_vote_sum * 100) / total_vote_sum
        gianni_vote_sum_percent = (gianni_vote_sum * 100) / total_vote_sum
        facu_vote_sum_percent = (facu_vote_sum * 100) / total_vote_sum

        if giovanni_vote_sum > gianni_vote_sum and giovanni_vote_sum > facu_vote_sum:
            most_voted = "Giovanni"
        elif gianni_vote_sum > facu_vote_sum:
            most_voted = "Gianni"
        else:
            most_voted = "Facu"
        
        final_info = f"El promedio de edad de los votantes de género Femenino es: {f_age_average}.\n\nCantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo: {m_count_gio_facu}.\n\nNombre del votante más joven que votó a Gianni: {gianni_youngest_vote_name}\n\nVotos que recibió Giovanni: {giovanni_vote_sum}, esto es, %{giovanni_vote_sum_percent:.4} de los votos.\nVotos que recibió Gianni: {gianni_vote_sum},esto es, %{gianni_vote_sum_percent:.4} de los votos\nVotos que recibió Facu: {facu_vote_sum}, esto es, %{facu_vote_sum_percent:.4} de los votos.\n\nEl nombre del participante que debe dejar la casa es: {most_voted}."

        alert(title="", message= final_info)


if __name__ == "__main__":
    app = App()
    app.mainloop()