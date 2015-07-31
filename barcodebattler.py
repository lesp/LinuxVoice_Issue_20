#Barcode Battler

#Import modules
from sys import argv
import zbar
import random
import pygame
import time

#Variable
global player
global enemyHP
global enemyMP
global enemy_name
global weapon
global equip
global code

#Functions
def scanner():
    global code
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
        code = symbol.data

#Choose player, this is handled via QR codes on cards.
def player():
	global code
	global player
	if code == "Andrew":
		print("Andrew is your warrior")
		HP = random.randint(0,100)
		MP = random.randint(0,50)
		player = "Andrew"
		print(player+" has "+str(HP)+" HP and "+str(MP)+" MP")
	elif code == "Ben":
		print("Ben is your warrior")
		HP = random.randint(0,100)
		MP = random.randint(0,50)
		player = "Ben"
		print(player+" has "+str(HP)+" HP and "+str(MP)+" MP")
	elif code == "Graham":
		print("Graham is your warrior")
		HP = random.randint(0,100)
		MP = random.randint(0,50)
		player = "Graham"
		print(player+" has "+str(HP)+" HP and "+str(MP)+" MP")
	elif code == "Mike":
		print("Mike is your warrior")
		HP = random.randint(0,100)
		MP = random.randint(0,50)
		player = "Mike"
		print(player+" has "+str(HP)+" HP and "+str(MP)+" MP")

	else:
		print("Player not recognised, please scan one of the cards to continue")
		


#Generate an enemy.
def enemy():
        global enemy_name
        global enemyHP
        global enemyMP
        enemy_names = ["Windows10","Killersaur","MegaDave","OpenSourcerer"]
        enemy_name = random.choice(enemy_names)
        enemyHP = random.randint(0,100)
        enemyMP = random.randint(0,50)
        print("Your enemy is "+enemy_name)
        print("They have "+str(enemyHP)+" HP and "+str(enemyMP)+" MP")
              

#Equip player with a weapon
def weapon():
        global code
        global weapon
        scanner()
        print(code)
        value = int(code) / 13000000000000 / random.randint(0,10)
        print(value)
        if value > 0 and value < 5:
                print("You have a basic wooden sword")
                weapon = ("wooden_sword")
        elif value > 5 and value < 11:
                print("You have a steel sword")
                weapon = ("steel_sword")
        elif value == 0:
                print("You have no sword...you will have to use your fists of fury!")
                weapon = ("fists")
        else:
                print("You have an enchanted sword of mega power")
                weapon = ("enchanted_sword")

def equip():
        global code
        global equip
        scanner()
        print(code)
        value = int(code) / 1300000000000 / random.randint(0,10)
        print(value)
        if value > 0 and value < 5:
                print("You have a basic wooden shield")
                equip = ("wood_shield")
        elif value > 5 and value < 11:
                print("You have an iron shield")
                equip = ("iron_shield")
        elif value == 0:
                print("You have no shield...that sucks")
                equip = ("nothing")
        else:
                print("You have a mirrored shield that can reflect half damage to your attacker")
                equip = ("mirror_shield")

#T E S T I N G
scanner()
print(code)
player()
enemy()
time.sleep(5)
weapon()
time.sleep(5)
equip()

###BATTLE###

#Like Final Fantasy we choose who goes first using random.choice
combatants = ["warrior","enemy"]
attacker = random.choice(combatants)
print(attacker)

#For each attack a random number is used.
#For enemy it is a random number with max value being MP
#For player this is the MP + their weapon

#If the player HP == 0 then it's game over.
#If the enemy HP == 0 then the player wins the game
#Else we keep doing this until someone is dead.
