from typing import List
from models.token import TokenEntry
from models.token_enum import TypeToken
from statistics import mean

from pandas import DataFrame

from process.helpers import render_data


class Extraer:
    def __init__(self, tokens: List[TokenEntry]) -> None:
        self.lista: List[TokenEntry] = tokens
        self.lista.append(TokenEntry(TypeToken.EOF, None, None, None))
        self.claves: List[str] = []
        self.registros: List = []
        self.output: str = ''

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
                self.add_output(self.lista[i + 2].lexema)
                # print(, end='')
            elif self.lista[i].token == TypeToken.IMPRIMIRLN:
                self.add_output_ln(self.lista[i + 2].lexema)
                # print(self.lista[i + 2].lexema)
            elif self.lista[i].token == TypeToken.CONTEO:
                self.add_output_ln(len(self.registros))
                # print(len(self.registros))
            elif self.lista[i].token == TypeToken.PROMEDIO:
                campo = self.lista[i + 2].lexema
                index = self.claves.index(campo)
                elements = list(map(lambda r: r[index], self.registros))
                prom = mean(elements)
                self.add_output_ln('Promedio de: {} = {}'.format(campo, prom))
                # print('Promedio de: {} = {}'.format(campo, prom))
            elif self.lista[i].token == TypeToken.CONTARSI:
                campo = self.lista[i + 2].lexema
                index = self.claves.index(campo)
                elements = list(map(lambda r: r[index], self.registros))
                count = elements.count(self.lista[i + 4].lexema)
                self.add_output_ln('Conteo de: {} = {}'.format(campo, count))
                # print('Conteo de: {} = {}'.format(campo, count))
            elif self.lista[i].token == TypeToken.DATOS:
                data_dict = {}
                for clave in self.claves:
                    index = self.claves.index(clave)
                    elements = list(map(lambda r: r[index], self.registros))
                    data_dict[clave] = elements
                data_frame = DataFrame(data=data_dict)
                self.add_output_ln(str(data_frame))
                # print(str(data_frame))
            elif self.lista[i].token == TypeToken.SUMAR:
                campo = self.lista[i + 2].lexema
                index = self.claves.index(campo)
                elements = list(map(lambda r: r[index], self.registros))
                total = sum(elements)
                self.add_output_ln('Suma de: {} = {}'.format(campo, total))
                # print('Suma de: {} = {}'.format(campo, total))
            elif self.lista[i].token == TypeToken.MAX:
                campo = self.lista[i + 2].lexema
                index = self.claves.index(campo)
                elements = list(map(lambda r: r[index], self.registros))
                max_value = max(elements)
                self.add_output_ln('Maximo de: {} = {}'.format(
                    campo, max_value))
                # print('Maximo de: {} = {}'.format(campo, max_value))
            elif self.lista[i].token == TypeToken.MIN:
                campo = self.lista[i + 2].lexema
                index = self.claves.index(campo)
                elements = list(map(lambda r: r[index], self.registros))
                min_value = min(elements)
                self.add_output_ln('Minimo de: {} = {}'.format(
                    campo, min_value))
                # print('Minimo de: {} = {}'.format(campo, min_value))
            elif self.lista[i].token == TypeToken.EXPORTAR_REPORTE:
                titulo = self.lista[i + 2].lexema
                self.add_output_ln('Exportando reporte ...')
                render_data(titulo, self.claves, self.registros)

            i += 1

    def add_output(self, data: str):
        self.output += str(data)

    def add_output_ln(self, data: str):
        self.output += str(data) + '\n'