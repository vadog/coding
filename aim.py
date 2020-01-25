import pygame
import random 

pygame.init()

win= pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game")

prgrmrun = True
gamerun = True


cx = random.randrange(100,900) 
cy = random.randrange(100,900) 

score = 0

font = pygame.font.SysFont("comicsans", 30, True)
font1 = pygame.font.SysFont("comicsans", 80, True)

currenttime = 0
intercounter1 = 0
time = 5

while prgrmrun:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            prgrmrun = False
     
    
    if gamerun == False:
        score = 0
        currenttime = intercounter - intercounter
        countdown = time - currenttime
        gamerun = True
        

    if gamerun == True:    
        countdown = time - currenttime
        intercounter = round((pygame.time.get_ticks())/1000)
        if intercounter1 != intercounter:
            currenttime += 1
        intercounter1 = intercounter

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
            pygame.draw.rect(win,(0,0,255),(400,600,200,50))
            text3 = font.render("Play Again", 1, (235,0,0))
            win.blit(text3, (500-(text3.get_width()/2) , 625-(text3.get_height()/2)))

            
            if x > 400 and x < 600 and y > 600 and y < 650:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gamerun = False
    



        text = font.render("Score: "+ str(score), 1, (235,0,0))
        win.blit(text, (20 ,10))
        
        text1 = font.render("Time: "+ str(countdown), 1, (235,0,0))
        win.blit(text1, (980- text1.get_width() ,10))
        
        
        pygame.display.update()


pygame.quit()