class Greedy:
    
    def __init__(self, i, f, h):
        self.inicio = i
        self.fim    = f
        self.mapa   = []
        self.heuris = h

    def adicionarCaminho(self, origem, fim, dist):
        self.mapa.append((origem,fim,dist))
        return
    
    def funcao(self, dados):

        def ordem(o):
            return o[1]

        def menorDistancia(dados):
            d = sorted(dados, key=ordem)
            return d
        
        def maiorDistancia(self):
            d = sorted(dados, key=ordem, reverse=True)
            return d
        
        return menorDistancia(dados)

    def executar(self):
        visitados = [self.inicio]
        posso_visit = []
        f = list(filter(lambda x: x[0] in visitados, self.mapa))
        for l in range(0, len(f)):
            posso_visit.append(f[l][1])
        g = self.funcao(self.heuris)
        for i in range(0, len(g)):
            if(g[i][0] in posso_visit):
                visitados.append(g[i][0])
                f = list(filter(lambda x: x[0] in visitados, self.mapa))
                print(f)
                break
        # print('Custo:', custo, '\nCaminho:', visitados)
        return

if __name__ == "__main__":
    dist_lin_ret = [
        ('Arad', 366),
        ('Bucharest', 0),
        ('Craiova', 160),
        ('Dobreta', 242),
        ('Eforie', 161),
        ('Fagaras', 178),
        ('Giurgiu', 77),
        ('Hirsova', 151),
        ('Iasi', 226),
        ('Lugoj', 244),
        ('Mehadia', 241),
        ('Neamt', 234),
        ('Oradea', 380),
        ('Pitesti', 98),
        ('Rimnicu Vilcea', 193),
        ('Sibiu', 253),
        ('Timisoara', 329),
        ('Urziceni', 80),
        ('Vaslui', 199),
        ('Zerind', 374)
    ]
    g = Greedy('Arad', 'Bucharest', dist_lin_ret)
    g.adicionarCaminho('Arad', 'Sibiu', 140)
    g.adicionarCaminho('Arad', 'Timisoara', 118)
    g.adicionarCaminho('Arad', 'Zerind', 75)
    g.adicionarCaminho('Bucharest', 'Fagaras', 211)
    g.adicionarCaminho('Bucharest', 'Giurgiu', 90)
    g.adicionarCaminho('Bucharest', 'Pitesti', 101)
    g.adicionarCaminho('Bucharest', 'Urziceni', 85)
    g.adicionarCaminho('Craiova', 'Dobreta', 120)
    g.adicionarCaminho('Craiova', 'Pitesti', 138)
    g.adicionarCaminho('Craiova', 'Rimnicu_Vilcea', 146)
    g.adicionarCaminho('Dobreta', 'Mehadia', 75)
    g.adicionarCaminho('Eforie', 'Hirsova', 86)
    g.adicionarCaminho('Fagaras', 'Sibiu', 99)
    g.adicionarCaminho('Hirsova', 'Urziceni', 98)
    g.adicionarCaminho('Iasi', 'Neamt', 87)
    g.adicionarCaminho('Iasi', 'Vaslui', 92)
    g.adicionarCaminho('Lugoj', 'Mehadia', 70)
    g.adicionarCaminho('Lugoj', 'Timisoara', 111)
    g.adicionarCaminho('Oradea', 'Zerind', 71)
    g.adicionarCaminho('Oradea', 'Sibiu', 151)
    g.adicionarCaminho('Pitesti', 'Rimnicu_Vilcea', 97)
    g.adicionarCaminho('Rimnicu_Vilcea', 'Sibiu', 80)
    g.adicionarCaminho('Urziceni', 'Vaslui', 142)
    g.executar()
