from random import randint
import Rainha
import Tabuleiro

class Genetica:

    # Condição de parada caso 1 seja válido
    def e_valido(tabuleiro):
        Xs = [k[0] for k in tabuleiro.genotipo]
        Ys = [k[1] for k in tabuleiro.genotipo]
        for i in range(tabuleiro.tamanho):
            
            # Verificando se apenas 1 está na mesma linha e coluna
            if(Xs.count(tabuleiro.genotipo[i][0] == 1) and Ys.count(tabuleiro.genotipo[i][1] == 1)):
                continue
            else:
                return False
            
            # Verificando inversa 

            l = tabuleiro.genotipo[i]
            while(l[0] > -1 and l[1] > -1):
                l = (l[0]-1, l[1]-1)
                if(l is in tabuleiro.genotipo):
                    return False

            l = tabuleiro.genotipo[i]
            while(l[0] < tabuleiro.tamanho and l[1] < tabuleiro.tamanho):
                l = (l[0]+1, l[1]+1)
                if(l is in tabuleiro.genotipo):
                    return False
            
            # Verificando diagonal normal (os de antes e os depois)

            l = tabuleiro.genotipo[i]
            while(l[0] > -1 and l[1] > tabuleiro.tamanho):
                l = (l[0]-1, l[1]+1)
                if(l is in tabuleiro.genotipo):
                    return False

            l = tabuleiro.genotipo[i]
            while(l[0] < tabuleiro.tamanho and l[1] > -1):
                l = (l[0]+1, l[1]-1)
                if(l is in tabuleiro.genotipo):
                    return False

        return True

    def fitness():


    # Mutações: Alteram a tupla de um par aleatório (implementei usando para um valor percentual ou valor bruto)
    def mutacaoPercentual(tabuleiro, percentual_mut):
        for i in range(round(tabuleiro.tamanho * percentual_mut)):
            tabuleiro.genotipo[randint(0, tabuleiro.tamanho)] = (randint(0, tabuleiro.tamanho), randint(0, tabuleiro.tamanho))
        return

    def mutacaoNumero(tabuleiro, numero_mut):
        for i in range(numero_mut):
            tabuleiro.genotipo[randint(0, tabuleiro.tamanho)] = (randint(0, tabuleiro.tamanho), randint(0, tabuleiro.tamanho))
        return