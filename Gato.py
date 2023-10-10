from Animal import Animal

class Gato(Animal):
    def __init__(self,nome,raca):
        super().__init__(nome,especie="Gato")
        self._raca = raca
    def emitirsom(self):
        print(f"{self._nome}mia. (miau miau)")

    def buscar (self):
        print(f"{self._nome}arranhar o.  (sofa)")
