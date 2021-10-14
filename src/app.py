from afd import automata
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from analizer import Sintactico
from models.pre_process import pre_process

if __name__ == '__main__':
    Tk().withdraw()
    filename = askopenfilename()
    file = open(filename, 'r+')
    tokens, errs = automata(file.read())
    p_tokens = pre_process(tokens)
    sintax = Sintactico(p_tokens)
    sintax.startup()
