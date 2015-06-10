import pygame

class Boss(pygame.sprite.Sprite):
    def __init__(self, pos, speed=[1,1]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImages =    [pygame.image.load("Resources/Object/Enemy/Lobsta.PNG")]
        
        self.leftImages =  [pygame.image.load("Resources/Objects/Enemy/lobstaleft1.PNG"),
                            pygame.image.load("Resources/Objects/Enemy/loibstaleft2.PNG")]
        
        self.rightImages =  [pygame.image.load("Resources/Objects/Enemy/lobstaright1.PNG"),
                             pygame.image.load("Resources/Objects/Enemy/Lobstaright2.PNG")]
        
        self.facing = "down"
        self.changed = False
        self.images = self.downImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.waitCount = 0
        self.maxWait = 60*.25
        self.maxSpeed = speed[0]
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        self.didBounceX = False
        self.didBounceY = False
        self.move()
        self.collideEdge(width, height)
        self.animate()
        self.changed = False
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def collideEdge(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.didBounceX = True
                self.speedx = -self.speedx
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.didBounceY = True
                self.speedy = -self.speedy
                #print "hit yWall"
    
    def animate(self):       
        if self.changed:    
            if self.facing == "up":
                self.images = self.upImages
            elif self.facing == "down":
                self.Images = self.downImages
            elif self.facing == "right":
                self.Images = self.rightImages
            elif self.facing == "left":
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
            
    def collideWall(self, other):
        #print "hitting"
        if not self.didBounceX:
            self.speedx = -self.speedx
            self.didBounceX = True
        if not self.didBounceY:
            self.speedy = -self.speedy
            self.didBounceY = True
            #print "hit Ball"
        self.move()
        self.move()
                    
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
