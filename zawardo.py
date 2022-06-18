import pandas as pd
import matplotlib as mt

from agent import Agent


matrix = list(range(70))
zawardo = [
        matrix[0:10],
        matrix[10:20],
        matrix[20:30],
        matrix[30:40],
        matrix[40:50],
        matrix[50:60],
        matrix[60:70]
          ]

          
obstacles = [(0,6),(1,1),(1,2),(4,5),(4,6),(6,6),(6,7),(6,8)]

for obstacles in obstacles:
    x,y = obstacles
    zawardo[x][y] = None

zawardomx = pd.DataFrame(zawardo)
print(zawardomx)


agent = Agent(zawardomx,(2,2),(6,5))
agent.strategy('bfs')

#tasks
#MUNDO:
    # criar matriz de 0 a 70 {concluido}
    #agente tem não pode ser capaz de utrapassar o objeto da matriz nulo {concluido}
    #agente só pode andar 1 espaço por vez lateralmente e horizontalmente {concluido}
    #(opcional) criar mundo no pygame 
    #agente tem que ser capaz de encontrar o numero indicado{concluido}
    #agente tem que ser capaz de encontrar o caminho com menos gastos
#estrategia do agente:
    #o agente pode terá 3 estrategias 
    # bfs: utilização de FIFO {quase completo}
    # dfs: utilizando LIFO
    # a*: dfs e bfs 
    # djk (opcional) fds