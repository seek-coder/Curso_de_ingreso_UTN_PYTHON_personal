import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        while True:
            last_name = prompt(title="APELLIDO", prompt="Hola, somos Rising BTL. A continuación le solicitaremos algunos datos.\n\nIngrese su apellido: ")
            if last_name == None or last_name == "" or last_name.isdigit():
                alert(title="ERROR",message="No ha ingresado ningún dato o el apellido es inválido. Vuelva a intentarlo.")
                continue
            break

        while True:
            age = prompt(title="AGE", prompt="Ingrese su edad (entre 18 y 90 años inclusive): ")
            valid_age_interval = int(age) >= 18 and int(age) <= 90
            if age == None or age == "" or age.isdigit() == False or not valid_age_interval:
                alert(title="ERROR",message="No ha ingresado ningún dato o la edad no es válida. Vuelva a intentarlo.")
                continue
            break

        soltero = ["Soltero", "Soltera"]
        casado = ["Casado", "Casada"]
        divorciado = ["Divorciado", "Divorciada"]
        viudo = ["Viudo", "Viuda"]
        while True:
            civil_status = prompt(title="ESTADO CIVIL", prompt="Ingrese su estado civil: \n\n(Especifique: Soltero/a, Casado/a, Divorciado/a, Viudo/a)")
            if civil_status == None or civil_status == "" or civil_status not in soltero + casado + divorciado + viudo:
                alert(title="ERROR",message="No ha ingresado ningún dato o el estado civil no es corresponde a ninguno de la lista. Vuelva a intentarlo.")
                continue

            if civil_status in soltero:
                civil_status = "Soltero/a"
            elif civil_status in casado:
                civil_status = "Casado/a"
            elif civil_status in divorciado:
                civil_status = "Divorciado/a"
            elif civil_status in viudo:
                civil_status = "Viudo/a"
            break

        print(civil_status)

        while True:
            num_id = prompt(title="NÚMERO DE LEGAJO", prompt="Ingrese su número de legajo (de cuatro cifras y sin ceros a la izquierda): ")
            if num_id == None or num_id == "" or num_id.isdigit() == False or len(num_id) != 4 or int(num_id) < 1000:
                alert(title="ERROR",message="No ha ingresado ningún dato o el número de legajo es inválido. Vuelva a intentarlo.")
                continue
            break

        self.txt_apellido.delete(0, "end")
        self.txt_apellido.insert(0, last_name)

        self.txt_edad.delete(0, "end")
        self.txt_edad.insert(0, age)

        self.combobox_tipo.set(civil_status)

        self.txt_legajo.delete(0, "end")
        self.txt_legajo.insert(0, num_id)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
