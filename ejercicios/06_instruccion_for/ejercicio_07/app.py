import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Braian Catriel Gatto
-----
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #DIVISOR DE UN NÚMERO: NÚMERO QUE PERMITE DIVIDIR A OTRO CON RESTO 0
        div_len = None
        div_num_list = []

        num = prompt(title="", prompt="Ingrese un número: ")
        num_int = int(num)
        for i in range(1, (num_int + 1)):
            if num_int % int(i) == 0:
                div_num_list.append(i)
        div_len = len(div_num_list)
        #print(div_num_list, div_len)
        alert(title="", message=f"Números divisores: {div_num_list}\n\nCantidad de números divisores encontrados: {div_len}")

    
if __name__ == "__main__":
    app = App()
    app.mainloop()