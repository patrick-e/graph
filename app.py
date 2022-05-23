import pygame,sys


#tamanho da janela
width = 640
height = 480 
size = width,height



#cores do campo
lightgray = (225, 225, 225)
darkgray = (160, 160, 160)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 128, 0)

#numero e configuração de colunas e linhas



#iniciando a janela
pygame.init()
screen = pygame.display.set_mode(size)

tick = pygame.time.Clock()

        
class Settings():
    def __init__(self):
        self.col = 640
        self.rows = 640
        self.w = width // self.col
        self.h = height // self.rows
        self.distance_rows = self.rows   // 50
        self.distance_col = self.col // 50
    def grid(self, col , rows):
        '''
        esta função cria um divisao de linhas e colunas no pygame
        '''
        global screen,black
        x = 0
        y = 0

        for i in range(rows):
            x += self.distance_rows
            y += self.distance_rows
            
            pygame.draw.line(screen,white,(0,x),(rows,x))
            pygame.draw.line(screen,white,(y,0),(y,col))
            
                

    def redraw(self, screen):
        global black
        screen.fill(black)
        settings.grid(self.col,self.rows)
        pygame.display.update()

settings = Settings()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    settings.redraw(screen)

        