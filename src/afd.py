import re


def automata(input: str):
    # define regex
    L = re.compile(r'[A-Za-z_-]')
    E = re.compile(r'[^\n\']')
    D = re.compile(r'[0-9]')
    T = re.compile(r'[\s\n\t]')
    S = re.compile(r'[;,=\(\)\[\]\{\}]')

    input += '\n'  # fix EOF error
    tokens: list = []
    errs: list = []
    state: int = 0
    lex: str = ''
    index: int = 0
    row: int = 1
    col: int = 1

    while index < len(input):
        char = input[index]

        if state == 0:

            if L.search(char):
                state = 1
                index += 1
                col += 1
                lex += char
            elif re.search(r"[#]", char):
                state = 2
                index += 1
                col += 1
                lex += char
            elif re.search(r"[']", char):
                state = 3
                index += 1
                col += 1
                lex += char
            elif re.search(r'["]', char):
                state = 4
                index += 1
                col += 1
                lex += char
            elif D.search(char):
                state = 5
                index += 1
                col += 1
                lex += char
            elif S.search(char):
                state = 6
                index += 1
                col += 1
                lex += char
            else:
                index += 1

        elif state == 1:

            if L.search(char):
                index += 1
                col += 1
                lex += char
            else:
                tokens.append(lex)
                lex = ''
                state = 0
        elif state == 2:

            if re.search(r"[\n]", char):
                state = 7
                index += 1
                col = 1
                row += 1
                lex += char
            if E.search(char) or re.search(r"[']", char):
                index += 1
                col += 1
                lex += char

            elif char == re.search(r'[\n]', char):
                state = 7
                index += 1
                col = 1
                row += 1
                lex += char
        elif state == 3:

            if re.search(r"[']", char):
                state = 8
                index += 1
                col += 1
                lex += char
        elif state == 4:

            if re.search(r'["]', char):
                state = 9
                index += 1
                col += 1
                lex += char
            elif E.search(char) or re.search(r"[']", char):
                index += 1
                col += 1
                lex += char

        elif state == 5:

            if re.search(r'[.]', char):
                state = 10
                index += 1
                col += 1
                lex += char
            elif D.search(char):
                index += 1
                col += 1
                lex += char
            else:
                tokens.append(lex)
                lex = ''
                state = 0
        elif state == 6:

            tokens.append(lex)
            lex = ''
            state = 0
        elif state == 7:

            tokens.append(lex)
            lex = ''
            col = 1
            row += 1
            state = 0
        elif state == 8:

            if re.search(r"[']", char):
                state = 11
                index += 1
                col += 1
                lex += char
        elif state == 9:

            tokens.append(lex)
            lex = ''
            state = 0
        elif state == 10:

            if D.search(char):
                state = 12
                index += 1
                col += 1
                lex += char
        elif state == 11:

            if E.search(char):
                state = 13
                index += 1
                col += 1
                lex += char
            elif re.search(r'[\n]', char):
                state = 13
                index += 1
                col = 1
                row += 1
                lex += char
        elif state == 12:

            if D.search(char):
                index += 1
                col += 1
                lex += char
            else:
                tokens.append(lex)
                lex = ''
                state = 0
        elif state == 13:

            if E.search(char):
                index += 1
                col += 1
                lex += char
            elif re.search(r'[\n]', char):
                index += 1
                col = 1
                row += 1
                lex += char
            elif re.search(r"[']", char):
                state = 15
                index += 1
                col += 1
                lex += char

        elif state == 15:

            if re.search(r"[']", char):
                state = 16
                index += 1
                col += 1
                lex += char

        elif state == 16:

            if re.search(r"[']", char):
                state = 17
                index += 1
                col += 1
                lex += char

        elif state == 17:

            tokens.append(lex)
            lex = ''
            state = 0

    return tokens