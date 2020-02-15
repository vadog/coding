import pygame

pygame.init()

win= pygame.display.set_mode((500,480))

run = True


x = 40
y = 300

isjump = False
jumpcount = 10
spikeclear = True
spikes = []

class sp1ke():
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.color =  color
        self.vel = 5


    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x,self.y, self.width, self.height))




while run:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys= pygame.key.get_pressed()

    pygame.draw.rect(win,(0,0,255),(x,y,50,50))

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

    for spike in spikes:
        if spike.x > -50:
            spike.x -= spike.vel
        else:
            spikes.pop(spikes.index(spike))
            spikeclear = True

    
    if spikeclear:
        spikes.append(sp1ke ( 400,320,30,30,(0,0,255) ))
        spikeclear = False


    for spike in spikes:
        spike.draw(win)
    pygame.display.update()


pygame.quit()
