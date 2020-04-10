import pygame

class obstacle():
    def __init__(self, screen, screen_resolution, obstacle_image_path, obstacle_image_size = (50, 50)):

        self.base_position = {"x":screen_resolution[0]+20, "y":screen_resolution[1]-obstacle_image_size[1]}

        self.obstacle_moveing_speed = 0.25


        self.screen = screen
        self.screen_resolution = screen_resolution
        self.obstacle_image_size = obstacle_image_size

        temp_image = pygame.image.load(obstacle_image_path).convert_alpha()
        self.obstacle_image = pygame.transform.scale(temp_image, obstacle_image_size)

        self.obstacle_position = {"x":self.base_position["x"], "y":self.base_position["y"]}
  
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

    def get_random_obstacle_position(self):
        pass



class tree(obstacle):
    def __init__(self, screen, screen_resolution, obstacle_image_path='images/tree.png', obstacle_image_size=(40,60)):
        super().__init__(screen, screen_resolution, obstacle_image_path=obstacle_image_path, obstacle_image_size=obstacle_image_size)
