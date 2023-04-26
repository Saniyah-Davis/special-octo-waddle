import pygame

screen = pygame.display.set_mode((831,519))
pygame.display.set_caption('Run, Hooter, Run')

def menu():
    image = pygame.image.load('images/Hooter-Lounging.jpg')
    image = pygame.transform.scale(image, (831,519))
    while True:
        screen.blit(image,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(300,325) and event.pos[1] in range(200,228):
                    #play button is 100pi by 101pi
                    game()

def game():
    image = pygame.image.load('images/background image temple.jpeg')
    image = pygame.transform.scale(image, (831,519))
    bgx = 0 
    while True:
        screen.blit(image,(bgx-831,0))
        screen.blit(image,(0,0))
        screen.blit(image,(bgx+831,0))

        bgx = bgx - 1
        if bgx <= -831:
            bgx =  0

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.pos[0] in range(300,325) and event.pos[1] in range(200,228):
                    print('space')
#menu()
game()
