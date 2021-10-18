
from typing import List
from models.token_enum import TypeToken


class ErrorEntry:
    def __init__(self, linea: int, col: int, char: str) -> None:
        self.linea: int = linea
        self.col: int = col
        self.char: str = char

class SintaxError:
    def __init__(self, linea: int, col: int, last_token: TypeToken, expected_tokens: List[TypeToken]) -> None:
        self.linea: int = linea
        self.col: int = col
        self.last_token: TypeToken = last_token
        self.expected_tokens: List[TypeToken] = expected_tokens