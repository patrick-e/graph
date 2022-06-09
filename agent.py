#tasks
#MUNDO:
    # criar matriz de 0 a 70 {concluido}
    #agente tem não pode ser capaz de utrapassar o objeto da matriz nulo {concluido}
    #agente só pode andar 1 espaço por vez lateralmente e horizontalmente {concluido}
    #(opcional) criar mundo no pygame 
    #agente tem que ser capaz de encontrar o numero indicado 
    #agente tem que ser capaz de encontrar o caminho com menos gastos
#estrategia do agente:
    #o agente pode terá 3 estrategias 
    # bfs: utilização de FIFO 
    # dfs: utilizando LIFO
    # a*: dfs e bfs 
    # djk (opcional) fds
import random as rd
from bfs import Bfs

class Agent():
    def __init__(self,world,start:tuple,objective:tuple) :
        self.world = world
        self.start = start
        self.objective = objective
        self.visited = []
        self.ef = 0


    def moveset(self ):
        reference = self.start 
        x,y = reference 
        self.r = rd.choices([
                (x-1,y),
                (x+1,y),
                (x,y-1),
                (x,y+1)
                ])
        self.ef += 1
        return self.r

    def way(self):

        while self.start != self.objective:
            self.visited.append([self.start])
            for i in self.moveset():
                self.start = i
            self.visited
        print(self.visited)
        print(self.ef)
            
        




