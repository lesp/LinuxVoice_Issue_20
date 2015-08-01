import pygame
import time
pygame.init()

def picture(img,w,h):
    pic = pygame.image.load(img)
    background = (0, 0, 0)
    screen = pygame.display.set_mode((w,h))
    screen.fill((background))
    screen.blit(pic,(0,0))
    pygame.display.flip()
    time.sleep(3)
    pygame.display.quit()

def audio(music):
    pygame.mixer.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(1)

def pic_text():
    pygame.font.init()
    screen = pygame.display.set_mode((800,600))
    background = (0, 0, 0)
    screen.fill((background))
    
    
    
    pygame.display.flip()
    for i in range(10):
        background = (128, 0, 0)
        screen.fill((background))
        myfont = pygame.font.Font(None, 60)
        info1 = myfont.render("PREPARE FOR BATTLE",1,(0,255,0))
        screen.blit(info1, (150,300))
        pygame.display.flip()
        time.sleep(0.3)
        background = (0, 0, 128)
        screen.fill((background))
        myfont = pygame.font.Font(None, 60)
        info1 = myfont.render("PREPARE FOR BATTLE",1,(0,255,255))
        screen.blit(info1, (150,300))
        pygame.display.flip()
    pygame.display.quit()

pic_text()
#audio("intro.mp3")
#picture("masthead.gif",500,229)


