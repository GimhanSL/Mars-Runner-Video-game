import pygame
import random
pygame.init()
pygame.mixer.init()
#constants
display_info = pygame.display.Info()
width = 500
high = 650
speed = 2
move_left = False
move_right = False
player_speed = 10
score = 0
health = 5
bv = 5
rv = 5

#creating display
screen = pygame.display.set_mode((width, high))
pygame.display.set_caption("Mars Runner")


#fonts

fontk = pygame.font.SysFont("upheavtt.ttf", 48)

#sounds----------------
pygame.mixer.music.load("Sounds\\menu_sound.mp3")
pygame.mixer.music.play(-1)


#Loading images

#game UI
game_name = pygame.image.load("Start\\game_name.png")
ground_s = pygame.image.load("Start\\ground.png")
hall1= pygame.image.load("Start\\hall1.png")
hall2 = pygame.image.load("Start\\hall2.png")
hall3 = pygame.image.load("Start\\hall3.png")
space = pygame.image.load("Start\\space.png")
start_button = pygame.image.load("Start\\start_button.png")
icon = pygame.image.load("updated\\icon.png")
pygame.display.set_icon(icon)
space_rect = space.get_rect(topleft = (0,0))

play_button = pygame.image.load("Start\\Play_button.png")
exit_button = pygame.image.load("Start\\exit_button.png")
game_over_img = pygame.image.load("Start\\game_over.png")
exit_button_rect = exit_button.get_rect(center = ((width/2), (500)))
play_button_rect = play_button.get_rect(center = ((width/2),(380)))
game_over_rect = game_over_img.get_rect(center = ((width/2), (high/2)))
screen.blit(game_name, (94,64))
screen.blit(space, (0,0))

#health bar
h1 = pygame.image.load("Health\\h6.png")
h2 = pygame.image.load("Health\\h1.png")
h3 = pygame.image.load("Health\\h2.png")
h4 = pygame.image.load("Health\\h3.png")
h5 = pygame.image.load("Health\\h4.png")
h6 = pygame.image.load("Health\\h5.png")
h1_rect = h1.get_rect(topleft = (5,5))
h2_rect = h2.get_rect(topleft = (2,2))
h3_rect = h3.get_rect(topleft = (2,2))
h4_rect = h4.get_rect(topleft = (2,2))
h5_rect = h5.get_rect(topleft = (2,2))
h6_rect = h6.get_rect(topleft = (2,2))

def health_logic():
    if health == 5:
        screen.blit(h1, h1_rect)
    if health == 4:
        screen.blit(h2, h2_rect)
    if health == 3:
        screen.blit(h3, h3_rect)
    if health == 2:
        screen.blit(h4, h4_rect)
    if health == 1:
        screen.blit(h5, h5_rect)
    if health == 0:
        screen.blit(h6, h6_rect)


#Bullet
bullet = pygame.image.load("Bullet\\bullet.png")
bullet_rect = bullet.get_rect(topleft = ((width/2), (high- 30)))
bullets = []

##grass

grass1 = pygame.image.load("ground\\g1.png")
grass2 = pygame.image.load("ground\\g2.png")
grass3 = pygame.image.load("ground\\g3.png")
grass4 = pygame.image.load("ground\\g4.png")

grass1_rect1 = grass1.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
grass1_rect2 = grass1.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
grass1_rect3 = grass2.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
grass1_rect4 = grass2.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
grass1_rect5 = grass3.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
grass1_rect6 = grass3.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
grass1_rect7 = grass4.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
grass1_rect8 = grass4.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))

def grass_spawn(rect):
    rect.y += speed
    if rect.y >= high:
        rect.x, rect.y = random.randint(0, 460), 0



#player####################################################
background_img = pygame.image.load("ground\\grass.png")
player_img = pygame.image.load("player\\w1.png")
player_img1 = pygame.image.load("player\\w2.png")
player_img2 = pygame.image.load("player\\w3.png")
player_img3 = pygame.image.load("player\\w4.png")

