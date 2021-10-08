from afd import automata
from tkinter import Tk
from tkinter.filedialog import askopenfilename

if __name__ == '__main__':
    Tk().withdraw()
    filename = askopenfilename()
    file = open(filename, 'r+')
    tokens = automata(file.read())
    print(tokens)