import pygame
from random import randint
import time
global is_paused
is_paused = True


class Box:

  def __init__(self,x,y,size,hp,vec):
    self.x = x
    self.y = y
    self.hp = hp
    self.size = size
    self.vec = vec
    self.key = pygame.key.get_pressed()
    self.this = pygame.draw.rect(screen, 255,(self.x,self.y,self.size,self.size))
  
  def collisions(self, screen):
    self.key = pygame.key.get_pressed()
    if self.key[pygame.K_a]:
      self.x -= self.vec
    if self.key[pygame.K_d]:
      self.x += self.vec
    if self.key[pygame.K_w]:
      self.y -= self.vec
    if self.key[pygame.K_s]:
      self.y += self.vec
    if self.key[pygame.K_F11]:
      pygame.display.toggle_fullscreen()
    if self.key[pygame.K_ESCAPE]:
      global is_paused
      if is_paused == True:
        is_paused = False
        time.sleep(.2)
      else:
        is_paused = True
        time.sleep(.2)
    if self.key[pygame.K_LSHIFT]:
      pygame.quit()
    if self.this.colliderect(top):
      self.y = 1
    if self.this.colliderect(bottom):
      self.y = screen.get_height()-(self.size+.01)
    if self.this.colliderect(left):
      self.x = 1
    if self.this.colliderect(right):
      self.x = screen.get_width()-(self.size+.01)
  def show(self,screen):
    if self.x<screen.get_width() and self.y<screen.get_height() and self.x > -self.size and self.y > -self.size:
      self.this = pygame.draw.rect(screen, 255,(self.x,self.y,self.size,self.size))

class Enemy:
  def __init__(self,x,y,size):
    self.x = x
    self.y = y
    self.size = size
    self.this = pygame.draw.rect(screen, [255,0,0],(self.x,self.y,self.size,self.size))
  
  def collisions(self,screen):
    if boxes[0].x+randint(-50,50) > self.x:
      self.x += .5
    else:
      self.x -= .5
    if boxes[0].y+randint(-50,50) > self.y:
      self.y += .5
    else:
      self.y -= .5
    if self.this.colliderect(boxes[0].this):
      enemies.remove(self)
  def show(self,screen):
    if self.x<screen.get_width()+10 and self.y<screen.get_height()+10 and self.x > -10 and self.y > -10:
      self.this = pygame.draw.rect(screen, [255,0,0],(self.x,self.y,self.size,self.size))

class pause:
  def __init__(self,x,y,name):
    self.x = x
    self.y = y
    self.key = pygame.key.get_pressed()
    self.name = name
    self.this = pygame.draw.rect(screen, [240,240,240],(self.x,self.y,100,100))
  
  def collisions(self,screen,collider):
    self.key = pygame.key.get_pressed()
    if self.this.colliderect(collider):
      self.this = pygame.draw.rect(screen, [255,255,255],(self.x,self.y,100,100))
      if self.key[pygame.K_RETURN]:
        print("wow, something happened")
    else:
      self.this = pygame.draw.rect(screen, [240,240,240],(self.x,self.y,100,100))

pygame.init()

screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
menu = pygame.Surface((screen.get_width(),screen.get_height()))
clock = pygame.time.Clock()

boxes = [Box(screen.get_width()/2, screen.get_height()/2, 50, 50,5),Box(screen.get_width()/4, screen.get_height()/2, 25, 50,25)]
enemies = []
PauseMenu = [pause(100,100,"test")]
counter = 0


while True:
  if is_paused:
    menu = pygame.transform.scale(menu,(screen.get_width(),screen.get_height()))
    screen.fill((255, 255, 0))
    menu.fill((0,0,0))
    menu.set_alpha(100)
    top = pygame.Rect((0,0),(screen.get_width(),1))
    bottom = pygame.Rect((0,screen.get_height()-1),(screen.get_width(),1))
    right = pygame.Rect((screen.get_width()-1,0),(1,screen.get_height()))
    left = pygame.Rect((0,0),(1,screen.get_height()))
    for thing in enemies:
      thing.show(screen)
    boxes[0].show(screen)
    screen.blit(menu,(0,0))
    for thing in PauseMenu:
      thing.collisions(screen,boxes[1].this)
    boxes[1].collisions(screen)
    boxes[1].show(screen)
    clock.tick(60)
    pygame.display.flip()
    pygame.event.pump()
  else:
    if counter % 10 == 0: enemies.append(Enemy(randint(-100,screen.get_width()+100),randint(-100,screen.get_height()+100),25))
    counter += 1
    screen.fill((255, 255, 0))
    top = pygame.Rect((0,0),(screen.get_width(),1))
    bottom = pygame.Rect((0,screen.get_height()-1),(screen.get_width(),1))
    right = pygame.Rect((screen.get_width()-1,0),(1,screen.get_height()))
    left = pygame.Rect((0,0),(1,screen.get_height()))
    for thing in enemies:
      thing.collisions(screen)
      thing.show(screen)
    boxes[0].collisions(screen)
    boxes[0].show(screen)
    pygame.display.flip()
    pygame.event.pump()
    # print(clock.get_fps())
    clock.tick(60)