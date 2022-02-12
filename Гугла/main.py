import pygame
import os

player = pygame.image.load("img/p.png")
cactusi = pygame.image.load("img/c.png")

timer = 0
world = 1
clock = pygame.time.Clock()
fps = 120

width = 1200
height = 700

window = pygame.display.set_mode((width, height))

def world1():
    window.fill((255,255,255))
    p_group.update()
    p_group.draw(window)
    c_g.update()
    c_g.draw(window)
    pygame.display.update()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 500
        self.jump = False
        self.jump_acceleration = -21

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            self.jump = True
        if self.jump:
            if self.jump_acceleration <= 20:
                self.rect.y += self.jump_acceleration
                self.jump_acceleration += 0.7
            else:
                self.jump = False
                self.jump_acceleration = -20
        if pygame.sprite.spritecollide(self, c_g, False):
            print("fdgfh")

class C(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cactusi
        self.rect = self.image.get_rect()
        self.rect.x = 1350
        self.rect.y = 500
    def update(self):
        self.rect.x -= 5
        cactus = C()
        c_g = pygame.sprite.Group()
        c_g.add(cactus)

pl = Player()
p_group = pygame.sprite.Group()
p_group.add(pl)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if world == 1:
        world1()

    clock.tick(fps)
