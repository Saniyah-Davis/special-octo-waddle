import pygame

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Run, Hooter, Run')

def menu():
    image = pygame.image.load('images/Hooter-Lounging.jpg')
    image = pygame.transform.scale(image, (640,480))
    while True:
        screen.blit(image,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(300,325) and event.pos[1] in range(200,228):
                    game()

def game():
    image = pygame.image.load('background image temple.jpeg')
    image = pygame.transform.scale(image, (640,480))
    while True:
        screen.blit(image,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.pos[0] in range(300,325) and event.pos[1] in range(200,228):
                    print('space')
menu()
