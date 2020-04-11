import pygame
import math

class player():
    def __init__(self, screen, screen_resolution, player_image, player_image_size):
        # jump stuff
        self.going_up = False
        self.going_down = False
        self.mid_air = False

        self.air_time = 3
        self.air_time_counter = self.air_time
        self.max_jump_height = 120
        self.jump_speed = 10
        self.fall_speed = 12

        # duck stuff (will duck is required because if player holding down button while character is mid air)
        self.is_ducked = False
        self.will_duck = False


        self.base_position = {"x":20, "y":screen_resolution[1]-player_image_size[1]}
        self.player_position = {"x":self.base_position["x"], "y":self.base_position["y"]}

        self.screen = screen
        self.screen_resolution = screen_resolution
        self.player_image = player_image
        self.player_image_size = player_image_size


        
    def draw_player(self):
        """draws player to screen"""
        self.screen.blit(self.player_image, (self.player_position["x"],self.player_position["y"]))
    
    def get_hit_box(self):
        """returns current hitbox of the character"""
        hit_box = self.player_image.get_rect()
        hit_box[0] = self.player_position["x"]
        hit_box[1] = self.player_position["y"]
        return hit_box
    
    def is_collided(self, rect):
        """returns true if colision happens"""
        # return self.get_hit_box().colliderect(rect)
        player_hitbox = self.get_hit_box()
        distance = math.sqrt((math.pow(rect[0]-player_hitbox[0],2) + (math.pow(rect[1]-player_hitbox[1],2))))
        # dont collide with objects passed you
        if distance < self.player_image_size[0] and rect[0] >= player_hitbox[0]:
            return True
        else:
            return False

    def duck(self):
        """ducks"""
        self.player_position["y"] += 25
        self.is_ducked = True
        self.will_duck = False
        
    def unduck(self):
        """unducks"""
        self.player_position["y"] -= 25
        self.is_ducked = False


    def jump(self):
        """jumps"""
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
            self.player_position["y"] += self.fall_speed
            if(self.player_position["y"] >= self.base_position["y"]):
                self.going_up = False
                self.going_down = False
                self.mid_air = False       
                self.air_time_counter = self.air_time

    def start_jumping(self, air_time_counter):
        """initiates jump"""
        self.set_air_time_counter(air_time_counter)
        self.going_up = True

    def is_jumping(self):
        """returns true if character is jumping"""
        if(self.going_down or self.going_up or self.mid_air):
            return True
        else:
            return False

    def set_air_time_counter(self, air_time_counter):
        """set air time for character"""
        self.air_time_counter = air_time_counter