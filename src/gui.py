from tkinter import Button, Frame, Text, Tk
from tkinter.messagebox import showerror, showinfo
from tkinter.constants import END
from tkinter.filedialog import askopenfilename
from typing import List, Tuple
from models.error_entry import ErrorEntry, SintaxError
from models.token import TokenEntry
from process.afd import automata
from process.analyzer import Sintactico
from process.extract import Extraer
from process.helpers import process_file
from process.pre_process import pre_process


class MainApp:
    def __init__(self) -> None:

        self.root = Tk()
        self.frame = Frame()

        self.root.geometry('980x640')
        self.root.resizable(0, 0)
        self.frame.place(x=0, y=0)
        self.frame.config(width=980, height=640)

        Button(self.frame, text='Abrir archivo',
               command=self.load_file).place(x=10, y=10)
        Button(self.frame, text='Analizar archivo',
               command=self.analyze_file).place(x=120, y=10)
        Button(self.frame, text='Reporte en HTML',
               command=self.show_reports).place(x=240, y=10)
        Button(self.frame,
               text='Reporte en graphviz',
               command=self.render_graphviz).place(x=360, y=10)
        Button(self.frame, text='Ejecutar', command=self.execute).place(x=500,
                                                                        y=10)

        self.file: str = ''

        self.txt_input = Text(self.frame, width=65, height=32)
        self.txt_input.place(x=10, y=60)

        self.txt_console = Text(self.frame, width=50, height=32)
        self.txt_console.place(x=560, y=60)

        self.valid_str: str = ''
        self.valid_tokens: List[TokenEntry] = []
        self.lexical_errs: List[ErrorEntry] = []
        self.sintax_errs: List[SintaxError] = []

        self.root.mainloop()

    def load_file(self):
        filename = askopenfilename()
        file = open(filename, 'r+', encoding='utf-8')

        self.file = ''
        self.txt_input.delete('1.0', END)

        self.file = file.read()
        self.txt_input.insert(END, self.file)

    def analyze_file(self):
        self.valid_str = ''
        self.valid_tokens.clear()
        self.lexical_errs.clear()
        self.sintax_errs.clear()

        txt = self.txt_input.get('1.0', END)
        tokens, errs = automata(txt)
        p_tokens = pre_process(tokens)
        sintax = Sintactico(p_tokens)
        sintax_errs = sintax.startup()

        if (not len(errs) > 0) and (not len(sintax_errs) > 0):
            self.valid_str = txt
            self.valid_tokens = p_tokens
            showinfo('OK',
                     'analisis lexico y sintactico finalizado correctamente')
        else:
            self.valid_tokens = p_tokens
            self.lexical_errs = errs
            self.sintax_errs = sintax_errs
            showerror('Error', 'Analisis lexico o sintactico a fallado')

    def show_reports(self):
        process_file(self.valid_tokens, self.lexical_errs, self.sintax_errs)

    def render_graphviz(self):
        pass

    def execute(self):
        extract: Extraer = Extraer(self.valid_tokens)
        extract.extract_claves()
        extract.extract_registros()
        extract.extract_commands()


if __name__ == '__main__':
    MainApp()