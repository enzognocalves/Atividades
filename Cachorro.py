from Animal import Animal

class Cachorro(Animal):
    def __init__(self,nome,raca):
        super().__init__(nome,especie="Cachorro")
        self._raca = raca
    def emitirsom(self):
        print(f"{self._nome}late. (au au)")

    def buscar (self):
        print(f"{self._nome}buscar. (bola)")
