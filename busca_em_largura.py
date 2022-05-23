import collections
import pandas as pd

cordanate = range(70)
mapa =  [
        cordanate[:10],
        cordanate[10:20],
        cordanate[20:30],
        cordanate[30:40],
        cordanate[40:50],
        cordanate[50:60],
        cordanate[60:70]
        ]
mapa_df = pd.DataFrame(mapa)
mapa_df
print(mapa_df)
class Node:
    def __init__(self, value, cordenate):
        self.value = value
        self.cordenate = cordenate
        self.connection = []

    def __repr__(self):
        return f'{self.value}'

class Bsf():

    def bfs(self, start, root, end):
        self.start = start
        ranks = collections.deque([self.start])
        while start != None:
            if root == end:
                ranks.popleft()
                return ranks
               
        print(ranks)
bs=Bsf()
bs.bfs((0,0),mapa,(10,40))