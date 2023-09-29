import random
import GameSettings
import pygame
import os

temp = pygame.image.load(os.path.join('assets', 'enemy.png'))
enemy_sprite = pygame.transform.scale(temp, (GameSettings.enemy_width, GameSettings.enemy_height))

class Enemies():

    def __init__(self):
        self.enemy_info = []
        self.enemy_total_count = GameSettings.enemy_count
        self.enemy_cur_count = 0
        self.speed = GameSettings.enemy_speed
        self.sprite = enemy_sprite
    
    def spawn_enemy(self, player_x_cor, player_y_cor):
        if self.enemy_cur_count >= self.enemy_total_count:
            pass
        else:
            getting_loc = True
            while getting_loc:
                x, y = random.randint(100, 1100), random.randint(75, 560)
                dis = (abs(player_x_cor - x) ** 2 + abs(player_y_cor - y) ** 2) ** 0.5
                if dis > 300:
                    self.enemy_info.append((x, y))
                    self.enemy_cur_count += 1
                    getting_loc = False
    
    def update_enemies(self, player_x_cor, player_y_cor, player_rect):
        collision_info = []
        for i in range(len(self.enemy_info)):
            # Updating enemy position towards player & 'normalizing' the path
            enemy_cur_position = self.enemy_info[i]
            direction = (player_x_cor, player_y_cor) - pygame.Vector2(enemy_cur_position)
            if direction.length_squared() > 0:
                direction.normalize_ip()
            test_enemy_pos = enemy_cur_position
            test_enemy_pos += direction * self.speed
            enemy_rect = self.sprite.get_rect(topleft=test_enemy_pos)
            if pygame.Rect.colliderect(player_rect, enemy_rect) == True:
                collision_info.append("X")
            else:
                collision_info.append(" ")
            for j in range(len(self.enemy_info)):
                second_enemy_rect = self.sprite.get_rect(topleft=self.enemy_info[j])
                if pygame.Rect.colliderect(enemy_rect, second_enemy_rect) == True:
                    break
            if "X" not in collision_info:
                self.enemy_info[i] = test_enemy_pos