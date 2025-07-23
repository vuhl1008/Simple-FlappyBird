from Bird import Bird
from Pipe import Pipe
from ListPipe import ListPipe
from score import Score
import random
import pygame
pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
#Load image
bird1_img=pygame.image.load("../assets/yellowbird-downflap.png").convert_alpha()
bird2_img=pygame.image.load("../assets/yellowbird-midflap.png").convert_alpha()
bird3_img=pygame.image.load("../assets/yellowbird-upflap.png").convert_alpha()
pipe_img=pygame.image.load("../assets/pipe.png").convert()
floor_img=pygame.image.load("../assets/base.png").convert()
bg_img=pygame.image.load("../assets/background.png").convert()

#scale image
pipe_surface=pygame.transform.scale2x(pipe_img)
bg=pygame.transform.scale2x(bg_img)
floor=pygame.transform.scale2x(floor_img)

#initialize
bird_timer=pygame.USEREVENT+1
pygame.time.set_timer(bird_timer, 200)
pipe_timer = pygame.USEREVENT
pygame.time.set_timer(pipe_timer, random.randint(600,1200))
birds=[bird1_img,bird2_img,bird3_img]
bird=Bird(birds,50,200)
pipeList=ListPipe()
player_score=Score()
floor_x=0
game_over=False
running =True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            #Jump
            if event.key==pygame.K_SPACE:
                bird.jump()
            #reset game
            if event.key==pygame.K_r:
                game_over=False
                bird = Bird(birds, 50, 200)
                # Reset pipes
                pipeList.clear()
                bird.pipes.clear()
                # Reset score
                player_score.score = 0
                # Reset floor
                floor_x = 0

            if game_over and event.key==pygame.K_x:
                running=False
            #create pipe
        if event.type==pipe_timer:
            if not game_over:
             pipe = Pipe(pipe_surface)
             pipe.create()
             pipeList.append(pipe)
             bird.pipes.append(pipe)
             player_score.score+=1
            
            #update bird
        if event.type==bird_timer:
            bird.update()

            #check_collision
        if bird.checkcollision():
           game_over=True




    pipeList.move_pipe()
    bird.move()
    floor_x-=1
    screen.fill((0, 0, 0))
    screen.blit(bg,(0,0))
    if not game_over:
        bird.draw(screen)
        pipeList.draw_pipes(screen)
    else:
        if player_score.score>player_score.high_score:
           player_score.high_score=player_score.score
        player_score.displayHighScore(screen)


    screen.blit(floor,(floor_x ,600))
    screen.blit(floor,(floor_x+432 ,600))
    if floor_x<=- floor.get_width():
        floor_x=0
    player_score.displayScore(screen)
    pygame.display.update()
    clock.tick(60)
pygame.quit()



