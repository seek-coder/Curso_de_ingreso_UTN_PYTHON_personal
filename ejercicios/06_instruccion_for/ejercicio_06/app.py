import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Braian Catriel Gatto
-----
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        even_num_list = [1]

        num = prompt(title="", prompt="Ingrese un número: ")
        num_int = int(num)
        for i in range(1, (num_int + 1)):
            if i % 2 == 0:
                even_num_list.append(i)
        even_num_list_length = len(even_num_list) - 1
        alert(title="", message=f"Números pares desde el 1 hasta el número ingresado: {even_num_list} \n\nCantidad de pares: {even_num_list_length}")
    
if __name__ == "__main__":
    app = App()
    app.mainloop()