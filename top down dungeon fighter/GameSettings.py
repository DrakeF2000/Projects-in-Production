import pygame
import os

# Window Settings 
resolution = (1280, 720)
resolution_width = 1280
resolution_height = 720
title = "Dangerous Dan, The Grey Knight of the Underworld"
fps = 60

# Gameplay Settings
player_health = 5
player_speed = 7
player_attack_frame_count = 20
player_attack_cooldown = 30
standard_collision_distance = 0
invincibility_frame_count = 100

enemy_count = 1
enemy_speed = 3

# Game Sprites
player_width = 75
player_height = 100

enemy_width = 50
enemy_height = 50

temp = pygame.image.load(os.path.join('assets', 'background.png'))
background = pygame.transform.scale(temp, (resolution))

temp = pygame.image.load(os.path.join('assets', 'player_weapon.png'))
weapon_north = pygame.transform.scale(temp, (75, 150))
weapon_south = pygame.transform.rotate(weapon_north, 180)
weapon_east = pygame.transform.rotate(weapon_north, 270)
weapon_west = pygame.transform.rotate(weapon_north, 90)

temp = pygame.image.load(os.path.join('assets', 'heart.png'))
heart = pygame.transform.scale(temp, (25, 35))

temp = pygame.image.load(os.path.join('assets', 'testing.png'))
testing = pygame.transform.scale(temp, (10, 10))

# Giving game proper sprite oreintation
def get_weapon_sprite(player_direction):
    if player_direction == "north":
        return weapon_north
    elif player_direction == "east":
        return weapon_east
    elif player_direction == "south":
        return weapon_south
    elif player_direction == "west":
        return weapon_west

def get_weapon_location(player_direction, x_cor, y_cor):
    if player_direction == "north":
        return (x_cor, y_cor - 155)
    elif player_direction == "east":
        return (x_cor + 105, y_cor)
    elif player_direction == "south":
        return (x_cor, y_cor + 105)
    elif player_direction == "west":
        return (x_cor - 155, y_cor)