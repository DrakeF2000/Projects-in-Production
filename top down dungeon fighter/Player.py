import GameSettings
import pygame
import os

temp = pygame.image.load(os.path.join('assets', 'player.png'))
temp = pygame.transform.scale(temp, (GameSettings.player_width, GameSettings.player_height))
player_north = temp
player_east = pygame.transform.rotate(temp, 270)
player_south = pygame.transform.rotate(temp, 180)
player_west = pygame.transform.rotate(temp, 90)

class Player():

    def __init__(self):
        self.x_cor = GameSettings.resolution_width / 2
        self.y_cor = 400
        self.direction = "north"
        self.start_attack_animation = False
        self.attack_frame_counter = 0
        self.attack_cooldown = 0
        self.health = GameSettings.player_health
        self.invincibility_frames = 0
        self.ready = False
        
    def get_player_sprite(self ):
        if self.direction == "north":
            return player_north
        elif self.direction == "east":
            return player_east
        elif self.direction == "south":
            return player_south
        elif self.direction == "west":
            return player_west
        else:
            return player_north

    def player_left(self):
        if self.x_cor > 100:
            self.x_cor -= GameSettings.player_speed
    
    def player_right(self):
        if self.x_cor < 1110:
            self.x_cor += GameSettings.player_speed
    
    def player_up(self):
        if self.y_cor > 75:
            self.y_cor -= GameSettings.player_speed
    
    def player_down(self):
        if self.y_cor < 560:
            self.y_cor += GameSettings.player_speed
    
    def take_damage(self):
        if self.invincibility_frames == 0:
            self.health -= 1
            self.invincibility_frames = GameSettings.invincibility_frame_count
        if self.invincibility_frames > 0:
            self.invincibility_frames -= 1
        
    def get_rect(self):
        self.rect = self.get_player_sprite().get_rect(topleft=(self.x_cor, self.y_cor))
        return self.rect