from typing import List
from models.token import TokenEntry
from models.token_enum import TypeToken
from statistics import mean


class Extraer:
    def __init__(self, tokens: List[TokenEntry]) -> None:
        self.lista: List[TokenEntry] = tokens
        self.lista.append(TokenEntry(TypeToken.EOF, None, None, None))
        self.claves: List[str] = []
        self.registros: List = []

    def extract_claves(self):
        i = 0
        flag_claves: bool = False
        while self.lista[i].token != TypeToken.EOF:
            if self.lista[i].token == TypeToken.CLAVES:
                flag_claves = True
            elif flag_claves and self.lista[
                    i].token == TypeToken.CORCHETE_CERRAR:
                flag_claves = False
            elif flag_claves and self.lista[i].token == TypeToken.STRING:
                self.claves.append(self.lista[i].lexema.strip())
            i += 1

    def extract_registros(self):
        i = 0
        j = 0
        registro: List = []
        flag_registros: bool = False
        while self.lista[i].token != TypeToken.EOF:
            if self.lista[i].token == TypeToken.REGISTROS:
                flag_registros = True
            elif flag_registros and self.lista[
                    i].token == TypeToken.CORCHETE_CERRAR:
                flag_registros = False
            elif flag_registros and self.lista[i].token in [
                    TypeToken.STRING, TypeToken.DOUBLE, TypeToken.INTEGER
            ]:
                registro.append(self.lista[i].lexema)
                j += 1
                if not j < len(self.claves):
                    self.registros.append(registro.copy())
                    registro.clear()
                    j = 0
            i += 1

    def extract_commands(self):
        i = 0
        while self.lista[i].token != TypeToken.EOF:
            if self.lista[i].token == TypeToken.IMPRIMIR:
                print(self.lista[i + 2].lexema, end='')
            elif self.lista[i].token == TypeToken.IMPRIMIRLN:
                print(self.lista[i + 2].lexema)
            elif self.lista[i].token == TypeToken.CONTEO:
                print(len(self.registros))
            elif self.lista[i].token == TypeToken.PROMEDIO:
                index = self.claves.index(self.lista[i + 2].lexema)
                elements = list(map(lambda r: r[index], self.registros))
                prom = mean(elements)
                print('Promedio: {}'.format(prom))
            elif self.lista[i].token == TypeToken.CONTARSI:
                index = self.claves.index(self.lista[i + 2].lexema)
                elements = list(map(lambda r: r[index], self.registros))
                count = elements.count(self.lista[i + 4].lexema)
                print('Conteo: {}'.format(count))
            elif self.lista[i].token == TypeToken.DATOS:
                pass
            elif self.lista[i].token == TypeToken.SUMAR:
                index = self.claves.index(self.lista[i + 2].lexema)
                elements = list(map(lambda r: r[index], self.registros))
                total = sum(elements)
                print('Suma: {}'.format(total))
            elif self.lista[i].token == TypeToken.MAX:
                index = self.claves.index(self.lista[i + 2].lexema)
                elements = list(map(lambda r: r[index], self.registros))
                max_value = max(elements)
                print('Maximo: {}'.format(max_value))
            elif self.lista[i].token == TypeToken.MIN:
                index = self.claves.index(self.lista[i + 2].lexema)
                elements = list(map(lambda r: r[index], self.registros))
                min_value = min(elements)
                print('Minimo: {}'.format(min_value))
            elif self.lista[i].token == TypeToken.EXPORTAR_REPORTE:
                pass
            i += 1