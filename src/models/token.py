from models.token_enum import TypeToken


class TokenEntry:
    def __init__(self, token: TypeToken, lexema: str, fila: int, col: int) -> None:
        self.token: TypeToken = token
        self.lexema: str = lexema
        self.fila: int = fila
        self.col: int = col