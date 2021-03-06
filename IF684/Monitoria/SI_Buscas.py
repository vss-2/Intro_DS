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
        # Uma implementação adicional que pode ser feita e
        # não está nos códigos tradicionais é colocar uma condicional para parar
        # o BFS ou DFS, já ambos tradicionalmente eles percorrem o grafo todo

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
        # Lembrando que a pilha pode ser implementada de forma recursiva
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
        trajeto = [self.inicio]
        while(self.fim not in self.visitados and len(self.grafo)>0):

            # Vemos se há vértice entre origem (já visitada)
            # e nó destino (ainda não visitado).
            # Olhamos o primeiro da fila de prioridades
            if(self.grafo[0][0] in self.visitados and self.grafo[0][1] not in self.visitados):
                
                # Atualização do custo e trajeto
                trajeto.append(self.grafo[0][1])
                custo += self.grafo[0][2]

                for g in self.grafo:
                    if(g[1] == self.grafo[0][1]):
                        # Atualização do custo dos nós acessados pelo visitado
                        g[2] += self.grafo[0][2]

                # Remoção do vértice pego, adicionando no visitado e
                # reordenação da fila de prioridades
                self.visitados.add(self.grafo[0][1])
                self.grafo.pop(0)
                self.grafo.sort(key=lambda x: x[2])
            else:
                # Caso usar o menor vértice não seja possível, jogo ele no fim 
                # da fila e a próxima iteração vamos ver se o 2o melhor serve
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

    # Para efeito de exemplificação, o código considera entrada amigável, ou seja:
    # grafos conexos, e que exista caminho entre início e fim
    with open('input.txt') as arq:
        linhas = arq.readlines()
        while(len(linhas) > 0):
            l = linhas.pop(0)
            if(l.startswith('#') or l == '\n'):
                continue
            
            if(l.startswith('Algoritmo')):
                algoritmo = l.split(':')[1].strip()
                if(algoritmo != 'BFS' and algoritmo != 'DFS' and algoritmo != 'UCS' and algoritmo != 'A*'):
                    print('\nAlgoritmo não identificado!')
                    exit()
            
            if(l.startswith('Estado inicial')):
                est_inicial = l.split(':')[1].strip()
                l = linhas.pop(0)
                if(l.startswith('Estado final')):
                    est_final   = l.split(':')[1].strip()
                    if(algoritmo == 'BFS' or algoritmo == 'DFS'):
                        alg_bfs_dfs = BFS_DFS(algoritmo, est_inicial, est_final)
                    elif(algoritmo == 'UCS'):
                        alg_ucs = UCS(est_inicial, est_final)
                    elif(algoritmo == 'A*'):
                        Astar(l)


            if(l.startswith('Conjunto de Estados:')):
                while(len(linhas) > 0):
                    l = linhas.pop(0)
                    if(l=='\n'):
                        # Se tiver encerrado a entrada, executa o algoritmo
                        print('Iniciando {}'.format(algoritmo))
                        if(algoritmo == 'BFS' or algoritmo == 'DFS'):
                            alg_bfs_dfs.executar()
                        elif(algoritmo == 'UCS'):
                            alg_ucs.executar()
                        elif(algoritmo == 'A*'):
                            alg_astar.executar()
                        else:
                            exit()
                        print('--------------------------------------')
                        break

                    if(algoritmo == 'BFS' or algoritmo == 'DFS'):
                        alg_bfs_dfs.inserir(int(l.split()[0]), int(l.split()[1]))
                    elif(algoritmo == 'UCS'):
                        alg_ucs.inserir(int(l.split()[0]), int(l.split()[1]), int(l.split()[2]))
                    elif(algoritmo == 'A*'):
                        Astar(l)


    arq.close()
    exit()
