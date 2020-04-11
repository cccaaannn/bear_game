import pygame
import random
import gc
import sys
from player import player as create_player
from obstacle import tree as create_tree
from obstacle import bird as create_bird
class bear_game():
    def __init__(self):
        self.init_window()
        self.set_game_options()
        self.load_game_elements()
        self.init_game()
        self.start_menu()

    # game options
    def init_window(self):
        pygame.init()
        self.screen_resolution = (800,300)
        self.screen = pygame.display.set_mode(self.screen_resolution)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("BEAR")
        self.game_icon = pygame.image.load("images/player.png")
        pygame.display.set_icon(self.game_icon)

    def set_game_options(self):
        self.background_image_size = (1600,300)
        self.tree_image_size = (40, 50)
        self.bird_image_size = (40, 30)
        self.player_image_size = (50, 50)
        self.player_image_outline = (40, 45)

        self.background_path = "images/background.png"
        self.tree_image_path = "images/tree.png"
        self.bird_image_path = "images/bird.png"
        self.player_image_path = "images/player.png"
        
        self.long_jump_duration = 30
        self.short_jump_duration = 3

    def load_game_elements(self):
        # load images
        background = pygame.image.load(self.background_path).convert_alpha()
        self.background = pygame.transform.scale(background, self.background_image_size)

        player_image = pygame.image.load(self.player_image_path).convert_alpha()
        self.player_image = pygame.transform.scale(player_image, self.player_image_size)

        tree_image = pygame.image.load(self.tree_image_path).convert_alpha()
        self.tree_image = pygame.transform.scale(tree_image, self.tree_image_size)

        bird_image = pygame.image.load(self.bird_image_path).convert_alpha()
        self.bird_image = pygame.transform.scale(bird_image, self.bird_image_size)

        # set fonts
        self.comicsans20 = pygame.font.SysFont('Comic Sans MS', 20)
        self.comicsans30 = pygame.font.SysFont('Comic Sans MS', 30)
        self.comicsans50 = pygame.font.SysFont('Comic Sans MS', 50)
        self.comicsans70 = pygame.font.SysFont('Comic Sans MS', 70)
        
    def init_game(self):
        self.score = 0
        self.background_x = 0
        self.frame_counter = 0
        self.player = create_player(self.screen, self.screen_resolution, self.player_image, player_image_size=self.player_image_outline)
        self.obstacles = []

    def reset_game(self):
        self.obstacles.clear()
        gc.collect()
        self.init_game()
    
    # menus
    def start_menu(self):
        selected_menu_item = 0
        menu_element_count = 3
        while True:
            self.screen.fill((255,255,255))
            self.screen.blit(self.background,(self.background_x,0))
            self.background_x -= 2
            if(self.background_x <= -800):
                self.background_x = 0
            

            if(selected_menu_item == 0):
                start_game_text = self.comicsans50.render("START GAME", False, (255, 0, 0))
                high_scores_text = self.comicsans50.render("HIGH SCORES", False, (0, 0, 0))
                quit_game_text = self.comicsans50.render("QUIT", False, (0, 0, 0))
            elif(selected_menu_item == 1):
                start_game_text = self.comicsans50.render("START GAME", False, (0, 0, 0))
                high_scores_text = self.comicsans50.render("HIGH SCORES", False, (255, 0, 0))
                quit_game_text = self.comicsans50.render("QUIT", False, (0, 0, 0))
            elif(selected_menu_item == 2):
                start_game_text = self.comicsans50.render("START GAME", False, (0, 0, 0))
                high_scores_text = self.comicsans50.render("HIGH SCORES", False, (0, 0, 0))
                quit_game_text = self.comicsans50.render("QUIT", False, (255, 0, 0))

            self.screen.blit(start_game_text,(self.screen_resolution[0]/4+30,self.screen_resolution[1]/4-40))
            self.screen.blit(high_scores_text,(self.screen_resolution[0]/4+30,self.screen_resolution[1]/4+20))
            self.screen.blit(quit_game_text,(self.screen_resolution[0]/4+130,self.screen_resolution[1]/4+80))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        selected_menu_item += 1
                        selected_menu_item = selected_menu_item%menu_element_count
                    if event.key == pygame.K_UP:
                        selected_menu_item -= 1
                        selected_menu_item = selected_menu_item%menu_element_count
                    if event.key == pygame.K_RETURN:
                        if(selected_menu_item == 0):
                            self.game()
                        elif(selected_menu_item == 1):
                            self.high_scores()
                        elif(selected_menu_item == 2):
                            sys.exit()

            pygame.display.update()
            self.clock.tick(60)

    def high_scores(self):
        while True:
            self.screen.fill((255,255,255))
            self.screen.blit(self.background,(self.background_x,0))
            self.background_x -= 2
            if(self.background_x <= -800):
                self.background_x = 0
            
            # TODO add high scores

            back_text = self.comicsans50.render("BACK", False, (255, 0, 0))
            self.screen.blit(back_text,(50,self.screen_resolution[1]-70))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                        self.start_menu()
                        
            pygame.display.update()
            self.clock.tick(60)

    def gameover(self):
        while True:
            # gameover info
            game_over_text = self.comicsans70.render('Game Over', False, (200, 0, 0))
            continue_text = self.comicsans20.render('(press enter to continue esc to menu)', False, (0, 0, 0))

            self.screen.blit(game_over_text,(self.screen_resolution[0]/4,self.screen_resolution[1]/4-20))
            self.screen.blit(continue_text,(self.screen_resolution[0]/4,self.screen_resolution[1]/4+60))
            
            # gameover screen events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.reset_game()
                        self.game()
                    if event.key == pygame.K_ESCAPE:
                        self.reset_game()
                        self.start_menu()

            pygame.display.update()
            self.clock.tick(60)

    # game
    def create_obstacle(self, rand_interval_tree=75, rand_interval_bird=150, distance_more_than=200, distance_less_than=30, obstacle_moveing_speed=6):
        if(random.randint(0, rand_interval_tree) == 0):
            if(self.obstacles):
                base_pos = self.obstacles[-1].get_base_position()["x"]
                current_pos = self.obstacles[-1].get_pos()["x"]
                if(base_pos - current_pos > distance_more_than or base_pos - current_pos < distance_less_than):
                    self.obstacles.append(create_tree(self.screen, self.screen_resolution, self.tree_image, obstacle_moveing_speed))  
            else:
                self.obstacles.append(create_tree(self.screen, self.screen_resolution, self.tree_image, obstacle_moveing_speed))

        if(random.randint(0, rand_interval_bird) == 0):
            if(self.obstacles):
                base_pos = self.obstacles[-1].get_base_position()["x"]
                current_pos = self.obstacles[-1].get_pos()["x"]
                if(base_pos - current_pos > distance_more_than or base_pos - current_pos < distance_less_than):
                    self.obstacles.append(create_bird(self.screen, self.screen_resolution, self.bird_image, obstacle_moveing_speed))
            else:
                self.obstacles.append(create_bird(self.screen, self.screen_resolution, self.bird_image, obstacle_moveing_speed))

    def game(self):
        while True:
            # moving background 
            self.screen.fill((255,255,255))
            self.screen.blit(self.background,(self.background_x,0))
            self.background_x -= 2
            if(self.background_x <= -800):
                self.background_x = 0


            # calculate and show score
            textsurface = self.comicsans30.render('SCORE:{0}'.format(self.score), False, (0, 0, 0))
            self.screen.blit(textsurface,(10,10))
            if(self.frame_counter%10 == 0):
                self.score += 1
            self.frame_counter += 1


            # player actions
            self.player.draw_player()

            if(self.player.is_jumping()):
                self.player.jump()

            if(self.player.will_duck):
                if(not self.player.is_jumping() and not self.player.is_ducked):
                    self.player.duck()


            
            # create obstacles
            if(self.score < 100):
                self.create_obstacle(obstacle_moveing_speed=6)
            elif(self.score < 200):
                self.create_obstacle(obstacle_moveing_speed=7)
            elif(self.score < 300):
                self.create_obstacle(obstacle_moveing_speed=8)
            elif(self.score < 400):
                self.create_obstacle(obstacle_moveing_speed=9)
            elif(self.score < 500):
                self.create_obstacle(obstacle_moveing_speed=10)
            else:
                self.create_obstacle(obstacle_moveing_speed=11)
            

            # move, delete check collision obstacles
            for obstacle in self.obstacles:
                obstacle.move_obstacle()
                obstacle.draw_obstacle()
                if(obstacle.delete_obstacle_if_out_of_screen()):
                    self.obstacles.remove(obstacle)
                
                # gameover screen
                if(self.player.is_collided(obstacle.get_hit_box())):
                    self.gameover()
                        



            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    # long jump on hold
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        if(not self.player.is_jumping() and not self.player.is_ducked):
                            self.player.start_jumping(self.long_jump_duration)
                
                    if event.key == pygame.K_DOWN:
                        self.player.will_duck = True

                if event.type == pygame.KEYUP:
                    # short jump on tap
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        if(self.player.is_jumping()):
                            self.player.set_air_time_counter(self.short_jump_duration)
                            
                    if event.key == pygame.K_DOWN:
                        if(self.player.is_ducked):
                            self.player.unduck()

            pygame.display.update()
            self.clock.tick(60)

