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
        #INICIALIZACIÓN DE VARIABLES
        most_voted_name = ""
        most_voted_acc = None

        less_voted_name = ""
        less_voted_acc = None
        less_voted_age = 0

        age_sum = 0

        vote_sum = 0

        m_count = 0
        f_count = 0
        nb_count = 0

        most_accept_name = ""
        most_accept_acc = None

        f_higher_50 = 0
        f_less_50 = 0

        count = 0

        #INGRESO DE DATOS
        while True:
            name = prompt(title="", prompt="Ingrese el nombre: ")
            while name == None or name == "" or name.isdigit() == True:
                alert(title="", message="Datos inválidos.")
                name = prompt(title="", prompt="Ingrese el nombre: ")

            age = prompt(title="", prompt="Ingrese la edad(mayor a 25): ")
            while int(age) <= 25:
                alert(title="", message="Datos inválidos.")
                age = prompt(title="", prompt="Ingrese la edad(mayor a 25): ")
            age_int = int(age)
            age_sum += age_int

            votes = prompt(title="", prompt="Ingrese la cantidad de votos (no menos a cero): ")
            while int(votes) < 0:
                alert(title="", message="Datos inválidos.")
                votes = prompt(title="", prompt="Ingrese la cantidad de votos (no menos a cero): ")
            votes_int = int(votes)
            vote_sum += votes_int

            genre = prompt(title="", prompt="Ingrese el sexo (M, F, NB): ")
            while genre != "M" and genre != "F" and genre != "NB":
                alert(title="", message="Datos inválidos.")
                genre = prompt(title="", prompt="Ingrese el sexo (M, F, NB): ")

            match genre:
                case "M":
                    m_count += 1
                case "F":
                    f_count += 1
                    if age_int > 50:
                        f_higher_50 += 1
                    elif age_int < 50:
                        f_less_50 += 1
                case "NB":
                    nb_count += 1
            
            accept_rate = prompt(title="", prompt="Ingrese el nivel de aceptación de imagen (entre -100 y 100): ")
            while int(accept_rate) < -100 or int(accept_rate) > 100:
                alert(title="", message="Datos inválidos.")
                accept_rate = prompt(title="", prompt="Ingrese el nivel de aceptación de imagen (entre -100 y 100): ")
            accept_rate_int = int(accept_rate)

            count += 1

            if most_voted_acc == None or votes_int > most_voted_acc:
                most_voted_acc = votes_int
                most_voted_name = name
            
            if less_voted_acc == None or votes_int < less_voted_acc:
                less_voted_acc = votes_int
                less_voted_name = name
                less_voted_age = age_int

            if most_accept_acc == None or accept_rate_int > most_accept_acc:
                most_accept_acc = accept_rate_int
                most_accept_name = name
                most_accept_genre = genre
            print(name, age, votes_int, genre, accept_rate_int)
            cancel = question(title="", message="¿Desea continuar?")
            if cancel == False:
                break

        #PROMEDIO FUERA DEL WHILE
        if count > 0:
            age_average = age_sum / count
        
        #DIFERENCIA ENTRE CANTIDAD DE GÉNEROS
        if m_count > f_count and m_count > nb_count:
            most_genre = "Masculino"
        elif f_count > nb_count:
            most_genre = "Femenino"
        else:
            most_genre = "No Binario"
        #INFORME DE DATOS

        #INFORME POR PRINT
        print(f"Nombre del cantidato con más votos: {most_voted_name}, Nombre y edad del candidatos con menos votos {less_voted_name} | {less_voted_age}, Promedio de edad de los cndaditos: {age_average}, Total de votos emitidos: {vote_sum}, Total de candidatos de cada sexo: M = {m_count} | F = {f_count} | NB = {nb_count}, Nombre y sexo del mejor candidato segun aceptación: {most_accept_name} | {most_accept_genre}, Sexo femenino mayores a 50 y menores a 50: {f_higher_50} | {f_less_50}, De que sexo hubo más candidatos: {most_genre}")




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
