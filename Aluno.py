from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self,nome):
        super().__init__(nome)

    def saudar(self):
        return f'olá, eu sou aluno {self._}'
