import pygame
import random
from player import player as plyr
from obstacle import tree as create_tree


# init window
pygame.init()
screen_resolution = (800,300)
screen = pygame.display.set_mode(screen_resolution)

# set up window
pygame.display.set_caption("BEAR")
icon = pygame.image.load("images/player.png")
pygame.display.set_icon(icon)

# set background
background = pygame.image.load('images/background.png').convert_alpha()
background = pygame.transform.scale(background, (1600,300))
background_x = 0

# instansiate player and trees list
player = plyr(screen, screen_resolution)
trees = []

comicsans20 = pygame.font.SysFont('Comic Sans MS', 20)
comicsans30 = pygame.font.SysFont('Comic Sans MS', 30)
comicsans50 = pygame.font.SysFont('Comic Sans MS', 50)

score = 0
running = True
# game loop
while running:
    
    # background 
    screen.fill((255,255,255))
    screen.blit(background,(background_x,0))
    background_x -= 0.1
    if(background_x <= -800):
        background_x = 0


    # show_score(score)
    textsurface = comicsans30.render('SCORE:{0}'.format(score), False, (0, 0, 0))
    screen.blit(textsurface,(10,10))
    score += 1

    # player
    player.draw_player()

    if(player.is_jumping()):
        player.jump()

    if(player.will_duck):
        if(not player.is_jumping() and not player.is_ducked):
            player.duck()


    
    # obstacles
    if(random.randint(0,3500) == 0):
        trees.append(create_tree(screen, screen_resolution))

    for tree in trees:
        tree.move_obstacle()
        tree.draw_obstacle()
        if(tree.delete_obstacle_if_needed()):
            trees.remove(tree)
        
        # gameover screen
        if(player.is_collided(tree.get_hit_box())):
            while running:
                textsurface = comicsans50.render('Game Over', False, (0, 0, 0))
                textsurface2 = comicsans20.render('(press right to continue)', False, (0, 0, 0))

                screen.blit(textsurface,(150,50))
                screen.blit(textsurface2,(160,100))
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:

                        for tree2 in trees:
                            del tree2
                        trees.clear()
                        score = 0
                        player = plyr(screen, screen_resolution)

                        break
                pygame.display.update()




    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if(not player.is_jumping() and not player.is_ducked):
                    player.start_jumping(370)

            if event.key == pygame.K_DOWN:
                player.will_duck = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if(player.is_jumping()):
                    player.set_air_time_counter(50)
                    
            if event.key == pygame.K_DOWN:
                if(player.is_ducked):
                    player.unduck()



    pygame.display.update()