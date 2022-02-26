import pygame
import os

player = pygame.image.load("img/p.png")
cactusi = pygame.image.load("img/c.png")
ground = pygame.image.load("img/road.png")

timer = 0
world = 1
clock = pygame.time.Clock()
fps = 120

width = 1200
height = 700

window = pygame.display.set_mode((width, height))

def world1():
    window.fill((255,255,255))
    c_g.update()
    c_g.draw(window)
    road_group.update()
    road_group.draw(window)
    p_group.update()
    p_group.draw(window)
    pygame.display.update()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 510
        self.jump = False
        self.jump_acceleration = -25
        self.timer_spwn = 0

    def update(self):
        self.timer_spwn += 1
        if self.timer_spwn / fps > 1:
            cactus = C()
            c_g.add(cactus)
            self.timer_spwn = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            self.jump = True
        if self.jump:
            if self.jump_acceleration <= 25:
                self.rect.y += self.jump_acceleration
                self.jump_acceleration += 1
            else:
                self.jump = False
                self.jump_acceleration = -25
        if pygame.sprite.spritecollide(self, c_g, False):
            print("check")

class C(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cactusi
        self.rect = self.image.get_rect()
        self.rect.x = 1350
        self.rect.y = 500
    def update(self):
        self.rect.x -= 5

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 600
        
c_g = pygame.sprite.Group()

pl = Player()
p_group = pygame.sprite.Group()
p_group.add(pl)

road = Ground()
road_group = pygame.sprite.Group()
road_group.add(road)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if world == 1:
        world1()

    clock.tick(fps)
