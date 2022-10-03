from tkinter import ttk
from tkinter import *

class Cliente:
    def __init__(self, root):
        self.wind = root
        self.wind.title("RECIBO")
        self.wind.geometry("850x600")
        self.wind.config(bg="teal")

        frame1 = LabelFrame(self.wind, text="Datos del cliente", font=("calibri", 14))
        frame2 = LabelFrame(self.wind, text="Informacion", font=("calibri", 14))



if __name__ == '__main__':
    root = Tk()
    Cliente = Cliente(root)
    root.mainloop()


