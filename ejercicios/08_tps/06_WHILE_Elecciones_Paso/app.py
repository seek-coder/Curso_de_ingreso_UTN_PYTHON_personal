'''
Braian Catriel Gatto
--------
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

e. se pide ingresar el sexo (M , F , NB) , informar cuantos candidatos hay de cada sexo

f. se pide ingresar nivel de aceptacion de imagen del candidato (entre -100 y 100) informar el
nombre y sexo del que mejor nivel tiene 

g.de las personas de sexo femenino ,informar cuanta hay mayores a 50 y cuantas menores a esa edad

Todos los datos se ingresan por prompt y los resultados por consola (print)

h. de que sexo hubo mas candidatos
'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        #1) INICIALIZACIÓN DE VARIABLES
        most_voted_name = ""
        most_voted_count = None
        less_voted_name = ""
        less_voted_count = None
        less_voted_age = None

        age_average = 0

        age_acc = 0

        vote_sum = 0

        m_count = 0
        f_count = 0
        nb_count = 0

        best_accept_rate_name = ""
        best_accept_rate = None
        best_accept_rate_genre = ""

        f_above_50years = 0
        f_beyond_50years = 0

        most_genre_quantity = ""

        count = 0

        #2) PROCESO PRINCIPAL
        while True:
                initial_name = prompt(title="NOMBRE DE CANDIDATO", prompt= f"Ingrese el nombre:\n\nCantidad de candidatos ingresados: {count}")
                while initial_name == None or initial_name == "" or initial_name.isdigit() == True:
                    alert(title="ERROR",message="No ha ingresado ningún dato o el nombre es inválido. Vuelva a intentarlo.")
                    initial_name = prompt(title="NOMBRE DE CANDIDATO", prompt= "Ingrese el nombre: ")

                age = prompt(title="EDAD", prompt="Ingrese la edad (mayor a 25 años): ")
                while age == None or age == "" or age.isdigit() == False or int(age) <= 25:
                    alert(title="ERROR",message="No ha ingresado ningún dato o la edad no es válida. Vuelva a intentarlo.")
                    age = prompt(title="EDAD", prompt="Ingrese la edad (mayor a 25 años): ")
                age_int = int(age)
                age_acc += age_int

                vote = prompt(title="CANTIDAD DE VOTOS", prompt="Ingrese la cantidad de votos: ")
                while vote == None or vote == "" or vote.isdigit() == False or int(vote) <= 0:
                    alert(title="ERROR",message="No ha ingresado ningún dato o la cantidad de votos es inválida. Vuelva a intentarlo.")
                    vote = prompt(title="CANTIDAD DE VOTOS", prompt="Ingrese la cantidad de votos: ")
                vote_int = int(vote)
                vote_sum += vote_int

                genre = prompt(title="GÉNERO", prompt="Ingrese el género ('M', 'F', o 'NB' según corresponda): ")
                while genre == None or genre == "" or genre not in ["M", "F", "NB"]:
                    alert(title="ERROR",message="No ha ingresado ningún dato o el género no ha sido especificado. Vuelva a intentarlo.")
                    genre = prompt(title="GÉNERO", prompt="Ingrese el género ('M', 'F', o 'NB' según corresponda): ")

                accept_rate = prompt(title="NIVEL DE ACEPTACIÓN DE IMÁGEN", prompt="Ingrese el nivel de aceptación de imágen del candidato (entre -100 y 100): ")
                while accept_rate == None or accept_rate == "" or int(accept_rate) < -100 or int(accept_rate) > 100:
                    alert(title="ERROR",message="No ha ingresado ningún dato o nivel de aceptación no está dentro de los límites aceptados. Vuelva a intentarlo.")
                    accept_rate = prompt(title="NIVEL DE ACEPTACIÓN DE IMÁGEN", prompt="Ingrese el nivel de aceptación de imágen del candidato (entre -100 y 100): ")
                accept_rate_float = float(accept_rate)

                count += 1

                if count == 1:
                    most_voted_name = initial_name
                    most_voted_count = vote_int

                    less_voted_name = initial_name
                    less_voted_count = vote_int
                    less_voted_age = age_int

                    best_accept_rate_name = initial_name
                    best_accept_rate = accept_rate_float
                    best_accept_rate_genre = genre
                else:
                    if vote_int > most_voted_count:
                            most_voted_name = initial_name
                    elif vote_int < less_voted_count:
                            less_voted_name = initial_name
                            less_voted_age = age_int
                            
                    if accept_rate_float > best_accept_rate: # lo evaluo aparte para no verse afectado por las condiciones de maximo y minimo del conteo de votos
                            best_accept_rate_name = initial_name
                            best_accept_rate_genre = genre

                match genre:
                    case "M":
                        m_count += 1
                    case "F":
                        f_count += 1
                    case "NB":
                        nb_count += 1

                if genre == "F" and age_int > 50:
                    f_above_50years += 1
                elif genre == "F" and age_int < 50:
                    f_beyond_50years += 1

                cancel = question(title="CONFIRMACIÓN", message="¿Quiere seguir ingresando datos?")
                if cancel == False:
                    break

        #SE ROMPE EL BUCLE

        #3) OPERACIONES QUE LA COMPUTADORA SÓLO DEBE HACER UNA VEZ, AL FINAL:

        #CAMBIADO EL IF POR MATCH:
        age_average = age_acc / count
        

        if m_count > f_count and m_count > nb_count:
            most_genre_quantity = "Masculino"
        elif f_count > m_count and f_count > nb_count:
            most_genre_quantity = "Femenino"
        else:
            most_genre_quantity = "No binarix"

        print("candidato más votado: " + most_voted_name + "\n" 
                    "candidato menos votado y su edad: " + less_voted_name + " " + str(less_voted_age) + "\n"
                    "promedio de edad de candidatos: " + str(age_average) + "\n"
                    "total de votos emitidos: " + str(vote_sum) + "\n"
                    "cantidad de masculinos: " + str(m_count) + "\n"
                    "cantidad de femeninas: " + str(f_count) + "\n"
                    "cantidad de no binarixs: " + str(nb_count) + "\n"
                    "candidato con nivel de aceptación más alto y género: " + best_accept_rate_name + " " + best_accept_rate_genre + "\n"
                    "cantidad de femeninas mayores a 50 años: " + str(f_above_50years) + "\n"
                    "cantidad de femeninas menores a 50 años: " + str(f_beyond_50years) + "\n"
                    "hay mas candidatos del género: " + most_genre_quantity +"\n\n")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
