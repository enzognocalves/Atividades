class Pessoa:
     #construtor
    def __init__(self, nome, idade, refeicao=False, comunicacao=False):
        self._nome=  nome
        self._idade=  idade
        self._refeicao=  refeicao
        self._comunicacao=  comunicacao
    #get
    @property
    def nome(self):
        return self._nome
    #set
    @nome.setter
    def nome(self,nome):
         self._nome = nome

     #get
    @property
    def idade(self):
        return self._idade
       #set
    @idade.setter
    def idade(self,idade):
         self ._idade = idade
     #get
    @property
    def refeicao(self):
        return self._refeicao
      #set
    @refeicao.setter
    def refeicao(self,refeicao):
         self ._refeicao = refeicao
    #get
    @property
    def comunicacao(self):
        return self._comunicacao
    #set
    @comunicacao.setter
    def comunicacao(self,comunicacao):
         self ._comunicacao = comunicacao

     #métodos
    def Falar(self,assunto):
        if self._refeicao:
            print(f'){self._nome}nao pode falar de boca cheia !')
            return
        if self._comunicacao:
            print(f'{self ._nome} esta falando sobre {assunto}.')
            self._comunicacao = True
    def pararFala(self):
        if not self._comunicacao:
            print(f'{self._nome} nao esta falando')
            return
        print(f'{self._nome} parou de falar')
        self._= False
    def comer(self, alimento):
        if self._refeicao:
            print(f'{self._nome}ja esta comendo')
            return
        if self.comunicacao :
            print(f'{self._nome} nao pod ecomer falando.')
            return
        print(f'{self._nome}esta comendo{alimento}.')
        self._refeicao = True