#player_img = pygame.transform.scale(player_img, (32, 46))
player_rect = player_img.get_rect(topleft = ((width/2), (high- 30)))

player_list = [player_img,player_img1,player_img2,player_img3]

player_index = 0

def player_animations(list):
    global player_index
    player_index += 0.4
    player = list[int(player_index)]
    screen.blit(player, player_rect)
    if player_index >= (len(list)-1):
        player_index = 0

#mob###################################################

mob1 = pygame.image.load("slime\\s1.png")
mob2 = pygame.image.load("slime\\s2.png")
mob3 = pygame.image.load("slime\\s3.png")
mob4 = pygame.image.load("slime\\s4.png")

mob_list = [mob1,mob2,mob3,mob4]
mob_rect = mob1.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
mob_rect2 = mob1.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
mob_rect3 = mob1.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
mob_rect4 = mob1.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))

mob_index = 0

def mob_spawn(rect):
    rect.y += speed
    if rect.y >= high or player_rect.colliderect(rect) :
        rect.x, rect.y = random.randint(0, 400), 0

def mob_animations(list,rect):
    global mob_index
    mob_index += 0.4
    mob = list[int(mob_index)]
    screen.blit(mob, rect)
    if mob_index >= (len(list)-1):
        mob_index = 0

button = pygame.image.load("ground\\g1.png")
button_rect = button.get_rect(topleft = (200, 200))


##Trees
tree1 = pygame.image.load("trees\\t1.png")
tree2 = pygame.image.load("trees\\t2.png")
tree3 = pygame.image.load("trees\\t3.png")

###Tree rectangles
tree1_rect = tree1.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
tree1_rect1 = tree1.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
tree1_rect2 = tree1.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
tree1_rect3 = tree1.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
tree1_rect4 = tree1.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))

tree2_rect = tree2.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
tree2_rect1 = tree2.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
tree2_rect2 = tree2.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
tree2_rect3 = tree2.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
tree2_rect4 = tree2.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))

tree3_rect = tree3.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
tree3_rect1 = tree3.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
tree3_rect2 = tree3.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
tree3_rect3 = tree3.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))
tree3_rect4 = tree3.get_rect(topleft =(random.randint(0,width), random.randint(0,width)))

#Tree spawning mach
def tree_spawn(rect, rect2):
    global game_active, health
    rect.y += speed
    if rect.y >= high:
        rect.x, rect.y = random.randint(0, 460), -100
    if rect.colliderect(rect2):
        health -= 1
        rect.x, rect.y = random.randint(0, 460), -100

        if health == 0:
            game_active = False


#bullet_class
def create_bullet(x,y):
    bullet_rect = bullet.get_rect(center = (x,y))
    bullets.append(bullet_rect)

def update_bullet():
    for bull in bullets[:]:
        bull.y -= 10
        if bull.bottom < 0:
            bullets.remove(bull)



def bullet_hit(rect):
    global score
    for bull in bullets[:]:
        if bull.colliderect(rect):
            score += 10
            rect.x, rect.y = random.randint(0, 400), 0
            return score




run = True
game_started = False
game_active = True
game_over = True

