from tkinter import Button, Frame, Text, Tk


class MainApp:
    def __init__(self) -> None:
        self.root = Tk()
        self.frame = Frame()

        self.root.geometry('720x480')
        self.root.resizable(0, 0)
        self.frame.place(x=0, y=0)
        self.frame.config(width=720, height=480)

        Button(self.frame, text='Abrir archivo').place(x=10, y=10)
        Button(self.frame, text='Analizar archivo').place(x=120, y=10)
        Button(self.frame, text='Reporte en HTML').place(x=240, y=10)
        Button(self.frame, text='Reporte en graphviz').place(x=360, y=10)

        txt_input = Text(self.frame, width=45, height=25)
        txt_input.place(x=10, y=60)

        txt_console = Text(self.frame, width=40, height=25)
        txt_console.place(x=380, y=60)

        self.root.mainloop()

    def load_file():
        pass


if __name__ == '__main__':
    MainApp()