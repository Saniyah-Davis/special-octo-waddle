import pygame
import random

screen = pygame.display.set_mode((831,519))
pygame.display.set_caption('Run, Hooter, Run')

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
                    game()

def game():
    image = pygame.image.load('images/background image temple.jpeg')
    image = pygame.transform.scale(image, (831,519))
    bgx = 0 

    player = pygame.image.load('images/owl sprite.png')
    player = pygame.transform.rotozoom(player,0,0.2)
    player_y = 200
    gravity = .8
    #jumpcount = 0
    jump = False

    cherry = pygame.image.load('images/basketball.png')
    cherry = pygame.transform.rotozoom(cherry, 0,0.8)
    cherry_x = 800
    cherry_speed = .1

    while True:
        screen.blit(image,(bgx-831,0))
        screen.blit(image,(bgx,0))
        screen.blit(image,(bgx+831,0))

        bgx = bgx - .1
        if bgx <= -831:
            bgx = 0

        p_rect = screen.blit(player,(50, player_y))
        if player_y < 200:
            player_y += gravity
        if jump == True:
            player_y = player_y - 2
            if player_y < 0:
                player_y = 0
                
        c_rect = screen.blit(cherry,(cherry_x,200))
        cherry_x -= cherry_speed
        if cherry_x < -50:
            cherry_x = random.randint(700,800)
            cherry_speed = random.randint(1,5)

        if p_rect.colliderect(c_rect):
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
menu()