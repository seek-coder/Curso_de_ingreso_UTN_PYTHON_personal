import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Braian Catriel Gatto
-----
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #NUMERO PRIMO: ENTERO CON SÓLO DOS DIVISORES, O SEA, EL 1 Y SÍ MISMO
        #EJEMPLOS DE NUMERO PRIMO: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89
            num = prompt(title="", prompt="Ingrese un número: ")
            num_int = int(num)

            count = 0

            for i in range(2, num_int): #EMPIEZO EN 2 Y NO EN 1 PORQUE EL 1 QUEDA ES DIVISOR DE UN NUMERO PRIMO, AL IGUAL QUE NUM_INT
                print(num_int % i)
                if num_int % i == 0:
                    count += 1 #SI EN ALGÚN MOMENTO UN RESTO ES 0, EL CONTADOR AUMENTA EN UNO, LO QUE SIGNIFICA QUE YA AL HABER OTRO NÚMERO APARTE DEL 1 Y DE SÍ MISMO QUE DE RESTO 0, EL NÚMERO NO ES PRIMO
            if count == 0:
                info_num = f"El número {num_int} es primo"
            else:
                info_num = f"El número {num_int} no es primo"
            
            alert(title="", message=info_num)
            


    
if __name__ == "__main__":
    app = App()
    app.mainloop()