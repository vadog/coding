import pygame

pygame.init()

win= pygame.display.set_mode((500,480))

run = True


x = 40
y = 300

isjump = False
jumpcount = 10


while run:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys= pygame.key.get_pressed()

    pygame.draw.rect(win,(0,0,255),(x,y,100,100))

    if not isjump:     
        if keys[pygame.K_UP]:   
            isjump = True 
          
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            y -= jumpcount ** 2 * 0.5 * neg 
            jumpcount -= 1 

        else:
            isjump = False
            jumpcount = 10

    
    pygame.display.update()


pygame.quit()
