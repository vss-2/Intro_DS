from collections import defaultdict
# Defaultdict é uma modificação do dicionário padrão, ele retorna listas e 
# não exibe erro caso tente acessar um item do dict() que não exista

algoritmo    = ''
est_inicial  = ''
est_final    = ''
est_conjunto = []

class BFS_DFS:
    # A estrutura do BFS e DFS é fundamentalmente a mesma.
    # É possível verificar isso abaixo, 
    # já que apenas o local de remoção do nó é diferente (fila/pilha)

    def __init__(self, a, i, f):
        self.grafo  = defaultdict(list)
        self.visit  = defaultdict()
        self.inicio = int(i)
        self.fim    = int(f)
        self.alg    = a
    
    def inserir(self, origem, destino):
        self.visit.update({origem: False})
        self.visit.update({destino: False})
        self.grafo[origem].append(destino)
        return

    def executar(self):
        # Largura = fila (remoção do primeiro)
        if(self.alg == 'BFS'):
            fila = []

            # Início do algoritmo
            fila.append(self.inicio)
            self.visit.update({self.inicio: True})

            while(len(fila)>0):
                rem_no = fila.pop(0)
                print('Removendo {} da fila'.format(rem_no))

                # Adicionando novos nós na fila a partir do removido
                for g in self.grafo[rem_no]:
                    if(self.visit[g] == False):
                        fila.append(g)
                        print('Enfileirando {}'.format(g))
                        self.visit[g] = True
    
                print('Status da fila:\n', fila)
            return
        
        # Profundidade = pilha (remoção do último)
        else:
            pilha = []
            
            # Início do algoritmo
            pilha.append(self.inicio)
            self.visit.update({self.inicio: True})

            while(len(pilha)>0):
                rem_no = pilha.pop(len(pilha)-1)
                print('Removendo {} da pilha'.format(rem_no))

                # Adicionando novos nós na pilha a partir do removido
                for g in self.grafo[rem_no]:
                    if(self.visit[g] == False):
                        pilha.append(g)
                        print('Empilhando {}'.format(g))
                        self.visit[g] = True
    
                print('Status da pilha:\n', pilha)
            return

class UCS:
    def __init__(self, i, f):
        self.grafo  = []
        self.visitados = set()
        self.inicio = int(i)
        self.fim    = int(f)

    def inserir(self, origem, destino, distancia):
        # A fila de prioridade é atualizada a cada inserção
        self.grafo.append([origem, destino, distancia])
        self.grafo.sort(key=lambda x: x[2])
        return
    
    def executar(self):
        self.visitados.add(self.inicio)
        custo = 0
        trajeto = [[self.inicio, 0]]
        while(self.fim not in self.visitados and len(self.grafo)>0):

            # Vemos se há vértice entre origem já visitada 
            # e nó destino ainda não visitado.
            # Olhamos o primeiro da fila de prioridades
            if(self.grafo[0][0] in self.visitados and self.grafo[0][1] not in self.visitados):
                
                # Atualização do custo e trajeto, remoção do vértice pego 
                # reordenação da fila de prioridades
                trajeto.append(self.grafo[0][1])
                # Bug identificado: trajeto tem que verificar quem são os nós anteriores para atualizar o custo corretamente e deve guardar o par [novo_visitado, custo]
                custo += self.grafo[0][2]
                self.visitados.add(self.grafo[0][1])
                self.grafo.pop(0)
                self.grafo.sort(key=lambda x: x[2])
            else:
                # Caso usar o menor vértice não seja possível, jogo ele no fim 
                # e a próxima iteração vai ver se o 2o me
                self.grafo.append(self.grafo[0])
                self.grafo.pop(0)
                print(self.grafo)
                print(self.visitados)
                
        print('Trajeto:', trajeto)
        print('O melhor custo entre {} e {} é {}'.format(self.inicio, self.fim, custo))
        return

class Astar:
    def __init__(self):
        return

if __name__ == "__main__":
    alg_bfs_dfs = BFS_DFS('', 0, 0)
    alg_ucs     = UCS(0, 0)
    alg_astar   = Astar()

    with open('config.txt') as arq:
        linhas = arq.readlines()
        l = linhas.pop(0)
        while(len(linhas) > 0):
            if(l.startswith('#')):
                l = linhas.pop(0)
                continue
            
            if(l.startswith('Algoritmo')):
                l = linhas.pop(0)
                algoritmo = l.split(':')[1].strip()
                if(algoritmo == 'BFS' or algoritmo == 'DFS'):
                    alg_bfs_dfs = BFS_DFS(algoritmo, est_inicial, est_final)
                elif(algoritmo == 'UCS'):
                    UCS(l)
                elif(algoritmo == 'A*'):
                    Astar(l)
                if(algoritmo == 'BFS' or algoritmo == 'DFS' or algoritmo == 'UCS' or algoritmo == 'A*'):
                    print('\nAlgoritmo não identificado!')
                    exit()
                 
            
            if(l.startswith('Estado inicial')):
                l = linhas.pop(0)
                est_inicial = l.strip()

            if(l.startswith('Estado final')):
                l = linhas.pop(0)
                est_final   = l.strip()

            if(l.startswith('Conjunto de Estados:')):
                print(l)
                while(len(linhas) > 0):
                    l = linhas.pop(0)
                    if(algoritmo == 'BFS' or algoritmo == 'DFS'):
                        alg_bfs_dfs.inserir(int(l.split()[0]), int(l.split()[1]))
                    elif(algoritmo == 'UCS'):
                        alg_ucs.inserir(int(l.split()[0]), int(l.split()[1]))
                    elif(algoritmo == 'A*'):
                        Astar(l)

    arq.close()
    exit()
