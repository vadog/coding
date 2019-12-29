import pygame
import random 

pygame.init()

win= pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game")

run = True


cx = random.randrange(100,900) 
cy = random.randrange(100,900) 

score = 0

font = pygame.font.SysFont("comicsans", 30, True)
font1 = pygame.font.SysFont("comicsans", 80, True)

start_ticks=pygame.time.get_ticks()

time = 60

while run:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    

    seconds= round((pygame.time.get_ticks()-start_ticks)/1000)

    
    countdown = time- seconds
    if countdown < 0:
        countdown = 0

    
    
    x,y = pygame.mouse.get_pos()
    
    if countdown > 0:
        if x > cx - 60 and x < cx + 60:
            if y > cy -60 and y < cy + 60:
                cx = random.randrange(100,900) 
                cy = random.randrange(100,900) 
                score += 1
        pygame.draw.circle(win, (244,0,0), (cx,cy), 60)
    else: 
        text2 = font1.render("Times up you got "+ str(score)+" hits", 1, (235,0,0))
        win.blit(text2, (500- text2.get_width()/2 ,500))


    text = font.render("Score: "+ str(score), 1, (235,0,0))
    win.blit(text, (20 ,10))
    
    text1 = font.render("Time: "+ str(countdown), 1, (235,0,0))
    win.blit(text1, (980- text1.get_width() ,10))
    
   
    
    
    
    pygame.display.update()


pygame.quit()