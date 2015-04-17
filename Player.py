import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):  
        pygame.sprite.Sprite.__init__(self, self.containers)    
        self.upImages = [pygame.image.load("Resources/Objects/Player/Briansteelup1.PNG"),
                         pygame.image.load("Resources/Objects/Player/Briansteelup2.PNG"),
                         pygame.image.load("Resources/Objects/Player/Briansteelup3.PNG")]
        self.downImages = [pygame.image.load("Resources/Objects/Player/Briansteeldown1.PNG"),
                           pygame.image.load("Resources/Objects/Player/Briansteeldown2.PNG"),
                           pygame.image.load("Resources/Objects/Player/Briansteeldown3.PNG")]
        self.leftImages = [pygame.image.load("Resources/Objects/Player/Briansteelleft1.PNG"),
                           pygame.image.load("Resources/Objects/Player/Briansteelleft2.PNG"),
                           pygame.image.load("Resources/Objects/Player/Briansteelleft3.PNG")]
        self.rightImages = [pygame.image.load("Resources/Objects/Player/Briansteelright1.PNG"),
                            pygame.image.load("Resources/Objects/Player/Briansteelright2.PNG"),
                            pygame.image.load("Resources/Objects/Player/Briansteelright3.PNG")]
        self.upImages = [pygame.image.load("Resources/Objects/Player/Briansteelup1.PNG"),
                            pygame.image.load("Resources/Objects/Player/Briansteelup2.PNG"),
                            pygame.image.load("Resources/Objects/Player/Briansteelup3.PNG")]
        self.control =  [pygame.image.load("Resources/Objects/Player/capture3.PNG"),
                            pygame.image.load("Resources/Objects/Player/capture4.PNG")]                  
        self.heart =    [pygame.image.load("Resources/Objects/Player/emptyheart.PNG"),
                            pygame.image.load("Resources/Objects/Player/halfheart.PNG"),
                            pygame.image.load("Resources/Objects/Player/heart.PNG"),
                            pygame.image.load("Resources/Objects/Player/onethirdheart.PNG")]
        self.pain =     [pygame.image.load("Resources/Objects/Player/playerpaindown.PNG"),
                            pygame.image.load("Resources/Objects/Player/playerpainleft.PNG"),
                            pygame.image.load("Resources/Objects/Player/playerpainright.PNG"),
                            pygame.image.load("Resources/Objects/Player/playerpainup.PNG")]                  
        self.stabdown = [pygame.image.load("Resources/Objects/Player/stabdown.PNG"),
                            pygame.image.load("Resources/Objects/Player/stabdown2.PNG"),
                            pygame.image.load("Resources/Objects/Player/stabdown3.PNG")]
        self.stableft = [pygame.image.load("Resources/Objects/Player/stableft1.PNG"),
                            pygame.image.load("Resources/Objects/Player/stableft2.PNG"),
                            pygame.image.load("Resources/Objects/Player/stableft3.PNG")]
        self.stabright =[pygame.image.load("Resources/Objects/Player/stabright1.PNG"),
                            pygame.image.load("Resources/Objects/Player/stabright2.PNG"),
                            pygame.image.load("Resources/Objects/Player/stabright3.PNG")]
        self.stabup =   [pygame.image.load("Resources/Objects/Player/stabup.PNG"),
                            pygame.image.load("Resources/Objects/Player/stabup2.PNG"),
                            pygame.image.load("Resources/Objects/Player/stabup3.PNG")]
        self.knifethrowing = [pygame.image.load("Resources/Objects/Player/throwing knife.PNG")]                                         
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.maxSpeed = 5  
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.attacking = False             

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
                self.speedx = 0
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.didBounceY = True
                self.speedx = 0
                #print "hit xWall"
    
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 1
        else:
            self.waitCount = 0
            self.changed = True
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
                if self.attacking:
                    self.attacking = False
        
        if self.changed:    
            if self.facing == "up":
                if self.attacking:
                    self.images = self.stabup
                else:
                    self.images = self.upImages
            elif self.facing == "down":
                if self.attacking:
                    self.images = self.stabdown
                else:
                    self.images = self.downImages
            elif self.facing == "right":
                if self.attacking:
                    self.images = self.stabright
                else:
                    self.images = self.rightImages
            elif self.facing == "left":
                if self.attacking:
                    self.images = self.stableft
                else:
                    self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def collideWall(self, other):
        if not self.didBounceX:
            self.speedx = -self.speedx
            self.move()
            self.move()
            self.speedx = 0
            self.didBouncex = True
        if not self.didBounceY:
            self.speedy = -self.speedy
            self.move()
            self.move()
            self.move()
            self.speedy = 0
            self.didBounceY = True
            #print "hit Ball"
    
    def go(self, direction):
        if direction == "attack":
            self.changed = True
            self.speedx = 0
            self.speedy = 0
            self.attacking = True
            self.frame = 0
            self.waitCount = 0
        if direction == "up":
            self.facing = "up"
            self.changed = True
            self.speedy = -self.maxSpeed
        elif direction == "stop up":
            self.speedy = 0
        elif direction == "down":
            self.facing = "down"
            self.changed = True
            self.speedy = self.maxSpeed
        elif direction == "stop down":
            self.speedy = 0
            
        if direction == "right":
            self.facing = "right"
            self.changed = True
            self.speedx = self.maxSpeed
        elif direction == "stop right":
            self.speedx = 0
        elif direction == "left":
            self.facing = "left"
            self.changed = True
            self.speedx = -self.maxSpeed
        elif direction == "stop left":
            self.speedx = 0

    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
