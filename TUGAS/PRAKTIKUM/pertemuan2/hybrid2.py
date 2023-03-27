import pygame

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Player(GameObject, pygame.sprite.Sprite):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5
        if keys[pygame.K_UP]:
            self.y -= 5
        if keys[pygame.K_DOWN]:
            self.y += 5
        self.rect.x = self.x
        self.rect.y = self.y

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

player = Player(320, 240)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)