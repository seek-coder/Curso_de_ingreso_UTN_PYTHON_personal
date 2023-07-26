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
        #DATOS DEL MÁS VOTADO
        most_voted_name = "" #CANDIDATO MÁS VOTADO IGUALADO A "" PORQUE SI O SI VA A SER UN STRING
        most_voted_count = None #CANTIDAD MÁS ALTA DE VOTOS IGUALADA A NONE || LA EVALúO A NONE Y NO A 0 PORQUE ES LA FORMA CORRECTA DE ESPECIFICAR LA AUSENCIA DE VALORES, Y YO LO QUE NECESITO NO ES SUMAR SINO REEMPLAZAR; SI LA VARIABLE LA INICIALIZO EN 0 LE ESTOY DANDO UN VALOR, QUE ES 0

        #DATOS DEL MENOS VOTADO
        less_voted_name = ""
        less_voted_count = None
        less_voted_age = None

        #SUMA DE EDADES PARA SACAR EL PROMEDIO
        age_sum = 0 #ACÁ INICIALIZO EN 0 PARA PODER SUMAR LAS EDADES

        #ACUMULADOR DE VOTOS
        votes_sum = 0

        #CONTADOR
        count = 0 #ME SIRVE PARA LA LINEA 51 Y EN LUGAR DEL FLAG PARA IGUALAR MÍNIMOS Y MÁXIMOS EN LA PRIMERA VUELTA

        while True:
            #INGRESO DE DATOS Y VALIDACIÓN
            name = prompt(title="NOMBRE", prompt=f"Ingrese el nombre: \n\nCantidad de candidatos ingresados: {count}") #USO ESTE PROMPT PARA INFORMAR CUANTOS CANDIDATOS HAN SIDO INGRESADOS HASTA EL MOMENTO
            while name == None or name == "" or name.isdigit() == True: #TRIPLE VALIDACIÓN: None, vacío y dígito
                alert(title="ERROR", message="Datos inválidos.\n\nIntente nuevamente.")
                name = prompt(title="EDAD", prompt="Ingrese el nombre: ")
            
            age = prompt(title="EDAD", prompt="Ingrese la edad (mayor a 25): ")
            while age == None or age == "" or age.isdigit() == False or int(age) <= 25: #TRIPLE VALIDACIÓN: None, vacío y dígito + VALIDACIÓN DE INTERVALO
                alert(title="ERROR", message="Datos inválidos.\n\nIntente nuevamente.")
                age = prompt(title="EDAD", prompt="Ingrese la edad: ")
            age_int = int(age)
            age_sum += age_int

            votes = prompt(title="VOTOS", prompt="Ingrese la cantidad de votos (no menor a cero): ")
            while votes == None or votes == "" or votes.isdigit() == False or int(votes) < 0: #TRIPLE VALIDACIÓN: None, vacío y dígito + VALIDACIÓN DE INTERVALO
                alert(title="ERROR", message="Datos inválidos.\n\nIntente nuevamente.")
                votes = prompt(title="VOTOS", prompt="Ingrese la cantidad de votos (no menor a cero): ")
            votes_int = int(votes) #IMPORTANTE! SINO LA COMPARACIÓN ENTRE CANTIDAD DE VOTOS Y CUALQUIER OTRA COSA NO VA A SERVIR DESPUÉS DE LA PRIMERA VUELTA
            votes_sum += votes_int
            
            count += 1 

            if count == 1: #EN LA PRIMERA VUELTA SÓLO HAY UN CANDIDATO, ENTONCES EN LA PRIMERA VUELTA ÉL SERÁ TANTO EL MENOS COMO EL MÁS VOTADO Y LO PODEMOS USAR PARA COMPARAR LOS DEMÁS
                most_voted_name = name #REEMPLAZAR VARIABLE DE MÁS VOTADO POR EL PRIMER CANDIDATO
                most_voted_count = votes_int #REEMPLAZAR VARIABLE DE CANTIDAD DE VOTOS MÁXIMA POR LOS VOTOS DEL PRIMER CANDIDATO

                less_voted_name = name
                less_voted_count = votes_int
                less_voted_age = age_int

            elif votes_int > most_voted_count: #¡¡¡CONSIGNA (A)!!!
                    most_voted_name = name
            elif votes_int < less_voted_count: #¡¡¡CONSIGNA (B)!!!
                    less_voted_name = name
                    less_voted_age = age_int

            average_age = age_sum / count #DONDE EL DENOMINADOR CORRESPONDE A LA CANTIDAD DE VUELTAS || ¡¡¡CONSIGNA (C)!!!
            
            cancel = question(title="CONFIRMACIÓN", message="¿Continuar ingresando datos?") #CONFIRMAR SI SEGUIR O NO EL BUCLE
            if cancel == False:
                print("El candidato más votado es: " + most_voted_name,"El candidato con menos votos y su edad es: " + less_voted_name + " " + str(less_voted_age), "El promedio de edades de los candidatos es: " + str(average_age), "La cantidad de votos emitidos es de: " + str(votes_sum), sep = "\n") #ACÁ LA CONSOLA SÓLO SE VA A MOSTRAR AL CANCELAR EL QUESTION
                break
            

            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
