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

        self.lista = [5, -1, 2, 10, 0, 0, -9, 0, 10]

    def btn_comenzar_ingreso_on_click(self):
        while True:
            num = prompt(title="", prompt="Ingrese un número: ")
            if num == None:
                break
            num_int = int(num)
            self.lista.append(num_int)
            print(self.lista)


    def btn_mostrar_estadisticas_on_click(self):
        positive_sum = 0
        negative_sum = 0

        positive_count = 0
        negative_count = 0
        zero_count = 0

        positive_max = None
        negative_min = None

        even_list = []
        higher_num_list = []

        for i in self.lista:
            if i < 0:
                negative_sum += i
                negative_count += 1
                if negative_min == None or i < negative_min:
                    negative_min = i
            elif i > 0:
                positive_sum += i
                positive_count += 1
                if positive_max == None or i > positive_max:
                    positive_max = i
                    higher_num_list = []
                    higher_num_list.append(positive_max)
                elif i == positive_max:
                    higher_num_list.append(positive_max)
            else:
                zero_count += 1

            if i % 2 == 0:
                even_list.append(i)
            

            print(positive_sum, negative_sum, positive_count, negative_count, zero_count, positive_max, negative_min)

        if negative_count > 0:
            negative_average = negative_sum / negative_count

        if positive_count > negative_count and positive_count > zero_count:
            most_input = "Positivo"
        elif negative_count > zero_count:
            most_input = "Negativo"
        else:
            most_input = "Cero"

        info_message = f"La suma acumulada de los negativos es: {negative_sum}\n\nLa suma acumulada de los positivos es: {positive_sum}\n\nCantidad de números positivos ingresados: {positive_count}\n\nCantidad de números negativos ingresados: {negative_count}\n\nCantidad de ceros: {zero_count}\n\nEl minimo de los negativos: {negative_min}\n\nEl maximo de los positivos: {positive_max}\n\nEl promedio de los negativos es: {negative_average}\n\nListado de numeros pares: {even_list}\n\nTipo de numero mas ingresado: {most_input}\n\nLista de mayores: {higher_num_list}"

        alert(title="" ,message=info_message)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
