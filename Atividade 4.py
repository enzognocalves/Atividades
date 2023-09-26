import random
"""
def escrevernumerosaleatorios(qtdnumeros, nomearquivo):
    arquivosnumeros = open (nomearquivo, 'w')
    for i in range (qtdnumeros):
        arquivosnumeros.write(str(random.randit(0,100)))
        arquivosnumeros.write("\n")


    arquivosnumeros.close()

escrevernumerosaleatorios(100,'aleatorios.txt')
"""
"""
def escrevermedia(qtdnumeros, nomearquivo):
    arquivosnumeros = open(nomearquivo)
    soma = 0

    for i in range(qtdnumeros):
        num = float(arquivosnumeros.readline())
        soma +=num
    arquivosnumeros.close()
    return soma/qtdnumeros
print(escrevermedia(3, 'media.txt'))
"""
"""
def copiaarquivo(velhoarquivo,novoarquivo):
    f1 = open(velhoarquivo, "r")
    f2 = open(novoarquivo, "w")
    for texto in f1:
        f2.write(texto)
    f1.close()
    f2.close()
copiaarquivo("media.txt", "novo.txt")
"""
# Exercicio - 1
"""
nomes = ("dutch","micah","arthur","john","jack","sadie","charles","javier","hosea","lenny")
sobrenomes = ("van der","bell","morgan","marston,","adler","smith","escuella","metthews","summers")
def escrevernumerosaleatorios(nomes,nomearquivo):
    arquivonumeros = open(nomearquivo, "w")


    for i in nomes:
      arquivonumeros.write(str(i))
      arquivonumeros.write("\n")
escrevernumerosaleatorios(nomes,'nomes.txt')
"""
"""
sobrenomes = ("van der","bell","morgan","marston,","adler","smith","escuella","metthews","summers")
def escrevernumerosaleatorios(nomes,nomearquivo):
    arquivonumeros = open(nomearquivo, "w")


    for i in nomes:
      arquivonumeros.write(str(i))
      arquivonumeros.write("\n")
escrevernumerosaleatorios( sobrenomes,'sobrenomes.txt')
"""



