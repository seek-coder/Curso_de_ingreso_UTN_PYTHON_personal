import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón 'MÁXIMO' se analizará el vector lista_datos a efectos de determinar cuál es el número 
más grande allí contenido el cual deberá ser informado utilizando Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="MÁXIMO", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]


    def btn_calcular_on_click(self):
        max_num = None

        for i in self.lista_datos:
            if max_num == None or max_num < i:
                max_num = i

        alert(title="", message=f"El número más grande de la lista es: {max_num}")
'''
        count = 0

        for i in self.lista_datos:
            if count == 0:
                max_num = i
                min_num = i
            else:
                if i > max_num:
                    max_num = i
                elif i < min_num:
                    min_num = i
            count += 1
        alert(title="", message=f"El número más grande de la lista es: {max_num}")
        #print(max_num, min_num)
'''


if __name__ == "__main__":
    app = App()
    app.mainloop()