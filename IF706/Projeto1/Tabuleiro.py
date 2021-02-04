from random import randint
from Rainha import Rainha

class Tabuleiro:

    def __init__(self, qtd):
        self.tamanho  = qtd
        self.genotipo = []

    def inserir(self, rainha):
        self.genotipo.append(rainha)
        return self.genotipo

    def inicioAleatorio(self):
        for x in range(self.tamanho):
            r = Rainha(randint(0, self.tamanho - 1), randint(0, self.tamanho - 1))
            self.inserir(r)
        return self.genotipo

def main():
    i = input('Quantas rainhas serão?\n')
    t = Tabuleiro(int(i))
    i = input('O início será aleatório (s/n)?\n')
    if(i == 's'):
        t.inicioAleatorio()
    else:
        for x in range(self.tamanho):
            i = input('Insira as posições (no formato:x y) da {}a rainha\n'.format(x))
            r = Rainha(i.split(' ')[0], i.split(' ')[1])
            t.inserir(r)
    return t
