import re
from typing import List, Tuple
from models.error_entry import ErrorEntry
from models.token import TokenEntry
from models.token_enum import TypeToken


def automata(input: str) -> Tuple[Tuple[TokenEntry], Tuple[ErrorEntry]]:
    # define regex
    L = re.compile(r'[A-Za-z_-]')
    E = re.compile(r'[^\n\']')
    D = re.compile(r'[0-9]')
    T = re.compile(r'[\s\n\t]')
    S = re.compile(r'[;,=\(\)\[\]\{\}]')

    input += '\n'  # fix EOF error
    tokens: List[TokenEntry] = []
    errs: List[ErrorEntry] = []
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

            # Caracteres ignorados
            elif re.search(r'[\n]', char):
                row += 1
                col = 0
                index += 1

            elif re.search(r'[ \t]', char):
                col += 1
                index += 1
            else:
                errs.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                state = 0

        elif state == 1:
            if L.search(char):
                index += 1
                col += 1
                lex += char
            else:
                if lex.lower() in [
                        'claves', 'registros', 'imprimir', 'imprimirln',
                        'conteo', 'promedio', 'contarsi', 'datos', 'sumar',
                        'max', 'min', 'exportarreporte'
                ]:

                    switcher = {
                        'claves': TypeToken.CLAVES,
                        'registros': TypeToken.REGISTROS,
                        'imprimir': TypeToken.IMPRIMIR,
                        'imprimirln': TypeToken.IMPRIMIRLN,
                        'conteo': TypeToken.CONTEO,
                        'promedio': TypeToken.PROMEDIO,
                        'contarsi': TypeToken.CONTARSI,
                        'datos': TypeToken.DATOS,
                        'sumar': TypeToken.SUMAR,
                        'max': TypeToken.MAX,
                        'min': TypeToken.MIN,
                        'exportarreporte': TypeToken.EXPORTAR_REPORTE
                    }

                    type_token: TypeToken = switcher.get(lex.lower())
                    tokens.append(TokenEntry(type_token, lex, row, col))
                    lex = ''
                    state = 0
                else:
                    errs.append(ErrorEntry(row, col, char))
                    index += 1
                    col += 1
                    state = 0

        elif state == 2:
            if re.search(r"[\n]", char):
                state = 7
                index += 1
                col = 1
                row += 1
                lex += char
            elif E.search(char) or re.search(r"[']", char):
                index += 1
                col += 1
                lex += char
            else:
                errs.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                state = 0

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
                tokens.append(TokenEntry(TypeToken.INTEGER, lex, row, col))
                lex = ''
                state = 0
        elif state == 6:
            if lex.lower() in [';', ',', '=', '(', ')', '[', ']', '{', '}']:
                switcher = {
                    ';': TypeToken.PUNTO_COMA,
                    ',': TypeToken.COMA,
                    '=': TypeToken.IGUAL,
                    '(': TypeToken.PARENTESIS_ABRIR,
                    ')': TypeToken.PARENTESIS_CERRAR,
                    '[': TypeToken.CORCHETE_ABRIR,
                    ']': TypeToken.CORCHETE_CERRAR,
                    '{': TypeToken.LLAVE_ABRIR,
                    '}': TypeToken.LLAVE_CERRAR,
                }
                type_token: TypeToken = switcher.get(lex.lower())
                tokens.append(TokenEntry(type_token, lex, row, col))
            else:
                errs.append(ErrorEntry(row, col, char))
                index += 1
                col += 1
                state = 0
            lex = ''
            state = 0
        elif state == 7:
            tokens.append(
                TokenEntry(TypeToken.COMENTARIO_ONE_LINE, lex, row, col))
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
            tokens.append(TokenEntry(TypeToken.STRING, lex, row, col))
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
                tokens.append(TokenEntry(TypeToken.DOUBLE, lex, row, col))
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
            tokens.append(
                TokenEntry(TypeToken.COMENTARIO_MULTI_LINE, lex, row, col))
            lex = ''
            state = 0

    return tokens, errs