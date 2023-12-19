import pygame
import random


pygame.init()
WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('tp-pf')


#color defs
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRASS = (0, 204, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PURPLE = (127, 0, 255)
PINK = (255, 51, 255)
TEAL = (0, 255, 255)


#mafs
grav = 0.72
pxvel = 4
pwid = 40
pheight = 60


movers = []
class mover():
   def __init__(self, x: int, y: int) -> None:
      movers.append(self)
      self.x = x
      self.y = y
      self.xvel = 0
      self.yvel = 0
   
   def draw_mover(self):
      pygame.draw.rect(WIN, PURPLE, (self.x, self.y, pwid, pheight), width=3)
   
   def move(self):
      self.x += self.xvel
      self.y += self.yvel
      self.yvel += grav


blocks = []
class block():
   def __init__(self, x, y, wid, hei) -> None:
      blocks.append(self)
      self.x = x
      self.y = y
      self.width = wid
      self.height = hei
   
   def draw_block(self):
      pygame.draw.rect(WIN, GRASS, (self.x, self.y, self.width, self.height), width=0)

startx = 100
starty = 100
player = mover(startx, starty)
floor = block(0, 500, 500, 50)

#pygame.Rect.collideobjects

#main loop
run = True
while run:

   WIN.fill(WHITE)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False
      elif event.type == pygame.KEYDOWN:
         if event.key == pygame.K_RIGHT:
            player.xvel = pxvel
         elif event.key == pygame.K_LEFT:
            player.xvel = -pxvel
         elif event.key == pygame.K_SPACE:
            player.yvel = -15
      elif event.type == pygame.KEYUP:
         if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            player.xvel = 0

#thing funcs
   for bck in blocks:
      bck.draw_block()
   for movie in movers:
      movie.draw_mover()
   player.move()

   pygame.display.flip()