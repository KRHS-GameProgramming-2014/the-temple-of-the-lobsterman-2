import pygame, sys, random
from Wall import Wall
from Tile import Tile
from StartBlock import StartBlock
from EndBlock import EndBlock
from Level import Level
from Player import Player
from Enemy2 import Enemy
pygame.init()

clock = pygame.time.Clock()

width = 900
height = 600
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)


tiles = pygame.sprite.Group()
players = pygame.sprite.Group()
startBlocks = pygame.sprite.Group()
endBlocks = pygame.sprite.Group()
walls = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Tile.containers = (all, tiles)
Player.containers = (all, players)
StartBlock.containers = (all, startBlocks)
EndBlock.containers = (all, endBlocks)
Wall.containers = (all, walls)

level = Level(size, 30)
level.loadLevel(1)
player = Player(startBlocks.sprites()[0].rect.center)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.go("up")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.go("down")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("left")
            if event.key == pygame.K_x:
                player.go("attack")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.go("stop up")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.go("stop down")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("stop left")
    
    playersHitWalls = pygame.sprite.groupcollide(players, walls, False, False)
    
    for player in playersHitWalls:
			for wall in playersHitWalls[player]:
				player.collideWall(wall)
    
    all.update(width, height)
        
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)

        
