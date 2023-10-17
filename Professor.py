from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self,nome):
        super().__init__(nome)

    def saudar(self):
        return f'olá, eu sou o prof {self._nome}'
