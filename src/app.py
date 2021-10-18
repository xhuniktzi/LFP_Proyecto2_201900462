from helpers import process_file
from afd import automata
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from analizer import Sintactico
from pre_process import pre_process

if __name__ == '__main__':
    Tk().withdraw()
    filename = askopenfilename()
    file = open(filename, 'r+', encoding='utf-8')
    tokens, errs = automata(file.read())
    p_tokens = pre_process(tokens)
    if not len(errs) > 0:
        sintax = Sintactico(p_tokens)
        sintax_errs = sintax.startup()
        process_file(p_tokens, errs, sintax_errs)