while True:

        if game_active:
            if game_started:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT :
                            move_right = True
                        if event.key == pygame.K_LEFT :
                            move_left = True

                        elif event.key == pygame.K_SPACE:
                            create_bullet(player_rect.centerx, player_rect.top)

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT :
                            move_right = False
                        if event.key == pygame.K_LEFT :
                            move_left = False

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            game_started = True

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if play_button_rect.collidepoint(event.pos):
                            game_started = True

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if exit_button_rect.collidepoint(event.pos):
                            exit()


        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_u:
                        game_active = True
                        health = 5
                        score = 0





        if game_active:
            if game_started:
                screen.fill("white")

                screen.blit(grass1,grass1_rect1)
                screen.blit(grass2, grass1_rect2)
                screen.blit(grass3, grass1_rect3)
                screen.blit(grass4, grass1_rect4)
                screen.blit(grass1, grass1_rect5)
                screen.blit(grass2, grass1_rect6)
                screen.blit(grass3, grass1_rect7)
                screen.blit(grass4, grass1_rect8)


                # blitting images
                screen.blit(tree1, tree1_rect)
                screen.blit(tree1, tree1_rect1)
                screen.blit(tree1, tree1_rect2)
                screen.blit(tree1, tree1_rect3)

                screen.blit(tree3, tree3_rect)
                screen.blit(tree3, tree3_rect1)
                screen.blit(tree3, tree3_rect2)
                screen.blit(tree3, tree3_rect3)

                screen.blit(tree2, tree2_rect)
                screen.blit(tree2, tree2_rect1)
                screen.blit(tree2, tree2_rect2)
                screen.blit(tree2, tree2_rect3)

                player_animations(player_list)


                grass_spawn(grass1_rect1)
                grass_spawn(grass1_rect2)
                grass_spawn(grass1_rect3)
                grass_spawn(grass1_rect4)
                grass_spawn(grass1_rect5)
                grass_spawn(grass1_rect6)
                grass_spawn(grass1_rect7)
                grass_spawn(grass1_rect8)

                mob_animations(mob_list,mob_rect)
                mob_animations(mob_list, mob_rect2)
                mob_animations(mob_list, mob_rect3)
                mob_animations(mob_list, mob_rect4)

                mob_spawn(mob_rect)
                mob_spawn(mob_rect2)
                mob_spawn(mob_rect3)
                mob_spawn(mob_rect4)

                bullet_hit(mob_rect)
                bullet_hit(mob_rect2)
                bullet_hit(mob_rect3)
                bullet_hit(mob_rect4)

                text_surf = fontk.render(f"Score : {score}", True, "#a8a8a8")
                screen.blit(text_surf, (8,70))

                tree_spawn(tree1_rect,player_rect)
                tree_spawn(tree1_rect1,player_rect)
                tree_spawn(tree1_rect2,player_rect)
                tree_spawn(tree1_rect3,player_rect)

                tree_spawn(tree2_rect,player_rect)
                tree_spawn(tree2_rect1,player_rect)
                tree_spawn(tree2_rect2,player_rect)
                tree_spawn(tree2_rect3,player_rect)

                tree_spawn(tree3_rect,player_rect)
                tree_spawn(tree3_rect1,player_rect)
                tree_spawn(tree3_rect2,player_rect)
                tree_spawn(tree3_rect3,player_rect)

                for bull in bullets:
                    screen.blit(bullet, bull.topleft)

                if move_left == True :
                    player_rect.x -= player_speed
                elif move_right == True:
                    player_rect.x += player_speed
                else:
                    player_rect.x += 0

                if player_rect.x >= (width):
                    player_rect.x = 490
                if player_rect.x <= 0:
                    player_rect.x = 0

                update_bullet()
                health_logic()

            else:

                screen.blit(space, space_rect)
                #screen.fill("white")
                screen.blit(game_name, (65, 64))
                #screen.blit(ground_s, (0,314))
                screen.blit(play_button, play_button_rect)
                screen.blit(exit_button, exit_button_rect)


                if space_rect.right <= 510:
                    space_rect.right = 510
                    bv = -5
                if space_rect.left <= -1600:
                    space_rect.left = -5
                    bv = 5
                space_rect.x -= bv

                space_rect.x -= 5

        else:
            screen.blit(space, space_rect)
            screen.blit(game_over_img, game_over_rect)
            if space_rect.right <= 510:
                space_rect.right = 510
                bv = -5
            if space_rect.left <= -1600:
                space_rect.left = -5
                bv = 5
            space_rect.x -= bv

            space_rect.x -= 5

        pygame.display.update()
        pygame.time.delay(27)