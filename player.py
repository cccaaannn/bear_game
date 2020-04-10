import pygame
import math

class player():
    def __init__(self, screen, screen_resolution, player_image_size = (50, 50), player_image_path = "images/player.png"):
        # jump stuff
        self.going_up = False
        self.going_down = False
        self.mid_air = False

        self.air_time = 50
        self.air_time_counter = self.air_time
        self.max_jump_height = 140
        self.jump_speed = 0.3

        # duck stuff
        self.is_ducked = False
        self.will_duck = False


        self.base_position = {"x":20, "y":screen_resolution[1]-player_image_size[1]}


        self.screen = screen
        self.screen_resolution = screen_resolution
        self.player_image_size = player_image_size

        temp_image = pygame.image.load(player_image_path).convert_alpha()
        self.player_image = pygame.transform.scale(temp_image, player_image_size)
        self.player_position = {"x":self.base_position["x"], "y":self.base_position["y"]}

    def draw_player(self):
        self.screen.blit(self.player_image, (self.player_position["x"],self.player_position["y"]))
    
    def get_hit_box(self):
        hit_box = self.player_image.get_rect()
        hit_box[0] = self.player_position["x"]
        hit_box[1] = self.player_position["y"]
        return hit_box
    
    def is_collided(self, rect):
        # return self.get_hit_box().colliderect(rect)
        player_hitbox = self.get_hit_box()
        distance = math.sqrt((math.pow(rect[0]-player_hitbox[0],2) + (math.pow(rect[1]-player_hitbox[1],2))))
        if distance < self.player_image_size[0]:
            return True
        else:
            return False

    def duck(self):
        self.player_position["y"] += 25
        self.is_ducked = True
        self.will_duck = False
        
    def unduck(self):
        self.player_position["y"] -= 25
        self.is_ducked = False


    def jump(self):
        # print(self.player_position["x"],self.player_position["y"])
        if(self.going_up):
            self.player_position["y"] -= self.jump_speed
            if(self.player_position["y"] <= self.base_position["y"] - self.max_jump_height):
                self.going_up = False
                self.mid_air = True
        
        elif(self.mid_air):
            self.air_time_counter -= 1
            if(self.air_time_counter <= 0):
                self.mid_air = False
                self.going_down = True

        elif(self.going_down):
            self.player_position["y"] += self.jump_speed
            if(self.player_position["y"] >= self.base_position["y"]):
                self.going_up = False
                self.going_down = False
                self.mid_air = False       
                self.air_time_counter = self.air_time

    def start_jumping(self, air_time_counter):
        self.set_air_time_counter(air_time_counter)
        self.going_up = True

    def is_jumping(self):
        if(self.going_down or self.going_up or self.mid_air):
            return True
        else:
            return False

    def set_air_time_counter(self, air_time_counter):
        self.air_time_counter = air_time_counter