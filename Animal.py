#Herança
class Animal:
    def __init__(self,nome,especie):
        self._nome = nome
        self._especie = especie

    def emitirsom(self):
        print(f'{self._nome} faz um som')
