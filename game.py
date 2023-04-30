import pygame
import random
from playsound import playsound
playsound('t-for-temple.mp3')

screen = pygame.display.set_mode((831,519))
pygame.display.set_caption('Run, Hooter, Run')
obstacles = ['images/rosen sprite.png','images/t.png','images/cherry.png', 'images/basketball.png']

def menu():
    image = pygame.image.load('images/menu play.jpg')
    image = pygame.transform.scale(image, (831,519))
    while True:
        screen.blit(image,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(300,400) and event.pos[1] in range(100,200):
                    #play button is 70pi by 70pi
                    intro()

def game():
    image = pygame.image.load('images/background image temple.jpeg')
    image = pygame.transform.scale(image, (831,519))
    bgx = 0 

    player = pygame.image.load('images/owl sprite.png')
    player = pygame.transform.rotozoom(player,0,0.2)
    player_y = 400
    gravity = .8
    #jumpcount = 0
    jump = False

#obstacle 1
    obs = pygame.image.load(random.choice(obstacles))
    obs = pygame.transform.rotozoom(obs, 0,0.8)
    obs_x = 900
    obs_y = 400
    obs_speed = random.uniform(.5,1)

#obstacle 2
    obs2 = pygame.image.load(random.choice(obstacles))
    obs2 = pygame.transform.rotozoom(obs2, 0,0.8)
    obs2_x = 1400
    obs2_y = 400
    obs2_speed = random.uniform(.5,1)

    while True:
        screen.blit(image,(bgx-831,0))
        screen.blit(image,(bgx,0))
        screen.blit(image,(bgx+831,0))

        bgx = bgx - .1
        if bgx <= -831:
            bgx = 0

        p_rect = screen.blit(player,(50, player_y))
        if player_y < 400:
            player_y += gravity
        if jump == True:
            player_y = player_y - 2
            if player_y < 0:
                player_y = 0
    
        o_rect = screen.blit(obs,(obs_x,obs_y))
        obs_x -= obs_speed

        o2_rect = screen.blit(obs2,(obs2_x,obs2_y))
        obs2_x -= obs2_speed

        """if obs_x < 400:
            obs2 = pygame.image.load(random.choice(obstacles))
            obs2_x = 1000
            obs2_y = random.uniform(0,519)
            obs2_speed = random.uniform(.5,1)"""

        if obs_x < -100:
            obs = pygame.image.load(random.choice(obstacles))
            obs = pygame.transform.rotozoom(obs, 0,0.8)
            obs_x = 900
            obs_y = random.uniform(0,400)
            obs_speed = random.uniform(.5,1)

        if obs2_x < -100:
            obs2 = pygame.image.load(random.choice(obstacles))
            obs2 = pygame.transform.rotozoom(obs2, 0,0.8)
            obs2_x = 1000
            obs2_y = random.uniform(0,400)
            obs2_speed = random.uniform(.5,1)
              
        if p_rect.colliderect(o_rect) or p_rect.colliderect(o2_rect):
            return

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                jump = True
            if event.type == pygame.KEYUP:
                jump = False

def intro():
    image = pygame.image.load('images/intro.jpg')
    image = pygame.transform.scale(image, (831,519))
    while True:
        screen.blit(image,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(600,800) and event.pos[1] in range(350,500):
                    #play button is 70pi by 70pi
                    game()

menu()