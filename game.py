import pygame

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
    image = pygame.image.load('images/skywalk.jpg')
    image = pygame.transform.scale(image, (831,519))
    bgx = 0 

    player = pygame.image.load('images/owl sprite.png')
    player = pygame.transform.rotozoom(player,0,0.2)
    while True:
        screen.blit(image,(bgx-831,0))
        screen.blit(image,(bgx,0))
        screen.blit(image,(bgx+831,0))

        bgx = bgx - .1
        if bgx <= -831:
            bgx = 0

        screen.blit(player,(50,325))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.pos[0] in range(295,365) and event.pos[1] in range(130,200):
                    print('space')
menu()