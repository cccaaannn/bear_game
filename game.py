import pygame
import random
import gc
from player import player as create_player
from obstacle import tree as create_tree
from obstacle import bird as create_bird

# init window
pygame.init()
screen_resolution = (800,300)
screen = pygame.display.set_mode(screen_resolution)
pygame.display.set_caption("BEAR")
game_icon = pygame.image.load("images/player.png")
pygame.display.set_icon(game_icon)


# set game settings
tree_image_size = (40, 50)
bird_image_size = (40, 30)
player_image_size = (50, 50)
player_image_outline = (40, 45)
long_jump_duration = 370
short_jump_duration = 50
background_x = 0
score = 0
frame_counter = 0
running = True


# load images
background = pygame.image.load('images/background.png').convert_alpha()
background = pygame.transform.scale(background, (1600,300))

player_image = pygame.image.load("images/player.png").convert_alpha()
player_image = pygame.transform.scale(player_image, player_image_size)

tree_image = pygame.image.load("images/tree.png").convert_alpha()
tree_image = pygame.transform.scale(tree_image, tree_image_size)

bird_image = pygame.image.load("images/bird.png").convert_alpha()
bird_image = pygame.transform.scale(bird_image, bird_image_size)

# set fonts
comicsans20 = pygame.font.SysFont('Comic Sans MS', 20)
comicsans30 = pygame.font.SysFont('Comic Sans MS', 30)
comicsans50 = pygame.font.SysFont('Comic Sans MS', 50)


# instansiate player and trees list
player = create_player(screen, screen_resolution, player_image, player_image_size=player_image_outline)
obstacles = []





def gameover():
    while True:
        # gameover info
        textsurface = comicsans50.render('Game Over', False, (0, 0, 0))
        textsurface2 = comicsans20.render('(press right to continue)', False, (0, 0, 0))

        screen.blit(textsurface,(250,0))
        screen.blit(textsurface2,(250,50))
        
        # gameover screen events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    return True
        
        pygame.display.update()


def create_obstacle(rand_interval_tree=1000, rand_interval_bird=2000, distance_more_than=200, distance_less_than=30, obstacle_moveing_speed=0.25):
    if(random.randint(0, rand_interval_tree) == 0):
        if(obstacles):
            base_pos = obstacles[-1].get_base_position()["x"]
            current_pos = obstacles[-1].get_pos()["x"]
            if(base_pos - current_pos > distance_more_than or base_pos - current_pos < distance_less_than):
                obstacles.append(create_tree(screen, screen_resolution, tree_image, obstacle_moveing_speed))  
        else:
            obstacles.append(create_tree(screen, screen_resolution, tree_image, obstacle_moveing_speed))

    if(random.randint(0, rand_interval_bird) == 0):
        if(obstacles):
            base_pos = obstacles[-1].get_base_position()["x"]
            current_pos = obstacles[-1].get_pos()["x"]
            if(base_pos - current_pos > distance_more_than or base_pos - current_pos < distance_less_than):
                obstacles.append(create_bird(screen, screen_resolution, bird_image, obstacle_moveing_speed))
        else:
            obstacles.append(create_bird(screen, screen_resolution, bird_image, obstacle_moveing_speed))





# game loop
while running:
    
    # moving background 
    screen.fill((255,255,255))
    screen.blit(background,(background_x,0))
    background_x -= 0.1
    if(background_x <= -800):
        background_x = 0


    # calculate and show score
    textsurface = comicsans30.render('SCORE:{0}'.format(score), False, (0, 0, 0))
    screen.blit(textsurface,(10,10))
    if(frame_counter%10 == 0):
        score += 1
    frame_counter += 1


    # player actions
    player.draw_player()

    if(player.is_jumping()):
        player.jump()

    if(player.will_duck):
        if(not player.is_jumping() and not player.is_ducked):
            player.duck()


    
    # create obstacles
    if(score < 1000):
        create_obstacle(obstacle_moveing_speed=0.3)
    elif(score < 2000):
        create_obstacle(obstacle_moveing_speed=0.3)
    elif(score < 3000):
        create_obstacle(obstacle_moveing_speed=0.35)
    elif(score < 4000):
        create_obstacle(obstacle_moveing_speed=0.4)
    elif(score < 5000):
        create_obstacle(obstacle_moveing_speed=0.45)
    else:
        create_obstacle(obstacle_moveing_speed=0.5)
    

    # move, delete check collision
    for obstacle in obstacles:
        obstacle.move_obstacle()
        obstacle.draw_obstacle()
        if(obstacle.delete_obstacle_if_needed()):
            obstacles.remove(obstacle)
        
        # gameover screen
        if(player.is_collided(obstacle.get_hit_box())):
            running = gameover()
            if(running):
                player = create_player(screen, screen_resolution, player_image, player_image_size=player_image_outline)
                obstacles.clear()
                score = 0
                gc.collect()



    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # long jump on hold
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if(not player.is_jumping() and not player.is_ducked):
                    player.start_jumping(long_jump_duration)
        
            if event.key == pygame.K_DOWN:
                player.will_duck = True

        if event.type == pygame.KEYUP:
            # short jump on tap
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if(player.is_jumping()):
                    player.set_air_time_counter(short_jump_duration)
                    
            if event.key == pygame.K_DOWN:
                if(player.is_ducked):
                    player.unduck()



    pygame.display.update()