import pygame
import os
import random
import time



## Would like to add directionality to the enemy sprite as well as add heart image for how much health we have
## Would also like to add main menu that displays the highscore and doesn't have it in game
## Maybe add different enemies with different movement AIs?
## Maybe introduce different weapons that could be selected in the main menu after achieving a certain highscore?


with open("data.csv", "r") as file:
    highscore = int(file.readline())
    file.close()

def update_highscore(highscore, score):
    if score > highscore:
        with open("data.csv", "w") as file:
            file.write(str(score))
        file.close()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT  = 1280, 720 
WHITE = (255, 255, 255)
FPS = 60
MOVESPEED = 75
TITLE = "Bombs-Away"
ENEMY_SPEED = 3
health = 3

#initializing pygame
pygame.init()

# defining the size of the window
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Putting Image as background
backgroundImage = pygame.image.load(os.path.join('assets', 'background.png'))
background = pygame.transform.scale(backgroundImage, (WINDOW_WIDTH, WINDOW_HEIGHT))

#Making Character
characterX = 200
characterY = 150
characterDirection = "right"
characterImageLeft = pygame.image.load(os.path.join('assets', 'character_left.png'))
characterImageRight = pygame.image.load(os.path.join('assets', 'character_right.png'))
characterLeft = pygame.transform.scale(characterImageLeft, (150, 130))
characterRight = pygame.transform.scale(characterImageRight, (150, 130))

# Making Enemy
draw_enemy = True
enemyX = 1000
enemyY = 500
enemyDirection = "left"
enemyImage = pygame.image.load(os.path.join('assets', 'enemy.png'))
enemy = pygame.transform.scale(enemyImage, (150, 130))

# Making Bombs to Drop
bombImage = pygame.image.load(os.path.join('assets', 'bomb.png'))
bomb = pygame.transform.scale(bombImage, (75, 50))

# Creating a score
score = 0
font = pygame.font.Font(None, 36)


# Removes the enemy and gives it a new random location to be redrawn at
def respawn_enemy():
    global draw_enemy, enemyX, enemyY
    draw_enemy = False
    enemyX = random.randint(1, 1280)
    enemyY = random.randint(1, 720)
    draw_enemy = True

# Draws what will be on the screen each frame
def draw_window(draw_enemy, bombX, bombY, draw_bomb, score, health, highscore):
    win.blit(background, (0, 0))

    # Adding very left/right direction animation to character
    if characterDirection == "right":
        win.blit(characterRight, (characterX, characterY))
    else:
        win.blit(characterLeft, (characterX, characterY))

    # Adding the enemy
    if draw_enemy == True:
        win.blit(enemy, (enemyX, enemyY))

    # Dropping a bomb
    if draw_bomb == True:
        win.blit(bomb, (bombX, bombY))

    # Adding the Score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    win.blit(score_text, (10, 10))
    highscore_text = font.render("Highscore: " + str(highscore), True, (255, 255, 255))
    win.blit(highscore_text, (10, 50))

    # Adding "Health"
    health_text = font.render("Health: " + str(health), True, (255, 255, 255))
    win.blit(health_text, (1100, 10))

    # Calls the screen to update
    pygame.display.update()

# Game Logic Loop
def main():
    global characterY, characterX, characterDirection, enemyX, enemyY, draw_enemy, score, health, highscore
    bombX = 0
    bombY = 0
    draw_bomb = False
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    characterX -= MOVESPEED
                    characterDirection = "left"
                elif event.key == pygame.K_d:
                    characterX += MOVESPEED
                    characterDirection = "right"
                elif event.key == pygame.K_w:
                    characterY -= MOVESPEED
                elif event.key == pygame.K_s:
                    characterY += MOVESPEED
                elif event.key == pygame.K_q:
                    bombX = characterX
                    bombY = characterY
                    bombY += 100
                    if characterDirection == "right":
                        bombX += 100
                    draw_bomb = True

        # Making enemy move towards player
        dx = characterX - enemyX
        dy = characterY - enemyY
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance != 0:
            enemyX += dx / distance * ENEMY_SPEED
            enemyY += dy / distance * ENEMY_SPEED
        if distance < 50:
            respawn_enemy()
            health -= 1
        
        # Seeing if the enemy is in range of the bomb
        if draw_bomb == True:
            dx = enemyX - bombX
            dy = enemyY - bombY
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance < 100:
                respawn_enemy()
                draw_bomb = False
                score += 1
        if health == 0:
            update_highscore(highscore, score)
            run = False
        draw_window(draw_enemy, bombX, bombY, draw_bomb, score, health, highscore)


    pygame.quit()

if __name__ == "__main__":
    main()