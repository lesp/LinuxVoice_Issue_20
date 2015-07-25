#Import modules
from sys import argv
import zbar
from time import sleep
import pygame
from random import randint

#Pygame Setup
pygame.init()
pygame.mixer.init()


#Variables
global item
global HP
global MP

#Function to scan barcode
def scanner():
    global item
    proc = zbar.Processor()
    proc.parse_config('enable')
    device = '/dev/video1'
    if len(argv) > 1:
        device = argv[1]
    proc.init(device)
    proc.visible = True
    proc.process_one()
    proc.visible = False
    for symbol in proc.results:
        item = symbol.data
        print(item)
        return(item)


#Function to create character
"""
def character():
    scanner()
"""    

#Function to randomise character stats based on barcode
def randomiserHP():
    global item
    item = int(item)
    HP = item / randint(120000000000,130000000000)
    print("Your HP is "+str(HP))

def randomiserMP():
    global item
    global MP
    item = int(item)
    MP = item / randint(120000000000,130000000000)
    print("Your MP is "+str(MP))

#Enemy Character
def enemy():
    enemyHP = randint(30,90)
    enemyMP = randint(30,90)
    print("Your enemy appears before you and has "+str(enemyHP)+" hit points and "+str(enemyMP)+" magic points.")



#Main Loop
try:
    #Setup the player
    scanner()
    randomiserHP()
    sleep(1)
    scanner()
    randomiserMP()
    enemy()        
except KeyboardInterrupt:
    print("Exit")

#Conditionals
