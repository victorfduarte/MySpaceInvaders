'''import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

crashed = False

counter = pygame.time.get_ticks()
time = 1000
to_tick = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True            

        elif event.type == pygame.KEYDOWN:
            counter = pygame.time.get_ticks()
            to_tick = True
            print('HI')
        
        elif event.type == pygame.KEYUP:
            to_tick = False
        
        if to_tick:
            now = pygame.time.get_ticks()
            if now - counter >= time:
                counter = now
                print('HI')
    
    pygame.display.update()
    clock.tick(500)
'''

def func1():
    pass

def func2():
    pass

def func3():
    pass

lista = [func1, func2, func3]

for item in lista:
    item