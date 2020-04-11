import pygame

class obstacle():
    def __init__(self, screen, screen_resolution, obstacle_image, obstacle_moveing_speed, obstacle_image_size):

        self.base_position = {"x":screen_resolution[0]+20, "y":screen_resolution[1]-obstacle_image_size[1]}
        self.obstacle_position = {"x":self.base_position["x"], "y":self.base_position["y"]}

        self.obstacle_moveing_speed = obstacle_moveing_speed

        self.screen = screen
        self.screen_resolution = screen_resolution
        self.obstacle_image_size = obstacle_image_size
        self.obstacle_image = obstacle_image
        

        
  
    def __del__(self):
        pass
    
    def delete_obstacle_if_needed(self):
        if(self.get_hit_box()[0] < -50):
            del self
            return True
        else:
            return False

    def draw_obstacle(self):
        self.screen.blit(self.obstacle_image, (self.obstacle_position["x"],self.obstacle_position["y"]))

    def move_obstacle(self):
        self.obstacle_position["x"] -= self.obstacle_moveing_speed

    def get_hit_box(self):
        hit_box = self.obstacle_image.get_rect()
        hit_box[0] = self.obstacle_position["x"]
        hit_box[1] = self.obstacle_position["y"]
        return hit_box

    def get_pos(self):
        return self.obstacle_position

    def get_base_position(self):
        return self.base_position

    def set_obstacle_moveing_speed(self, new_speed):
        self.obstacle_moveing_speed = new_speed
    
    def get_obstacle_moveing_speed(self):
        return self.obstacle_moveing_speed



class tree(obstacle):
    def __init__(self, screen, screen_resolution, obstacle_image, obstacle_moveing_speed = 0.25, obstacle_image_size=(30,50)):
        super().__init__(screen, screen_resolution, obstacle_image=obstacle_image, obstacle_moveing_speed=obstacle_moveing_speed, obstacle_image_size=obstacle_image_size)


class bird(obstacle):
    def __init__(self, screen, screen_resolution, obstacle_image, obstacle_moveing_speed = 0.25, obstacle_image_size=(40,30)):
        super().__init__(screen, screen_resolution, obstacle_image=obstacle_image, obstacle_moveing_speed=obstacle_moveing_speed, obstacle_image_size=obstacle_image_size)
        self.base_position = {"x":screen_resolution[0]+20, "y":screen_resolution[1]-obstacle_image_size[1]-35}
        self.obstacle_position = {"x":self.base_position["x"], "y":self.base_position["y"]}

