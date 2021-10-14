from typing import List, Tuple
from models.token import TokenEntry
from models.token_enum import TypeToken


def pre_process(tokens: List[TokenEntry]) -> Tuple[Tuple[TokenEntry]]:
    results: List[TokenEntry] = []
    for t in tokens:
        if t.token == TypeToken.INTEGER:
            results.append(TokenEntry(t.token,int(t.lexema),t.fila,t.col))
        elif t.token == TypeToken.DOUBLE:
            results.append(TokenEntry(t.token, float(t.lexema),t.fila,t.col))
        elif t.token == TypeToken.COMENTARIO_ONE_LINE:
            results.append(TokenEntry(t.token, t.lexema.replace('#', '').strip(),t.fila,t.col))
        elif t.token == TypeToken.COMENTARIO_MULTI_LINE:
            results.append(TokenEntry(t.token, t.lexema.replace("'''", '').strip(),t.fila,t.col))
        elif t.token == TypeToken.STRING:
            results.append(TokenEntry(t.token, t.lexema.replace('"','').strip(),t.fila,t.col))
        else:
            results.append(TokenEntry(t.token, t.lexema.strip(),t.fila,t.col))

    return results