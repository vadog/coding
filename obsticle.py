import pygame

pygame.init()

win= pygame.display.set_mode((500,480))

run = True
FRAMERATE = 60
clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsans", 30, True)
font1 = pygame.font.SysFont("comicsans", 40, True)



px = 40
py = 300
gamerun = True
isjump = False
jumpcount = 10
spikeclear = True
spikes = []
score = 0
scorer = True
class sp1ke():
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.color =  color
        self.vel = 10


    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x,self.y, self.width, self.height))



while run:
    win.fill((0,0,0))
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

  
    clock.tick(FRAMERATE)
        
    x,y = pygame.mouse.get_pos()
  
  
    keys= pygame.key.get_pressed()

    if gamerun:

        pygame.draw.rect(win,(0,0,255),(px,py,50,50))

        pygame.draw.line(win,(50,200,0),(550,350),(-10,350))

    
    
    
        if not isjump:     
            if keys[pygame.K_UP]:   
                isjump = True 
            
        else:
            if jumpcount >= -10:
                neg = 1
                if jumpcount < 0:
                    neg = -1
                py -= jumpcount ** 2 * 0.5 * neg 
                jumpcount -= 1 

            else:
                isjump = False
                jumpcount = 10 

        for spike in spikes:
            if spike.x > -50: 
                spike.x -= spike.vel
            else:
                spikes.pop(spikes.index(spike))
                spikeclear = True
                scorer = True

        
        if spikeclear:
            spikes.append(sp1ke ( 550,320,30,30,(50,200,0) ))
            spikeclear = False
        

        for spike in spikes:
            if spike.x < px and spike.x > px - 50 :
                if spike.y < py + 50 :
                    pygame.time.delay(1000)
                    gamerun= False
    
            if spike.x < px- 50:
                if scorer:
                    score += 1
                    scorer = False

        for spike in spikes:
            spike.draw(win)
        
        
        
        text = font.render("Score: "+ str(score), 1, (235,0,0))
        win.blit(text, (20 ,10))
    else:
        text2 = font1.render("Your score: "+ str(score), 1, (235,0,0))
        win.blit(text2, (250- text2.get_width()/2 ,200))
        pygame.draw.rect(win,(0,0,255),(150,250,200,50))
        text3 = font.render("Play Again", 1, (235,0,0))
        win.blit(text3, (250-(text3.get_width()/2) , 275-(text3.get_height()/2)))
        
        if x > 150 and x < 350 and y > 250 and y < 300:
            if event.type == pygame.MOUSEBUTTONDOWN:
                gamerun = True
                isjump = False
                jumpcount = 10
                spikeclear = True
                spikes = []
                score = 0
                scorer = True
                px = 40
                py = 300
   
   
    pygame.display.update()
     


pygame.quit()
