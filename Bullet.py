import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction):  
        pygame.sprite.Sprite.__init__(self, self.containers)   
        self.image = pygame.image.load("Resources/Objects/Projectile/Bullet.png")
        self.rect = self.image.get_rect(center = pos)
        self.maxSpeed = 5  
        if direction == "up":
            self.speedx = 0
            self.speedy = -self.maxSpeed
        elif direction == "down":
            self.speedx = 0
            self.speedy = self.maxSpeed
        elif direction == "left":
            self.speedx = -self.maxSpeed
            self.speedy = 0
        elif direction == "right":
            self.speedx = self.maxSpeed
            self.speedy = 0
        self.speed = [self.speedx, self.speedy]
                   

    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        self.move()
        self.collideEdge(width, height)
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def collideEdge(self, width, height):
        if self.rect.left < 0 or self.rect.right > width:
            self.kill()
        if self.rect.top < 0 or self.rect.bottom > height:
            self.kill()
    
    
    def collideWall(self, other):
        self.kill()
    
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
