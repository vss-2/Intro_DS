from Capitais import Capitais
c = Capitais()
# Capitais é um grafo completo (todas ligações entre todos as cidades), entretanto,
# eu reduzo o número de conexões para 3 mais próximas
n = 4

def filtro(n):
    c_filtrado = []
    for i in c.lista:
        f = list(filter(lambda x: x.endswith(i), c.mapa))
        """para cada na lista das cidade
            filtre todas as cidades que sao atingidas a partir dessa
            ordene os resultados filtrados pelos mais proximos
            crie um novo dicionario com os resultados
            retorne o dicionario para main
        """
        for j in c.lista:
            f = list(filter(lambda x: x.startswith(j), c.mapa))
            d = dict()
            for k in c.lista:
                d = {j: c.mapa.get(j)}
            d = d.items()
            d.sort(key=lambda x: x[1])
            d = d[1:n+1]
        # A primeira distância é sempre 0
        c_filtrado.append(f[1:n+1])
    return c_filtrado

class Greedy:
    
    def __init__(self, i, f):
        self.inicio = i
        self.fim    = f

    def menorDistancia(self, d):
        # Heurística
        d.sort()
        return d[0]    

    def heuristica(self, dados):
        x = menorDistancia(dados)
        return x

    def executar(self, c_filtrado):
        c_atual = self.inicio
        custo = 0
        trajeto = []
        fronteira = []
        while(c_atual != self.fim):
            print('Visitando {}')
            heuristica(c_atual)
        print('Trajeto de {} a {} feito em: {} km'.format(self.inicio, self.fim, custo))
        return

if __name__ == "__main__":
    c_filtrado = filtro(n)
    print(c_filtrado)
    inicio = input('Qual o ponto de partida?\n')
    fim    = input('Qual o ponto de chegada?\n')
    g = Greedy(inicio, fim)
    g.executar(c_filtrado)
    exit()