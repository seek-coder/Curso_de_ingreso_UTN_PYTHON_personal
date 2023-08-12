import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Braian Catriel Gatto
-----
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                            columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                            columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        while True:
            ask_number = prompt(title="NÚMERO", prompt="Ingrese un número: ")
            if ask_number == None:
                break
            elif ask_number == "" or ask_number.lstrip("-").isdigit() == False:
                alert(title="ERROR", message="Datos inválidos.\n\nIntentelo de nuevo.")
            ask_number_int = int(ask_number)
            self.lista.append(ask_number_int)
            #print(self.lista)


    def btn_mostrar_estadisticas_on_click(self):
        negative_sum = 0
        positive_sum = 0

        negative_count = 0
        positive_count = 0
        zero_count = 0

        min_negative_num = None
        max_positive_num = None

        even_list = []
        highest_num_list = []

        for i in self.lista:
            if i < 0:
                negative_sum += i #SUMA ACUMULADA DE NEGATIVOS
                negative_count += 1 #CANTIDAD DE NEGATIVOS
                if min_negative_num == None or  i > min_negative_num: #MÍNIMO DE NEGATIVOS ¿el menor es el más cercano al 0?
                    min_negative_num = i
            elif i > 0:
                positive_sum += i #SUMA ACUMULADA DE POSITIVOS
                positive_count += 1 #CANTIDAD DE POSITIVOS
                if max_positive_num == None or i > max_positive_num: #MÁXIMO DE POSITIVOS
                    max_positive_num = i
                    highest_num_list = [] #RESETEAR LISTA
                    highest_num_list.append(max_positive_num) #AGREGAR MAYOR A LA LISTA
                elif i == max_positive_num:
                    highest_num_list.append(max_positive_num) #AGREGAR MAYOR A LA LISTA
            else:
                zero_count += 1

            if i % 2 == 0:
                even_list.append(i)
    
        if negative_count > 0: #VALIDAR QUE LA DIVISIÓN NO SEA CON 0 DE DENOMINADOR
            negative_average = negative_sum / negative_count

        if negative_count > positive_count and negative_count > zero_count:
            most_entered = "Negativo"
        elif positive_count > negative_count:
            most_entered = "Positivo"
        else:
            most_entered = "Cero"

        result_info = f"La suma acumulada de los negativos es {negative_sum}.\n\nLa suma acumulada de los positivos es {positive_sum}\n\nLa cantidad de números positivos ingresados es {positive_count}, de negativos es {negative_count} y de ceros es {zero_count}.\n\nEl mínimo de los negativos es {min_negative_num} y el máximo de los positivos es {max_positive_num}.\n\nEl promedio de los negativos es {negative_average}\n\nLa lista de números pares es {even_list}\n\nEl tipo de número más ingresado es {most_entered}\n\nEl lista de los números mayores es: {highest_num_list}"

        alert(title="INFORME DE RESULTADOS", message= result_info)

        #print(negative_sum, positive_sum, negative_count, positive_count, zero_count, min_negative_num, max_positive_num, negative_average, sep="\n")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
