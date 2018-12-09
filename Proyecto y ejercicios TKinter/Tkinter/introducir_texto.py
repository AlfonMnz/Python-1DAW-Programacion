"""
Vamos a crear un conversor de temperaturas que se le pide un dato
"""
import tkinter


class Conversor:
    def __init__(self):
        self.root = tkinter.Tk()

        self.button_fah = tkinter.Button(self.root, text="a Fahrenheit", command=self.convertir,width=8)
        self.biyounds = tkinter.DoubleVar()
        self.entrada = tkinter.Entry(self.root, textvariable=self.biyounds)
        self.resultado = 0
        self.result = tkinter.Label(self.root, text=self.resultado)
        self.button_kelvin= tkinter.Button(self.root, text="a Kelvin", command=self.convertir,width=8)
        self.button_celsius = tkinter.Button(self.root, text="a Celsius", command=self.convertir,width=8)
        self.empaquetar()


    def empaquetar(self):
        self.button_fah.grid(column=0,row=0)
        self.button_celsius.grid(column=0,row=1)
        self.button_kelvin.grid(column=0,row=2)
        self.entrada.grid(column=1,row=0)
        self.result.grid(column=2,row=2)

    def convertir(self):
        self.temperatura = self.biyounds.get()
        self.celsius = (self.temperatura - 32) * (5 / 9)
        self.result.config(text="El resultado es: {}".format(self.celsius))


c = Conversor()
c.root.mainloop()
