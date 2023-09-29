import pygame
import GameSettings
from Player import Player
from Enemies import Enemies
import os

# Things to work on this shit game:
# 1. Stop enemies from running into player by detecting distance from enemy to player within enemy update
# 2. Stop enemies from over lapping with one another by imploying a square point system and check whether all of the points of one square fall within the ranges of the other squares bounds
# 3. Make it so the enemies can die when they collide with the sword and respawn
# 4. Add death sounds to the enemies
# 5. Add a main menu to start the game
# 6. Add upgrade system
# 7. Imploy dropping system where every now and then you can even get a heart but don't overheal unless you get an upgrade maybe?
# 8. Maybe impliment new enemies into the game?

pygame.init()
win = pygame.display.set_mode(GameSettings.resolution)
pygame.display.set_caption(GameSettings.title)
pygame.mixer.init()
game_music = pygame.mixer.Sound(os.path.join('assets', 'music.mp3'))
game_music.play()
game_music.set_volume(0.1)

player = Player()
enemies = Enemies()

def main():
    
    game_running = True
    while game_running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if player.attack_cooldown == 0:
                    player.start_attack_animation = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.player_left()
            player.direction = "west"
            player.ready = True
        if keys[pygame.K_d]:
            player.player_right()
            player.direction = "east"
        if keys[pygame.K_w]:
            player.player_up()
            player.direction = "north"
        if keys[pygame.K_s]:
            player.player_down()
            player.direction = "south"
        
        if player.ready:
            enemies.spawn_enemy(player.x_cor, player.y_cor)
            enemies.update_enemies(player.x_cor, player.y_cor, player.get_rect())

        draw_window()

def draw_window():
    pygame.time.Clock().tick(GameSettings.fps)
    win.blit(GameSettings.background, (0,0))

    # Drawing Enemies
    for i in range(len(enemies.enemy_info)):
        win.blit(enemies.sprite, enemies.enemy_info[i])
    
    # Player Attack configuration
    if player.attack_cooldown > 0:
        player.attack_cooldown -= 1
    else:
        if player.start_attack_animation == True or player.attack_frame_counter > 0:
            if player.start_attack_animation == True:
                player.start_attack_animation = False
                player.attack_frame_counter = GameSettings.player_attack_frame_count
            else:
                if player.attack_frame_counter == 1:
                    player.attack_cooldown = GameSettings.player_attack_cooldown
                player.attack_frame_counter -= 1
                win.blit(GameSettings.get_weapon_sprite(player.direction), GameSettings.get_weapon_location(player.direction, player.x_cor, player.y_cor))
    # Drawing Players Hearts
    for i in range(player.health):
        win.blit(GameSettings.heart, (15 + i * 35, 15))

    # Game debugging
    font = pygame.font.Font(None, 36)
    text = font.render(f"attack cooldown: {player.attack_cooldown}", True, (255, 255, 255))
    win.blit(text, (500,0))

    win.blit(player.get_player_sprite(), (player.x_cor, player.y_cor))
    win.blit(GameSettings.testing, (player.x_cor, player.y_cor))
    player.get_rect()

    pygame.display.update()

if __name__ == '__main__':
    main()