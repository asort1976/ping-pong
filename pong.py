import pygame
pygame.init()
WW =700
WH = 500
sc = pygame.display.set_mode((WW, WH))
clock = pygame.time.Clock()
back = pygame.transform.scale(pygame.image.load('fon.png'), (700, 500))
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (15, 70))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        sc.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):

        keyp = pygame.key.get_pressed()
        if keyp[pygame.K_DOWN] and self.rect.y <427:
            self.rect.y += 5
        if keyp[pygame.K_UP] and self.rect.y >0:
            self.rect.y -= 5
n2 = Player('shtuka.png',5,5)
n3 = Player('shtuka.png',495,5)
run2= True
run = True
while run:
    if run2:
        sc.blit(back,(0,0))
        n2.update()
        n2.reset()
        n3.update()
        n3.reset()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    pygame.display.update()