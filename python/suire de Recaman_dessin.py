import pygame
import random
import time 
#Init the pygame engine 
pygame.init()

# Screen size :
screenH=600
screenW=800
size = [screenW,screenH]

# create a screen object :
screen = pygame.display.set_mode(size)

# important : the window's caption :
pygame.display.set_caption("Recaman algorithm")


def estabsente(serie,valeur):
    for n in range(0,len(serie)):
        if serie[n]==valeur:
            return False
    return True
'''
s = [2,3,4,5,0,20,33,11,35]
print(estabsente(s,9))
print(9 not in s)
'''
def recaman(maxi):
    serie=[]
    for n in range(0,maxi+1):
        if n==0:
            valeur = 0
        elif serie[n-1]-n>0 and estabsente(serie,serie[n-1]-n):
            valeur = serie[n-1]-n
        else :
            valeur = serie[n-1]+n
        serie.append(valeur)
    return serie


def draw_recaman(serie):
    '''
    fucntion taht draw the serie passed in parameter
    '''
    factor = 2
    start = serie[0]
    for index,number in enumerate(serie[1:]):
        pos = start
        diam=index+1
        if index%2==0:
            ang_deb=0
            ang_end=3.1415
        else :
            ang_deb=3.1415
            ang_end=0
        if number-start<0:
            pos=number
        col = pygame.Color(0,0,0)
        col.hsva = (index%255,100,100,2)
        pygame.draw.arc(screen,col,[pos*factor,(screenH/2)-diam*factor/2,factor*diam,factor*diam],ang_deb,ang_end,2)
        start = number
        if index%1000==0 : print(index)
        #updte gfx :
        pygame.display.flip()
        time.sleep(0.01)
    
s = recaman(20000)
draw_recaman(s)


while True:
    # ===============================
    # ==== manage events (keys....)
    # force all events to be processed : 
    pygame.event.pump()
    for event in pygame.event.get():
        # if a key is pressed :
        if event.type == pygame.KEYDOWN :
            # and the key is ESCAPE :
            if event.key == pygame.K_ESCAPE:
                pygame.quit() # close pygame
                raise SystemExit #for a system close
            if event.key == pygame.K_s:
                pygame.image.save(screen, "screenshot.jpg")

    # ===============================
    # ==== Drawing
    
   
pygame.quit()




