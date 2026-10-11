import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invasion")

# playicon load (Initial)
# player code variable
img_player = pygame.image.load('spaceship.png')
background = pygame.image.load('jeremy-thomas-E0AHdsENmDg-unsplash.jpg')

#player variables
play_x = 368
play_y = 525
player_x_changed = 0
player_Y_changed = 0

#scores
score = 0
my_scorecard = pygame.font.Font('freesansbold.ttf',32)
text_x =650
text_y =10

def showscore(x,y):
    myscore = my_scorecard.render(f'Score : {score}',True , (255,255,255))
    screen.blit(myscore,(x,y))

#end_of_game_text
end_font = pygame.font.Font('freesansbold.ttf',40)

def final_text():
    game_over_font =end_font.render(f'Game Over',True,(255,255,255))
    screen.blit(game_over_font,(200,200))

# Enemy code variable
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_changed = []
enemy_y_changed = []
number_enemy_count = 5

for enemy in range(number_enemy_count):
    img_enemy.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0, 534))
    enemy_y.append(random.randint(0, 345))
    enemy_x_changed.append(0.5)
    enemy_y_changed.append(50)

# bullet variables
bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 500
bullet_x_changed = 0
bullet_y_changed = 3
visible_bullet = False


def player(x, y):
    screen.blit(img_player, (x, y))


def enemyfunnction(x, y,en):
    screen.blit(img_enemy[en], (x, y))


def shoot_bullet(x, y):
    screen.blit(bullet_img, (x + 16, y + 10))


# Collision of the bullet with enemy
def if_collision(x_1, x_2, y_1, y_2):
    distance = math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)

    if distance < 27:
        return True
    else:
        return False


is_running = True

while is_running:

    screen.blit(background, (0, 0))

    # Game Quit
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            is_running = False

        # Key press
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player_x_changed += -0.3

            if event.key == pygame.K_RIGHT:
                player_x_changed += 0.3

            if event.key == pygame.K_DOWN:
                player_Y_changed += -0.4

            if event.key == pygame.K_UP:
                player_Y_changed += 0.4

            if event.key == pygame.K_SPACE:

                if not visible_bullet:
                    bullet_x = play_x
                    bullet_y = play_y
                    visible_bullet = True

        # Key release
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_changed = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_Y_changed = 0

    # Change player location
    play_x += player_x_changed
    play_y -= player_Y_changed

    # Restrict player to screen
    if play_x <= 0:
        play_x = 0
    elif play_x >= 736:
        play_x = 736

    if play_y <= 0:
        play_y = 0
    elif play_y >= 510:
        play_y = 510

    # ---------------- ENEMY MOVEMENT ----------------
    for enem in range(number_enemy_count):
        #endof game 
        if enemy_y[enem] > 500:
            for k in range(number_enemy_count):
                enemy_y[k] =1000
            final_text ()
            break
        enemy_x[enem] += enemy_x_changed[enem]

        if enemy_x[enem] <= 0:
            enemy_x_changed[enem] = 0.3
            enemy_y[enem] += 50

        elif enemy_x[enem] >= 736:
            enemy_x_changed[enem] = -0.3
            enemy_y[enem] += 50

        collision = if_collision(enemy_x[enem], bullet_x, enemy_y[enem], bullet_y)
            
        if collision:
            bullet_y = 500
            visible_bullet = False
            score +=1
            enemy_x[enem] = random.randint(0, 534)
            enemy_y[enem] = random.randint(0, 345)

        enemyfunnction(enemy_x[enem], enemy_y[enem],enem)


    # ---------------- Bullet MOVEMENT ----------------

    if bullet_y <= -64:
        visible_bullet = False
        bullet_y = 500

    if visible_bullet:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_changed

    # ------ Collision detection of bullet

    

    # Draw player and enemy
    player(play_x, play_y)
    showscore(text_x,text_y)

    # Update display
    pygame.display.update()


pygame.quit()