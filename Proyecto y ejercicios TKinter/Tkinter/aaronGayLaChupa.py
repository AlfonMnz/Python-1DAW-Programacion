import tkinter


class Biyounds(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent,width=90)


        self.pack()
        self.parent = parent
        self.variablity = tkinter.DoubleVar()
        self.iniciar_hub()

    def iniciar_hub(self):

        textito = tkinter.Label(self, text="achulichulichú", )
        textito.pack()


root = tkinter.Tk()
app = Biyounds(root)
root.mainloop()
