import random as rd


class Agent():
    def __init__(self,world,start,objective:tuple = ()) :
        self.world = world
        self.start = start
        self.objective = objective
        self.ef = 0
        self.visited = []
        self.queue = []


    def moveset(self):
        reference = self.start 
        x,y = reference 
        self.r = [
                (x-1,y),
                (x+1,y),
                (x,y-1),
                (x,y+1)
                ]
        self.ef += 1 
        return self.r

    
    def random(self):
        while self.start != self.objective:
            self.visited.append([self.start])
            for i in rd.choices(self.moveset()) :
                x,y = i
                i = (abs(x),abs(y))

                if i != None :
                    self.start = i
        else:    
            print(self.visited)    
            print(self.ef)
           
    def bfs(self):
        self.visited.append(self.start)
        self.queue.append(self.start)
        while self.queue:          
            m = self.queue.pop(0) 
            for j in self.moveset():
                if j not in self.visited:
                    self.visited.append(j[m])
                    self.queue.append(self.moveset)
        print(self.visited,"visited")
        print(self.ef)
               
    def strategy(self,strategy):
        ''' possible estrategy 'random','bfs',''dfs,'A*'
        '''
        j = [{'random':self.random()},
        {'bfs': self.bfs()}]
        # {'A*': self.astar()},
        # {"dfs":self.dfs()}

        return j[strategy]

        