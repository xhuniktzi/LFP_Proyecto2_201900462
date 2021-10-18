from typing import List
from models.error_entry import SintaxError
from models.token_enum import TypeToken
from models.token import TokenEntry


class Sintactico:
    def __init__(self, tokens: List[TokenEntry]):
        self.preanalisis: TypeToken = TypeToken.UNKNOWN
        self.index: int = 0
        self.lista: List[TokenEntry] = tokens
        self.lista.append(TokenEntry(TypeToken.EOF, None, None, None))
        self.preanalisis: TypeToken = self.lista[self.index].token
        self.errors: List[SintaxError] = []

    def startup(self):
        self.start()
        return self.errors

    def match(self, tipos_validos: List[TypeToken]):
        if self.preanalisis not in tipos_validos:
            token = self.lista[self.index - 1]
            self.errors.append(
                SintaxError(token.fila, token.col, token.token, tipos_validos))
            self.repetir()

        if self.preanalisis != TypeToken.EOF:
            self.index += 1
            self.preanalisis = self.lista[self.index].token

    def start(self):
        if self.preanalisis == TypeToken.CLAVES:
            self.claves()
            self.repetir()
        elif self.preanalisis == TypeToken.REGISTROS:
            self.registros()
            self.repetir()
        elif self.preanalisis == TypeToken.IMPRIMIR:
            self.imprimir()
            self.repetir()
        elif self.preanalisis == TypeToken.IMPRIMIRLN:
            self.imprimirln()
            self.repetir()
        elif self.preanalisis == TypeToken.CONTEO:
            self.conteo()
            self.repetir()
        elif self.preanalisis == TypeToken.PROMEDIO:
            self.promedio()
            self.repetir()
        elif self.preanalisis == TypeToken.CONTARSI:
            self.contarsi()
            self.repetir()
        elif self.preanalisis == TypeToken.DATOS:
            self.datos()
            self.repetir()
        elif self.preanalisis == TypeToken.SUMAR:
            self.sumar()
            self.repetir()
        elif self.preanalisis == TypeToken.MAX:
            self.max()
            self.repetir()
        elif self.preanalisis == TypeToken.MIN:
            self.min()
            self.repetir()
        elif self.preanalisis == TypeToken.EXPORTAR_REPORTE:
            self.exportar_reporte()
            self.repetir()
        elif self.preanalisis == TypeToken.COMENTARIO_ONE_LINE:
            self.match([TypeToken.COMENTARIO_ONE_LINE])
            self.repetir()
        elif self.preanalisis == TypeToken.COMENTARIO_MULTI_LINE:
            self.match([TypeToken.COMENTARIO_MULTI_LINE])
            self.repetir()

    def repetir(self):
        if self.preanalisis == TypeToken.CLAVES:
            self.claves()
            self.repetir()
        elif self.preanalisis == TypeToken.REGISTROS:
            self.registros()
            self.repetir()
        elif self.preanalisis == TypeToken.IMPRIMIR:
            self.imprimir()
            self.repetir()
        elif self.preanalisis == TypeToken.IMPRIMIRLN:
            self.imprimirln()
            self.repetir()
        elif self.preanalisis == TypeToken.CONTEO:
            self.conteo()
            self.repetir()
        elif self.preanalisis == TypeToken.PROMEDIO:
            self.promedio()
            self.repetir()
        elif self.preanalisis == TypeToken.CONTARSI:
            self.contarsi()
            self.repetir()
        elif self.preanalisis == TypeToken.DATOS:
            self.datos()
            self.repetir()
        elif self.preanalisis == TypeToken.SUMAR:
            self.sumar()
            self.repetir()
        elif self.preanalisis == TypeToken.MAX:
            self.max()
            self.repetir()
        elif self.preanalisis == TypeToken.MIN:
            self.min()
            self.repetir()
        elif self.preanalisis == TypeToken.EXPORTAR_REPORTE:
            self.exportar_reporte()
            self.repetir()
        elif self.preanalisis == TypeToken.COMENTARIO_ONE_LINE:
            self.match([TypeToken.COMENTARIO_ONE_LINE])
            self.repetir()
        elif self.preanalisis == TypeToken.COMENTARIO_MULTI_LINE:
            self.match([TypeToken.COMENTARIO_MULTI_LINE])
            self.repetir()

    def datos(self):
        self.match([TypeToken.DATOS])
        self.match([TypeToken.PARENTESIS_ABRIR])
        self.match([TypeToken.PARENTESIS_CERRAR])
        self.match([TypeToken.PUNTO_COMA])

    def conteo(self):
        self.match([TypeToken.CONTEO])
        self.match([TypeToken.PARENTESIS_ABRIR])
        self.match([TypeToken.PARENTESIS_CERRAR])
        self.match([TypeToken.PUNTO_COMA])

    def imprimir(self):
        self.match([TypeToken.IMPRIMIR])
        self.match([TypeToken.PARENTESIS_ABRIR])
        self.match([TypeToken.STRING])
        self.match([TypeToken.PARENTESIS_CERRAR])
        self.match([TypeToken.PUNTO_COMA])

    def imprimirln(self):
        self.match([TypeToken.IMPRIMIRLN])
        self.match([TypeToken.PARENTESIS_ABRIR])
        self.match([TypeToken.STRING])
        self.match([TypeToken.PARENTESIS_CERRAR])
        self.match([TypeToken.PUNTO_COMA])

    def promedio(self):
        self.match([TypeToken.PROMEDIO])
        self.match([TypeToken.PARENTESIS_ABRIR])
        self.match([TypeToken.STRING])
        self.match([TypeToken.PARENTESIS_CERRAR])
        self.match([TypeToken.PUNTO_COMA])

    def sumar(self):
        self.match([TypeToken.SUMAR])
        self.match([TypeToken.PARENTESIS_ABRIR])
        self.match([TypeToken.STRING])
        self.match([TypeToken.PARENTESIS_CERRAR])
        self.match([TypeToken.PUNTO_COMA])

    def max(self):
        self.match([TypeToken.MAX])
        self.match([TypeToken.PARENTESIS_ABRIR])
        self.match([TypeToken.STRING])
        self.match([TypeToken.PARENTESIS_CERRAR])
        self.match([TypeToken.PUNTO_COMA])

    def min(self):
        self.match([TypeToken.MIN])
        self.match([TypeToken.PARENTESIS_ABRIR])
        self.match([TypeToken.STRING])
        self.match([TypeToken.PARENTESIS_CERRAR])
        self.match([TypeToken.PUNTO_COMA])

    def exportar_reporte(self):
        self.match([TypeToken.EXPORTAR_REPORTE])
        self.match([TypeToken.PARENTESIS_ABRIR])
        self.match([TypeToken.STRING])
        self.match([TypeToken.PARENTESIS_CERRAR])
        self.match([TypeToken.PUNTO_COMA])

    def contarsi(self):
        self.match([TypeToken.CONTARSI])
        self.match([TypeToken.PARENTESIS_ABRIR])
        self.match([TypeToken.STRING])
        self.match([TypeToken.COMA])
        self.valor()
        self.match([TypeToken.PARENTESIS_CERRAR])
        self.match([TypeToken.PUNTO_COMA])

    def valor(self):
        self.match([TypeToken.STRING, TypeToken.DOUBLE, TypeToken.INTEGER])

    def claves(self):
        self.match([TypeToken.CLAVES])
        self.match([TypeToken.IGUAL])
        self.match([TypeToken.CORCHETE_ABRIR])
        self.bloque_claves()
        self.match([TypeToken.CORCHETE_CERRAR])

    def bloque_claves(self):
        self.match([TypeToken.STRING])
        if self.preanalisis == TypeToken.COMA:
            self.match([TypeToken.COMA])
            self.bloque_claves()

    def bloque_registros(self):
        self.cuerpo_registros()
        if self.preanalisis == TypeToken.LLAVE_ABRIR:
            self.bloque_registros()

    def cuerpo_registros(self):
        self.match([TypeToken.LLAVE_ABRIR])
        self.valores_registros()
        self.match([TypeToken.LLAVE_CERRAR])

    def valores_registros(self):
        self.valor()
        if self.preanalisis == TypeToken.COMA:
            self.match([TypeToken.COMA])
            self.valores_registros()

    def registros(self):
        self.match([TypeToken.REGISTROS])
        self.match([TypeToken.IGUAL])
        self.match([TypeToken.CORCHETE_ABRIR])
        self.bloque_registros()
        self.match([TypeToken.CORCHETE_CERRAR])