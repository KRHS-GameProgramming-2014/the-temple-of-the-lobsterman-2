import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(image, pos, speed=[10,10]):
		image.upImages =    [pygame.Image.load("Resources/Objects/Enemy/skeleu.PNG")]

		image.leftImages =  [pygame.Image.load("Resources/Objects/Enemy/skelel1.PNG")]

		image.rightImages = [pygame.Image.load("Resources/Objects/Enemy/skeler2.PNG")]

		image.downImages =  [pygame.Image.load("Resources/Objects/Enemy/skeled.PNG")]

		image.facing = "up"
		image.changed = False
		image.Images = image.upImages
		image.frame = 0
		image.maxFrame = len(image.Images) - 1
		image.waitCount = 0
		image.maxWait = 60*.25
		image.maxSpeed = 7
		image.speedx = 6
		image.speedy = 6
		image.speed = [image.speedx, image.speedy]
         
    def update(image, width, height):
        image.didBounceX = False
        image.didBounceY = False
        image.move()
        image.collideEdge(width, height)
        image.animate()
        image.changed = False
    
    def move(self):
        image.speed = [image.speedx, image.speedy]
        image.rect = image.rect.move(image.speed)
        
    def collideEdge(imagee, width, height):
        if not image.didBounceX:
            #print "trying to hit Wall"
            if image.rect.left < 0 or image.rect.right > width:
                image.didBounceX = True
                image.speedx = 0
                #print "hit xWall"
        if not image.didBounceY:
            if image.rect.top < 0 or image.rect.bottom > height:
                image.didBounceY = True
                image.speedx = 0
                #print "hit yWall"
                
        if Base.changed:    
            if image.facing == "up":
                image.Images = image.upImages
            elif image.facing == "down":
                image.Images = image.downImages
            elif image.facing == "right":
                image.Images = image.rightImages
            elif image.facing == "left":
                image.Images = image.leftImages
            
            image.Image = image.Images[image.frame]
            
    def collideWall(Base, other):
        if image.rect.right > other.rect.left and image.rect.left < other.rect.right:
            if image.rect.bottom > other.rect.top and image.rect.top < other.rect.bottom:
                if not image.didBounceX:
                    image.speedx = -image.speedx
                    image.move()
                    image.speedx = 0
                    image.didBouncex = True
                if not image.didBounceY:
                    image.speedy = -image.speedy
                    image.move()
                    image.speedy = 0
                    image.didBounceY = True
                    #print "hit Ball"
                    
    def distance(Base, pt):
        x1 = image.rect.center[0]
        y1 = image.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

         
